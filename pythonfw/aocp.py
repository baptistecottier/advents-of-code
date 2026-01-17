#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
Advent of Code puzzle runner and utility functions.
"""

# Standard import
import argparse
import builtins
import datetime
import io
import json
import multiprocessing
import os
import sys
import threading
import traceback
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path

# Third-party import
from aocd.models import Puzzle
from aocd.exceptions import AocdError
from aocd import submit


# ===========================================================================
# Utility Functions
# ===========================================================================

def color_text(txt: str, color: str):
    """
    Return the given text string wrapped in ANSI color codes for terminal output.

    Args:
        txt (str): The text to color.
        color (str or None): The name of the color (e.g., 'red', 'green').
                             If None, returns the text unchanged.

    Returns:
        str: The colored text with ANSI escape codes, or the original text if color is None.

    Examples:
        >>> color_text("Hello", "red")
        '\\x1b[31mHello\\x1b[0m'
    """
    ansi_colors = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    if color is None:
        return txt
    code = ansi_colors.index(color.casefold())
    reset = "\x1b[0m"
    return f"\x1b[{code + 30}m{txt}{reset}"


def _check_example_answers(my_answers, answer_a, answer_b):
    """Check if example answers match expected results."""
    if isinstance(my_answers, tuple):
        my_a = my_answers[0] if len(my_answers) > 0 else None
        my_b = my_answers[1] if len(my_answers) > 1 else None
    else:
        my_a, my_b = my_answers, None

    a_correct = str(my_a) == str(answer_a) if answer_a else True
    b_correct = str(my_b) == str(answer_b) if answer_b and my_b else True

    return a_correct and b_correct


def _format_answers(answers):
    """Format answers for display."""
    if isinstance(answers, tuple):
        return ", ".join(str(a) for a in answers)
    return str(answers)


def _process_example_data(day_module, data):
    """Process example data and prepare arguments."""
    if "get_example_input" in dir(day_module):
        return day_module.get_example_input(data)
    return data.get("input", data)


def _solve_example(day_module, example_args):
    """Solve a single example."""
    try:
        result = day_module.solver(example_args)
        return result
    except (TypeError, ValueError, KeyError, AttributeError):
        return None


def solve_examples(puzzle, details=False):
    """Load examples from file and test them."""
    day_str = str(puzzle.day).zfill(2)
    day_module_path = Path(f"./events/year_{puzzle.year}/day_{day_str}")

    if not day_module_path.exists():
        return []

    sys.path.insert(0, str(day_module_path))
    day_module = __import__(f"day_{day_str}")

    examples = load_examples_from_file(puzzle)
    if not examples:
        return []

    results = []
    for i, example in enumerate(examples, 1):
        example_input = _process_example_data(day_module, example)
        my_answer = _solve_example(day_module, example_input)
        answer_a = example.get("expected_a")
        answer_b = example.get("expected_b")
        is_correct = _check_example_answers(my_answer, answer_a, answer_b)

        if details:
            print(f"  Example {i}: {'✅' if is_correct else '❌'} "
                  f"(got {_format_answers(my_answer)})")
            if not is_correct:
                if answer_a:
                    print(f"    Expected part A: {answer_a}")
                if answer_b:
                    print(f"    Expected part B: {answer_b}")

        results.append(is_correct)

    return results


def save_examples_to_file(puzzle: Puzzle, examples: list) -> bool:
    """Save examples to a .examples file."""
    day_str = str(puzzle.day).zfill(2)
    examples_dir = Path(f"./events/year_{puzzle.year}/day_{day_str}")
    examples_dir.mkdir(parents=True, exist_ok=True)

    examples_path = examples_dir / f"day_{day_str}.examples"

    try:
        with open(examples_path, 'w', encoding='utf-8') as f:
            json.dump(examples, f, indent=2, ensure_ascii=False)

        print(f"  💾 Examples saved to: {examples_path}")
        return True
    except (OSError, IOError) as e:
        print(f"  ❌ Failed to save examples: {e}")
        return False


def load_examples_from_file(puzzle: Puzzle) -> list:
    """Load examples from a .examples file if it exists."""
    day_str = str(puzzle.day).zfill(2)
    examples_path = Path(f"./events/year_{puzzle.year}/day_{day_str}/day_{day_str}.examples")

    if not examples_path.exists():
        return []

    try:
        with open(examples_path, 'r', encoding='utf-8') as f:
            examples = json.load(f)

        print(f"  📁 Loaded {len(examples)} examples from: {examples_path}")
        return examples
    except (OSError, IOError, json.JSONDecodeError) as e:
        print(f"  ⚠️ Failed to load examples file: {e}")
        return []


def extract_examples_from_puzzle(puzzle: Puzzle, force_refresh: bool = False) -> list:
    """Extract examples from puzzle description - proof of concept."""
    # First, try to load from existing .examples file (unless forced refresh)
    if not force_refresh:
        existing_examples = load_examples_from_file(puzzle)
        if existing_examples:
            return existing_examples

    # For now, return some known examples for demonstration
    # In a full implementation, this would parse the puzzle webpage
    known_examples = {
        # 2015 Day 1 examples
        (2015, 1): [
            {'input': '(())', 'expected_a': '0', 'expected_b': None},
            {'input': '()()', 'expected_a': '0', 'expected_b': None},
            {'input': '(((', 'expected_a': '3', 'expected_b': None},
            {'input': '())', 'expected_a': '-1', 'expected_b': None},
            {'input': ')))', 'expected_a': '-3', 'expected_b': None},
        ],
        # 2020 Day 1 examples
        (2020, 1): [
            {'input': '1721\n979\n366\n299\n675\n1456', 'expected_a': '514579', 'expected_b': None},
        ],
    }

    key = (puzzle.year, puzzle.day)
    if key in known_examples:
        examples_count = len(known_examples[key])
        print(f"  📚 Found {examples_count} known examples for {puzzle.year} day {puzzle.day}")
        examples = known_examples[key]
        # Save the examples for future use
        save_examples_to_file(puzzle, examples)
        return examples

    print(f"  ❓ No known examples for {puzzle.year} day {puzzle.day}")
    return []


def save_input_to_file(puzzle: Puzzle, verbose: bool = True) -> bool:
    """Save puzzle input to a local .input file."""
    day_str = str(puzzle.day).zfill(2)
    input_dir = Path(f"./events/year_{puzzle.year}/day_{day_str}")
    input_dir.mkdir(parents=True, exist_ok=True)

    input_path = input_dir / f"day_{day_str}.input"

    try:
        with open(input_path, 'w', encoding='utf-8') as f:
            f.write(puzzle.input_data)

        if verbose:
            print(f"  💾 Input saved to: {input_path}")
        return True
    except (OSError, IOError) as e:
        if verbose:
            print(f"  ❌ Failed to save input: {e}")
        return False


# ============================================================================
# Main aocp Functions
# ============================================================================


def _submit_answer(answer, part, puzzle):
    """Submit answer to AOC and capture output."""
    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()

    part_letter = "a" if part == 1 else "b"

    with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
        if isinstance(answer, builtins.tuple):
            fixed_part, fixed_answer = answer
            submit_result = submit(fixed_answer, fixed_part, puzzle.day, puzzle.year)
        else:
            submit_result = submit(str(answer), part_letter, puzzle.day, puzzle.year)

    output = stdout_capture.getvalue() + stderr_capture.getvalue()
    return submit_result, output


def _parse_submission_result(submit_result, output):
    """Parse AOC submission result and return status info."""
    # Define status mappings
    correct_statuses = [
        (submit_result is None and "aocd will not submit" in output,
            "✅ Correct (already known)", "green"),
        ("already solved with same answer" in output, "✅ Correct (already solved)", "green"),
        ("That's the right answer" in output, "🎉 Correct (new submission)", "green")
    ]

    incorrect_statuses = [
        ("already solved with different answer" in output,
         "🤔 Incorrect (but already solved)", "yellow", True),
        ("That's not the right answer" in output, "❌ Incorrect", "red", False),
        ("You gave an answer too recently" in output, "⏰ Rate limited", "yellow", False)
    ]

    # Check for correct answers
    for condition, message, color in correct_statuses:
        if condition:
            return True, True, color_text(message, color)

    # Check for incorrect answers
    for condition, message, color, is_solved in incorrect_statuses:
        if condition:
            return False, is_solved, color_text(message, color)

    # Default case for unexpected responses
    print(f"  ⚠️  Unexpected submission response:\n{output}")
    return False, False, color_text("📤 Submitted", "blue")


def _handle_aocd_error(error_msg):
    """Handle AocdError and return status info."""
    if "is certain that" in error_msg and "is incorrect" in error_msg:
        return False, False, color_text("❌ Incorrect (cached)", "red")
    if "already solved" in error_msg:
        return True, True, color_text("✅ Correct (already solved)", "green")
    return False, False, color_text(f"⚠️  {error_msg[:50]}", "yellow")


def _handle_network_error(error):
    """Handle network errors and return status message."""
    error_type = type(error).__name__
    if "SSL" in error_type or "certificate" in str(error).lower():
        return "❌ SSL/Certificate error (network issue)"
    if "Connection" in error_type or "Timeout" in error_type:
        return "❌ Network error"
    return f"⚠️  {error_type}"


def _show_timeout_message(timeout_seconds, part, total_parts):
    """Show timeout message if needed."""
    if timeout_seconds is not None and part == total_parts:
        print(f"    ⏱️ Solver execution timed out after {timeout_seconds} seconds")


def parse_and_display_results(answers, puzzle, timeout_seconds=None):
    """Parse and nicely display the puzzle results with colored output.

    Returns: tuple - (all_results_correct, parts_solved_on_aoc) where:
        - all_results_correct: bool, True if solver gave correct answers
        - parts_solved_on_aoc: tuple, which parts are actually solved on AOC (1, 2, or both)
    """
    print("📊 Results:")
    all_results_correct = True
    parts_solved = []

    for part, answer in enumerate(answers, 1):
        medal = "🥇" if part == 1 else "🥈"
        is_correct = True
        is_solved_on_aoc = False

        try:
            submit_result, output = _submit_answer(answer, part, puzzle)
            is_correct, is_solved_on_aoc, colored_status = _parse_submission_result(submit_result,
                                                                                    output)

            print(f"  {medal} Part {part}: {answer} - {colored_status}")
            _show_timeout_message(timeout_seconds, part, len(answers))

        except AocdError as e:
            is_correct, is_solved_on_aoc, colored_status = _handle_aocd_error(str(e))
            print(f"  {medal} Part {part}: {answer} - {colored_status}")
            _show_timeout_message(timeout_seconds, part, len(answers))

        except (ConnectionError, TimeoutError, OSError) as e:
            status_msg = _handle_network_error(e)
            print(f"  {medal} Part {part}: {answer} - {color_text(status_msg, 'red')}")
            is_correct = False
            _show_timeout_message(timeout_seconds, part, len(answers))

        if not is_correct:
            all_results_correct = False

        if is_solved_on_aoc:
            parts_solved.append(part)

    return (all_results_correct, tuple(parts_solved))


class SolverTimeoutError(Exception):
    """Custom timeout exception for solver execution."""
    pass


def _preprocessing_wrapper(preprocessing_func, data, timeout_seconds):
    """Run preprocessing with timeout using threading.

    Args:
        preprocessing_func: Function to run
        data: Input data
        timeout_seconds: Timeout in seconds

    Returns:
        Result from preprocessing_func

    Raises:
        SolverTimeoutError if preprocessing times out
    """
    result_container = []
    exception_container = []

    def run_preprocessing():
        try:
            result_container.append(preprocessing_func(data))
        except (OSError, ValueError, KeyError, TypeError) as e:
            exception_container.append(e)

    thread = threading.Thread(target=run_preprocessing, daemon=True)
    thread.start()
    thread.join(timeout=timeout_seconds)

    if thread.is_alive():
        # Thread is still running - timeout occurred
        raise SolverTimeoutError(f"Preprocessing timed out after {timeout_seconds} seconds")

    if exception_container:
        raise exception_container[0]

    return result_container[0] if result_container else None


def _solver_process_wrapper(conn, module_path, module_name, solver_name, args,
                            suppress_output=False):
    """Wrapper to run solver in a subprocess and send result back via pipe."""
    import os
    import traceback

    # if suppress_output:
    #     devnull_fd = os.open(os.devnull, os.O_WRONLY)
    #     os.dup2(devnull_fd, 1)  # Redirect fd 1 (stdout) to /dev/null
    #     os.dup2(devnull_fd, 2)  # Redirect fd 2 (stderr) to /dev/null
    #     os.close(devnull_fd)

    try:
        # Add module path and import the module in the subprocess
        if module_path not in sys.path:
            sys.path.insert(0, module_path)
        day_module = __import__(module_name)
        solver_func = getattr(day_module, solver_name)

        # Always use context managers for output suppression at Python level too
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            if isinstance(args, tuple):
                result = solver_func(*args)
            else:
                result = solver_func(args)

        # Handle generators - send each yielded value as it arrives
        if hasattr(result, '__iter__') and not isinstance(result, (str, bytes, dict, tuple)):
            results = []
            try:
                for idx, item in enumerate(result):
                    results.append(item)
                    # Send each result immediately as it arrives
                    conn.send(('result', (idx, item)))
            except (OSError, StopIteration):
                conn.send(('error', traceback.format_exc()))
                return
            # Signal completion
            conn.send(('done', tuple(results)))
        else:
            # Non-generator result
            if isinstance(result, tuple):
                conn.send(('done', result))
            else:
                conn.send(('done', (result,)))
    except (OSError, ImportError, AttributeError):
        conn.send(('error', traceback.format_exc()))
    finally:
        conn.close()


def run_solver_with_timeout(module_path, module_name, solver_name, args,
                            timeout_seconds, suppress_output=False):
    """
    Run solver function with timeout using multiprocessing.

    Args:
        module_path: Path to module directory
        module_name: Name of module to import (e.g., 'day_15')
        solver_name: Name of solver function (usually 'solver')
        args: Arguments to pass to solver
        timeout_seconds: Timeout in seconds
        suppress_output: Whether to suppress stdout/stderr
        memory_limit_mb: Memory limit in MB (0 = unlimited)

    Returns:
        Tuple of (completed, result, intermediate_results)
        - completed: True if solver finished, False if timed out
        - result: Final result tuple
        - intermediate_results: List of (part_index, result) tuples for partial results
    """
    parent_conn, child_conn = multiprocessing.Pipe()
    process = multiprocessing.Process(
        target=_solver_process_wrapper,
        args=(child_conn, module_path, module_name, solver_name, args),
        kwargs={'suppress_output': suppress_output}
    )
    process.daemon = False
    process.start()

    start_time = datetime.datetime.now()
    partial_results = {}
    intermediate_results = []  # Track results as they arrive
    done = False
    final_results = None

    # Listen for results as they arrive, with timeout
    while True:
        elapsed = (datetime.datetime.now() - start_time).total_seconds()
        remaining_timeout = max(0.01, timeout_seconds - elapsed)

        # Check timeout FIRST - if exceeded, kill process immediately
        if elapsed > timeout_seconds:
            if process.is_alive():
                # Be aggressive: kill directly without terminate first
                process.kill()
                process.join(timeout=0.2)
            parent_conn.close()
            # Return timeout with partial results if any
            if partial_results:
                sorted_results = tuple(
                    partial_results[i] for i in sorted(partial_results.keys())
                )
                return (False, sorted_results, intermediate_results)
            else:
                return (False, None, intermediate_results)

        if not process.is_alive():
            # Process finished, collect any remaining messages
            while parent_conn.poll(timeout=0.01):
                try:
                    status, data = parent_conn.recv()
                    if status == 'result':
                        idx, result = data
                        partial_results[idx] = result
                        intermediate_results.append((idx, result))
                        # Display immediately as result arrives
                        print(f"  {'🥇' if idx == 0 else '🥈'} Part {idx + 1}: {result}")
                    elif status == 'done':
                        final_results = data
                        done = True
                        break
                    elif status == 'error':
                        parent_conn.close()
                        raise RuntimeError(f"Solver error: {data}")
                except EOFError:
                    done = True
                    break

            if done:
                parent_conn.close()
                if final_results:
                    return (True, final_results, intermediate_results)
                elif partial_results:
                    sorted_results = tuple(
                        partial_results[i] for i in sorted(partial_results.keys())
                    )
                    return (True, sorted_results, intermediate_results)
                else:
                    return (True, None, intermediate_results)
            else:
                parent_conn.close()
                if partial_results:
                    sorted_results = tuple(
                        partial_results[i] for i in sorted(partial_results.keys())
                    )
                    return (True, sorted_results, intermediate_results)
                else:
                    return (True, None, intermediate_results)

        # Poll for messages with remaining timeout
        if parent_conn.poll(timeout=remaining_timeout):
            try:
                status, data = parent_conn.recv()
                if status == 'result':
                    idx, result = data
                    partial_results[idx] = result
                    intermediate_results.append((idx, result))
                    # Don't display immediately - just collect for later display in Results section
                elif status == 'done':
                    final_results = data
                    done = True
                elif status == 'error':
                    parent_conn.close()
                    raise RuntimeError(f"Solver error: {data}")
            except EOFError:
                done = True

        # If we get here, ensure we return
        if done or not process.is_alive():
            parent_conn.close()
            if final_results:
                return (True, final_results, intermediate_results)
            elif partial_results:
                sorted_results = tuple(
                    partial_results[i] for i in sorted(partial_results.keys())
                )
                return (True, sorted_results, intermediate_results)
            else:
                return (True, None, intermediate_results)


def solve_day(puzzle: Puzzle, use_local_input: bool = True, preprocessing_func=None,
              suppress_solver_prints: bool = False, timeout_seconds: int = 60):
    """
    Solve an Advent of Code puzzle by importing the corresponding day module
    and running its solver.

    Args:
        puzzle: AOC Puzzle object containing year, day, and input data
        use_local_input: If True, attempts to use local input file first,
                        falls back to puzzle.input_data if file not found or empty
        preprocessing_func: Optional function to preprocess input data
        suppress_solver_prints: If True, suppresses all print output from
                               solver and preprocessing

    Examples:
        >>> puzzle = Puzzle(year=2022, day=15)
        >>> solve_day(puzzle)  # Loads day_01.py, calls solver(), submits answers

        >>> puzzle = Puzzle(year=2022, day=15, input_data="sensor data...")
        >>> solve_day(puzzle, use_local_input=False)  # Uses puzzle.input_data directly
    """
    # Start timing to include preprocessing in timeout calculation
    start_time = datetime.datetime.now()
    puzzle_input = None

    if use_local_input:
        try:
            day_str = str(puzzle.day).zfill(2)
            input_path = f"./events/year_{puzzle.year}/day_{day_str}/day_{day_str}.input"
            with open(input_path, encoding="utf-8") as data:
                file_content = data.read().rstrip('\n')
                if file_content:  # Only use local file if it has content
                    if preprocessing_func:
                        # Calculate remaining timeout for preprocessing
                        if timeout_seconds > 0:
                            elapsed = (datetime.datetime.now() - start_time).total_seconds()
                            remaining_preprocess_timeout = max(0.1, timeout_seconds - elapsed)
                        else:
                            remaining_preprocess_timeout = 60  # Large default if no timeout

                        if suppress_solver_prints:
                            stdout_redir = redirect_stdout(io.StringIO())
                            stderr_redir = redirect_stderr(io.StringIO())
                            with stdout_redir, stderr_redir:
                                puzzle_input = _preprocessing_wrapper(
                                    preprocessing_func, file_content,
                                    remaining_preprocess_timeout)
                        else:
                            puzzle_input = _preprocessing_wrapper(
                                preprocessing_func, file_content,
                                remaining_preprocess_timeout)
                    else:
                        puzzle_input = file_content
                    print(f"  📁 Using local input: {input_path}")

        except SolverTimeoutError as e:
            print(f"  ⏱️  Preprocessing timeout: {e}")
            # Return failure with timeout flag
            timeout_ret = (False, True, False, (), 0)
            return timeout_ret  # all_correct, timeout_occurred, has_answers,
            # parts_solved, num_parts

    if puzzle_input is None:
        # Try to save the input locally for future use
        day_str = str(puzzle.day).zfill(2)
        input_path = f"./events/year_{puzzle.year}/day_{day_str}/day_{day_str}.input"
        try:
            save_input_to_file(puzzle, verbose=False)
            print("  💾 Input auto-saved for future use")
            # Now read the locally saved file
            with open(input_path, encoding="utf-8") as data:
                file_data = data.read().rstrip('\n')
                if preprocessing_func:
                    # Calculate remaining timeout for preprocessing
                    if timeout_seconds > 0:
                        elapsed = (datetime.datetime.now() - start_time).total_seconds()
                        remaining_preprocess_timeout = max(0.1, timeout_seconds - elapsed)
                    else:
                        remaining_preprocess_timeout = 60  # Large default if no timeout

                    if suppress_solver_prints:
                        stdout_redir = redirect_stdout(io.StringIO())
                        stderr_redir = redirect_stderr(io.StringIO())
                        with stdout_redir, stderr_redir:
                            puzzle_input = _preprocessing_wrapper(
                                preprocessing_func, file_data,
                                remaining_preprocess_timeout)
                    else:
                        puzzle_input = _preprocessing_wrapper(
                            preprocessing_func, file_data,
                            remaining_preprocess_timeout)
                else:
                    puzzle_input = file_data
                print(f"  📁 Using auto-saved input: {input_path}")
        except (OSError, IOError):
            # Fallback to remote if saving fails
            if preprocessing_func:
                # Calculate remaining timeout for preprocessing
                if timeout_seconds > 0:
                    elapsed = (datetime.datetime.now() - start_time).total_seconds()
                    remaining_preprocess_timeout = max(0.1, timeout_seconds - elapsed)
                else:
                    remaining_preprocess_timeout = 60  # Large default if no timeout

                if suppress_solver_prints:
                    stdout_redir = redirect_stdout(io.StringIO())
                    stderr_redir = redirect_stderr(io.StringIO())
                    with stdout_redir, stderr_redir:
                        puzzle_input = _preprocessing_wrapper(
                            preprocessing_func, puzzle.input_data,
                            remaining_preprocess_timeout)
                else:
                    puzzle_input = _preprocessing_wrapper(
                        preprocessing_func, puzzle.input_data,
                        remaining_preprocess_timeout)
            else:
                puzzle_input = puzzle.input_data
            print("  🌐 Using remote input from AOC")
        except SolverTimeoutError as e:
            print(f"  ⏱️  Preprocessing timeout: {e}")
            # Return failure with timeout flag
            timeout_ret = (False, True, False, (), 0)
            return timeout_ret  # all_correct, timeout_occurred, has_answers,
            # parts_solved, num_parts

    # Add day directory to Python path to ensure we load the correct module
    # Use absolute path to work from any directory, resolving symlinks
    script_dir = Path(os.path.realpath(__file__)).parent
    day_path = str(script_dir / f"events/year_{puzzle.year}/day_{str(puzzle.day).zfill(2)}/")
    if day_path not in sys.path:
        sys.path.insert(0, day_path)

    day_module = __import__(f"day_{str(puzzle.day).zfill(2)}")
    if 'solver' in dir(day_module):
        try:
            answers = None
            timeout_occurred = False
            if timeout_seconds > 0:
                # Calculate remaining timeout after preprocessing
                elapsed = (datetime.datetime.now() - start_time).total_seconds()
                remaining_timeout = max(1, timeout_seconds - elapsed)

                completed, answers, _intermediate = run_solver_with_timeout(
                    day_path,
                    f"day_{str(puzzle.day).zfill(2)}",
                    'solver',
                    puzzle_input,
                    remaining_timeout,
                    suppress_output=suppress_solver_prints
                )

                if not completed:
                    # Timeout occurred
                    timeout_occurred = True
                    if answers is None:
                        # No partial results, use placeholder
                        answers = (-1,)
                    # If answers is not None, we have partial results - keep them as is
            else:
                if suppress_solver_prints:
                    with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                        if isinstance(puzzle_input, builtins.tuple):
                            answers = day_module.solver(*puzzle_input)
                        else:
                            answers = day_module.solver(puzzle_input)
                else:
                    if isinstance(puzzle_input, builtins.tuple):
                        answers = day_module.solver(*puzzle_input)
                    else:
                        answers = day_module.solver(puzzle_input)
        except SolverTimeoutError:
            timeout_occurred = True
            answers = (-1,)
        except Exception as solver_exc:  # pylint: disable=broad-except
            timeout_occurred = False  # Not a timeout, regular error
            exc_type = type(solver_exc).__name__
            exc_msg = str(solver_exc)[:80]
            print(f"  ⚠️  Solver error ({exc_type}): {exc_msg}")
            # For single day runs, show full traceback
            if suppress_solver_prints is False:
                print("\n  Full traceback:")
                traceback.print_exc()
            answers = (-1,)
    else:
        timeout_occurred = False
        answers = (-1,)

    # Display results with nice formatting
    # Pass timeout_occurred flag to show timeout message in results section
    if not answers or answers is None or answers == (-1,):
        # No valid answers - treat as failed
        print("📊 Results:")
        print("  ⚠️  No answers returned from solver")
        all_correct = False
        parts_solved_on_aoc = ()
        has_valid_answers = False
    elif timeout_occurred:
        timeout_kwarg = timeout_seconds
        all_correct, parts_solved_on_aoc = (
            parse_and_display_results(answers, puzzle, timeout_seconds=timeout_kwarg)
        )
        # Check if we have valid answers
        has_valid_answers = (
            answers != (-1,) and
            answers != () and
            answers is not None and
            not all(isinstance(a, tuple) and a[1] is None or a is None
                    for a in answers)
        )
    else:
        all_correct, parts_solved_on_aoc = parse_and_display_results(answers, puzzle)
        # Check if we have valid answers
        has_valid_answers = (
            answers != (-1,) and
            answers != () and
            answers is not None and
            not all(isinstance(a, tuple) and a[1] is None or a is None
                    for a in answers)
        )

    # Count the number of valid answers returned
    num_parts_returned = 0
    if has_valid_answers and answers:
        num_parts_returned = len(answers)

    return (all_correct, timeout_occurred, has_valid_answers,
            parts_solved_on_aoc, num_parts_returned)


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="🎄 Advent of Code puzzle runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  aocp 2024 1                    # Run day 1 of 2024
  aocp 2024 1 --examples         # Test examples first
  aocp 2024 1 --no-local         # Use remote input only
  aocp 2024 1 --save-input       # Save puzzle input to local file
  aocp 2024                      # Run all days of 2024
  aocp 2024 --days 1-5           # Run days 1 through 5
  aocp 2024 --days 1,3,5         # Run specific days
        """
    )

    parser.add_argument('year', type=int, help='Year (e.g., 2024)')

    parser.add_argument('day', type=int, nargs='?',
                        help='Day number (1-25). If omitted, runs all days.')

    parser.add_argument('--days', type=str,
                        help='Specify days to run: "1-5" for range or "1,3,5" '
                             'for specific days')

    parser.add_argument('-e', '--examples', action='store_true',
                        help='Test examples before running on real input')

    parser.add_argument('-ev', '--examples-verbose', action='store_true',
                        help='Test examples with verbose output')

    parser.add_argument('--no-local', action='store_true',
                        help='Skip local input files, use remote input only')
    parser.add_argument('--force', action='store_true',
                        help='Run on real input even if examples fail')

    parser.add_argument('--save-input', action='store_true',
                        help='Save puzzle input to local .input file')

    parser.add_argument('--extract-examples', action='store_true',
                        help='Extract and display examples from '
                             'puzzle description')

    parser.add_argument('--refresh-examples', action='store_true',
                        help='Force refresh examples (ignore cached '
                             '.examples files)')

    parser.add_argument('--timeout', type=int, default=60,
                        help='Timeout for solver execution in seconds '
                             '(0 = no timeout, default: 60)')

    parser.add_argument('-q', '--quiet', action='store_true',
                        help='Suppress verbose output, show only results table')

    # Enable argcomplete if available with custom completers
    # Note: Disabled to use bash completion for proper numeric day ordering
    # if ARGCOMPLETE_AVAILABLE and argcomplete:
    #     argcomplete.autocomplete(parser)
    return parser.parse_args()


