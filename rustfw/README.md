# Rust

Each day is `events/year_YYYY/day_DD/day_DD.rs`, a binary of this crate named `YYYY-DD`.
The `aoc::main!()` macro of `src/lib.rs` reads the day's input, then prints
`(part_1(input.clone()), part_2(input))`:

```rust
aoc::main!();

fn preprocessing(puzzle_input: &str) -> Vec<i32> { ... }

fn part_1(data: Vec<i32>) -> i32 { ... }

fn part_2(data: Vec<i32>) -> usize { ... }
```

Run a day from this folder, with its input in `events/year_2015/day_01/day_01.input`:

```bash
cargo run --release --bin 2015-01
```

Results are on the [scoreboard](../README.md#scoreboard): `python pythonfw/benchmark.py --lang rust`
builds every solution in release mode and runs it.
