"""
Test day for infinite loop timeout testing
"""

def preprocessing(puzzle_input: str) -> str:
    return puzzle_input.strip()

def solver(data: str) -> tuple[int, int]:
    """
    Solver with an intentional infinite loop for timeout testing.
    """
    print("  🔄 Starting infinite loop...")
    counter = 0
    while True:
        counter += 1
        # Do some work to make sure it's actually running
        if counter % 1000000 == 0:
            print(f"    Still running... {counter//1000000}M iterations")