def parse_days_string(days_str):
    """Parse days string like '1-5' or '1,3,5' into list of day numbers."""
    days = []

    for part in days_str.split(','):
        part = part.strip()
        if '-' in part:
            start, end = map(int, part.split('-'))
            days.extend(range(start, end + 1))
        else:
            days.append(int(part))

    return sorted(set(days))  # Remove duplicates and sort


def display_extracted_examples(puzzle: Puzzle, force_refresh: bool = False):
    """Display extracted examples from puzzle description."""
    print("📖 Extracting examples from puzzle description...")
    examples = extract_examples_from_puzzle(puzzle, force_refresh=force_refresh)
    if examples:
        print(f"  📋 Extracted {len(examples)} examples:")
        for i, example in enumerate(examples, 1):
            input_preview = example['input'][:50]
            has_more = '...' if len(example['input']) > 50 else ''
            print(f"    {i}. Input: {input_preview}{has_more}")
            if example.get('expected_a'):
                print(f"       Expected Part A: {example['expected_a']}")
            if example.get('expected_b'):
                print(f"       Expected Part B: {example['expected_b']}")
    else:
        print("  ❓ No examples extracted")


def run_day(year: int, day_number: int, parsed_args, suppress_solver_prints: bool = False,
            quiet: bool = False):
    """Run a specific day with given arguments."""
    day_str = str(day_number).zfill(2)
    if not quiet:
        print(f"\n🎄 Advent of Code - Year {year} - Day {day_str}")

    # Save input if requested
    if parsed_args.save_input:
        puzzle = Puzzle(year, day_number)
        if not save_input_to_file(puzzle, verbose=True):
            return (False, False, False, (), 0)
        print("  ✅ Input saved successfully")
        return (False, False, False, (), 0)

    # Add day directory to Python path
    # Use absolute path to work from any directory, resolving symlinks
    # Get project root (advents-of-code): aocp.py is in pythonfw/, so parent.parent
    aocp_file = Path(os.path.realpath(__file__))  # /pythonfw/aocp.py
    pythonfw_dir = aocp_file.parent  # /pythonfw
    project_root = pythonfw_dir.parent  # /advents-of-code
    day_path = str(project_root / f"events/year_{year}/day_{day_str}/")
    
    # Add project_root (parent of pythonfw) to path so day modules can import from pythonfw
    # This allows: from pythonfw.classes import X
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    if day_path not in sys.path:
        sys.path.insert(1, day_path)  # Insert after project root

    try:
        module = __import__(f"day_{day_str}")
    except ImportError as e:
        print(f"❌ Could not import day_{day_str}: {e}")
        return (False, False, False, (), 0)

    # Set up preprocessing function for solve_day to use
    if "preprocessing" in dir(module):
        preprocessing_func = module.preprocessing
    else:
        def _no_op(x):
            """Default preprocessing that returns input unchanged."""
            return x
        preprocessing_func = _no_op

    # Check if solver exists
    if 'solver' not in dir(module):
        print(f"❌ No solver function defined in day_{day_str}")
        return (False, False, False, (), 0)

    puzzle = Puzzle(year, day_number)

    # Extract examples if requested
    if parsed_args.extract_examples or parsed_args.refresh_examples:
        display_extracted_examples(puzzle, force_refresh=parsed_args.refresh_examples)

    # Handle examples
    if parsed_args.examples or parsed_args.examples_verbose:
        print("🧪 Testing examples...")
        success = solve_examples(puzzle, parsed_args.examples_verbose)

        if success:
            print("✅ All examples passed!")
        else:
            print("❌ Some examples failed!")
            if not parsed_args.force:
                user_input = input("Continue with real input anyway? (y/N): ")
                if user_input.lower() not in ['y', 'yes']:
                    return (False, False, False, (), 0)

    # Run on real input
    print("🚀 Running on real input...")
    timeout_display = (
        "disabled" if parsed_args.timeout == 0
        else f"{parsed_args.timeout} second{'s' if parsed_args.timeout != 1 else ''}"
    )
    if not quiet:
        print(f"  ⏱️  Timeout set to {timeout_display}")
    result = solve_day(puzzle, use_local_input=not parsed_args.no_local,
                       preprocessing_func=preprocessing_func,
                       suppress_solver_prints=suppress_solver_prints or quiet,
                       timeout_seconds=parsed_args.timeout)
    # result is a 5-tuple: (all_correct, timeout_occurred, has_answers,
    # parts_solved_on_aoc, num_parts_returned)
    (all_correct, timeout_occurred, has_answers,
     parts_solved_on_aoc, num_parts_returned) = result
    return (all_correct, timeout_occurred, has_answers, parts_solved_on_aoc,
            num_parts_returned)


