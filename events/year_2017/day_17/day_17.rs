aoc::main!();

fn preprocessing(puzzle_input: &str) -> usize {
    puzzle_input
    .parse()
    .unwrap()
}

fn part_1(steps: usize) -> usize {
    *(0..=2017)
    .fold((0, vec![0]), |(mut pos, mut state), entry| {
        pos = 1 + (pos + steps) % (entry + 1);
        state.insert(pos, entry + 1);
        (pos, state)})
    .1
    .iter()
    .skip_while(|n| **n != 2017)
    .nth(1)
    .unwrap()}

fn part_2(steps: usize) -> usize {
    (0..=50_000_000)
    .fold((0, 0), |(value, pos), entry| 
        (
            if pos == 1 {entry} else {value}
        ,
            1 + (pos + steps) % (entry + 1)
        ))
    .0
}