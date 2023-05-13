aoc2016::main!();

fn generator(input: &str) -> usize {
    input.parse().unwrap()
}

fn part_1(input: usize) -> usize {
    1 + 2 * solver(input, 2)
}

fn part_2(input: usize) -> usize {
    solver(input, 3)
}
fn solver(players: usize, step: usize) -> usize {
    let logn = (players as f64).log(step as f64) as u32;
    players % (step.pow(logn) as usize)
}