def display_scoreboard(year: int, days_to_run: list, day_results: dict):
    """Display a formatted scoreboard of all days."""
    # Don't display if no results yet
    if not day_results:
        return
    
    total_days = len(days_to_run)
    successful_days = sum(
        1 for d in days_to_run
        if day_results.get(d, {}).get('success', False)
    )

    # Check if we're running the full year (all 25 days)
    is_full_year = len(days_to_run) == 25 and all(d in days_to_run for d in range(1, 26))

    # Check if all days 1-24 are complete
    days_1_24_complete = all(
        day_results.get(d, {}).get('success', False) for d in range(1, 25)
    ) if is_full_year else False

    # Build two-column table-style scoreboard
    print(f"\n{'='*70}")
    print(f"🏆 Scoreboard - Advent of Code {year}")
    print(f"{'='*70}")
    print(f"{'Day':<6} {'Status':<17} {'Notes':<6}  │  {'Day':<6} {'Status':<17} {'Notes':<6}")
    print(f"{'-'*70}")
    
    # Build rows with two columns
    for i in range(0, len(days_to_run), 2):
        # First column
        day_num = days_to_run[i]
        result_info = day_results.get(day_num, {})
        success = result_info.get('success', False)
        notes = result_info.get('notes', '')
        
        # Determine status for first column
        if day_num not in day_results:
            # Day not run yet
            status_emoji = ""
            status_text = ""
            stars = ""
        elif day_num == 25 and success:
            part2_unlocked = is_full_year and days_1_24_complete
            status_emoji = "✅"
            status_text = "Complete"
            stars = "⭐" if not part2_unlocked else "⭐⭐"
        elif success:
            status_emoji = "✅"
            status_text = "Complete"
            stars = "⭐⭐"
        elif "Incomplete" in notes:
            status_emoji = "🚧"
            status_text = "Incomplete"
            stars = "⭐"
        elif "Timeout" in notes:
            status_emoji = "⏱️"
            status_text = "Timed out"
            stars = ""
        else:
            status_emoji = "❌"
            status_text = "Failed"
            stars = ""
        
        day_str = str(day_num).zfill(2)
        status_display = f"{status_emoji} {status_text}"
        left_col = f"{day_str:<6} {status_display:<17} {stars:<6}"
        
        # Second column (if exists)
        if i + 1 < len(days_to_run):
            day_num = days_to_run[i + 1]
            result_info = day_results.get(day_num, {})
            success = result_info.get('success', False)
            notes = result_info.get('notes', '')
            
            # Determine status for second column
            if day_num not in day_results:
                # Day not run yet
                status_emoji = ""
                status_text = ""
                stars = ""
            elif day_num == 25 and success:
                part2_unlocked = is_full_year and days_1_24_complete
                status_emoji = "✅"
                status_text = "Complete"
                stars = "⭐" if not part2_unlocked else "⭐⭐"
            elif success:
                status_emoji = "✅"
                status_text = "Complete"
                stars = "⭐⭐"
            elif "Incomplete" in notes:
                status_emoji = "🚧"
                status_text = "Incomplete"
                stars = "⭐"
            elif "Timeout" in notes:
                status_emoji = "⏱️"
                status_text = "Timed out"
                stars = ""
            else:
                status_emoji = "❌"
                status_text = "Failed"
                stars = ""
            
            day_str = str(day_num).zfill(2)
            status_display = f"{status_emoji} {status_text}"
            right_col = f"{day_str:<6} {status_display:<17} {stars:<6}"
            
            print(f"{left_col}  │  {right_col}")
        else:
            print(f"{left_col}")
    
    print(f"{'='*70}")

    # Count stars
    star_count = 0
    for d in days_to_run:
        if d == 25:
            day_25_info = day_results.get(25, {})
            day_25_success = day_25_info.get('success', False)
            day_25_incomplete = 'Incomplete' in day_25_info.get('notes', '')

            if day_25_success:
                star_count += 2 if (is_full_year and days_1_24_complete) else 1
            elif day_25_incomplete:
                star_count += 1
        else:
            if day_results.get(d, {}).get('success', False):
                star_count += 2
            elif 'Incomplete' in day_results.get(d, {}).get('notes', ''):
                star_count += 1

    percentage = 100 * successful_days // total_days if total_days > 0 else 0
    print(f"  {successful_days}/{total_days} days completed │ {star_count} ⭐ ({percentage}%)\n")


