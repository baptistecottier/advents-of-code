aoc::main!();

fn parser(input: &str) -> usize {
    input.parse().unwrap()
}

fn part_1(nb_players: usize) -> usize {
    1 + 2 * solver(nb_players, 2)
}

fn part_2(nb_players: usize) -> usize {
    solver(nb_players, 3)
}
fn solver(players: usize, step: usize) -> usize {
    let logn = (players as f64).log(step as f64) as u32;
    players % (step.pow(logn) as usize)
}