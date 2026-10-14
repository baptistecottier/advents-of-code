# Python

Code shared by the Python solutions, and the benchmark behind the [scoreboard](../README.md#scoreboard).

## Solutions

Each day is `events/year_YYYY/day_DD/day_DD.py`, run and submitted with
[Puzzle Submitter](https://github.com/baptistecottier/puzzle-submitter-vscode):

```python
def preprocessing(puzzle_input: str):  # optional, parses the raw input
    ...


def solver(data):                      # returns, or yields, the answer of each part
    yield part_1
    yield part_2
```

When `preprocessing` returns a tuple, it is unpacked: `solver(*data)`.
Helpers shared between days live in `functions.py` and `classes.py`.

## Benchmark

```bash
python pythonfw/benchmark.py                   # every year, Python and Rust
python pythonfw/benchmark.py 2024 --days 1-5   # some days only
python pythonfw/benchmark.py --lang python     # one language
python pythonfw/benchmark.py --changed         # only what changed since its last run
python pythonfw/benchmark.py --render          # redraw from events/benchmarks.json
```

Each day runs in its own process with a 5 minute timeout; the time covers preprocessing
and solving. Answers are checked against the ones Puzzle Submitter recorded as correct.
Results are stored in `events/benchmarks.json`, from which `scoreboard.py` writes the
homepage scoreboard and the year pages.