# Global preprocessing function placeholder
def _default_preprocessing(x):
    """Default preprocessing that returns input unchanged."""
    return x


pp = _default_preprocessing


def main():
    """Main entry point for aocp"""
    args = parse_arguments()

    # Determine which days to run
    days_to_run = []

    if args.day is not None:
        days_to_run = [args.day]
    elif args.days:
        try:
            days_to_run = parse_days_string(args.days)
        except ValueError as e:
            print(f"❌ Invalid days format: {e}")
            sys.exit(1)
    else:
        # Run all days (1-25)
        days_to_run = list(range(1, 26))

    # Validate days
    invalid_days = [d for d in days_to_run if d < 1 or d > 25]
    if invalid_days:
        print(f"❌ Invalid day numbers: {invalid_days} (must be 1-25)")
        sys.exit(1)

    print(f"🎯 Running {len(days_to_run)} day(s) for year {args.year}")
    if len(days_to_run) > 1:
        print(f"📅 Days: {', '.join(map(str, days_to_run))}")

    # Run each day
    success_count = 0
    suppress_prints = len(days_to_run) > 1
    day_results = {}  # Track results for scoreboard

    for day_num in days_to_run:
        try:
            # In quiet mode, suppress stdout from solve_day
            if args.quiet:
                with redirect_stdout(io.StringIO()):
                    result = run_day(args.year, day_num, args,
                                     suppress_solver_prints=suppress_prints,
                                     quiet=args.quiet)
            else:
                result = run_day(args.year, day_num, args,
                                 suppress_solver_prints=suppress_prints,
                                 quiet=args.quiet)
            (all_correct, timeout_occurred, has_answers, parts_solved_on_aoc,
             num_parts_returned) = result

            if all_correct and not timeout_occurred:
                # Check if both parts were returned (day has 2 parts)
                # Special case: Day 25 only has 1 part, so it's complete if
                # num_parts_returned >= 1
                if day_num == 25:
                    if num_parts_returned >= 1:
                        success_count += 1
                        day_results[day_num] = {
                            'success': True,
                            'result': '✅',
                            'notes': '⭐'
                        }
                    else:
                        day_results[day_num] = {
                            'success': False,
                            'result': '🚧',
                            'notes': 'Incomplete'
                        }
                elif num_parts_returned < 2:
                    # Only one part returned when two are available -
                    # mark as incomplete
                    day_results[day_num] = {
                        'success': False,
                        'result': '🚧',
                        'notes': 'Incomplete'
                    }
                else:
                    success_count += 1
                    day_results[day_num] = {'success': True, 'result': '✅', 'notes': '⭐⭐'}
            elif timeout_occurred:
                day_results[day_num] = {
                    'success': False,
                    'result': '⏱️',
                    'notes': ' Timeout'
                }
            elif parts_solved_on_aoc == (1,) and not has_answers:
                # Only part 1 solved on AOC and no valid solver answers - show as incomplete
                day_results[day_num] = {'success': False, 'result': '🚧', 'notes': 'Incomplete'}
            elif has_answers and not all_correct:
                # Solver ran and returned answers, but not all are correct - Failed
                day_results[day_num] = {'success': False, 'result': '❌', 'notes': 'Failed'}
            else:
                # Solver didn't run or had an error
                day_results[day_num] = {'success': False, 'result': '❌', 'notes': 'Failed'}
            
            # Display scoreboard after each day in quiet mode (progressive updates)
            if args.quiet and len(days_to_run) > 1 and day_results:
                # Use a simple redraw without ANSI codes - just print fresh table
                print("\033[H\033[J", end='', flush=True)  # Clear screen
                display_scoreboard(args.year, days_to_run, day_results)
                sys.stdout.flush()
                
        except KeyboardInterrupt:
            print("\n⏹️ Interrupted by user")
            break
        except Exception as exc:  # pylint: disable=broad-except
            exc_type = type(exc).__name__
            exc_msg = str(exc)[:100]  # Truncate long error messages
            print(f"❌ Error running day {day_num} ({exc_type}): {exc_msg}")
            day_results[day_num] = {
                'success': False,
                'result': '❌',
                'notes': f'Error: {exc_type}'
            }

    # Display scoreboard based on mode
    # In quiet mode with multiple days: show only scoreboard
    # In normal mode: show scoreboard after verbose output
    if len(days_to_run) > 1:
        display_scoreboard(args.year, days_to_run, day_results)

    print(f"🏁 Completed {success_count}/{len(days_to_run)} days successfully")
    sys.stdout.flush()
    sys.stderr.flush()
    # Exit immediately without waiting for child processes
    os._exit(0)


if __name__ == '__main__':
    main()
