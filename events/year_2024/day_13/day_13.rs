aoc::main!();

fn preprocessing(puzzle_input: &str) -> Vec<[f64; 6]> {
    puzzle_input
        .split("\n\n")
        .map(|machine| 
            Regex::new(r"([0-9]+)")
            .unwrap()
            .captures_iter(machine)
            .map(|draw| draw.extract())
            .map(|(_, [n])| n.parse::<f64>().unwrap())
            .collect_vec()
        .try_into().unwrap())
        .collect_vec()
}

fn part_1(machines: Vec<[f64; 6]>) -> u64 {
    get_minimum_cost(machines, 0.0)
    }

fn part_2(machines: Vec<[f64; 6]>) -> u64 {
    get_minimum_cost(machines, 10_000_000_000_000.)
    }

fn get_minimum_cost(machines: Vec<[f64; 6]>, delta: f64) -> u64 {
    machines
    .iter()
    .map(|m| 
        ((((delta + m[4]) * m[3]) - (m[2] * (delta + m[5]))) / ((m[0] * m[3]) - (m[2] * m[1])),
        ((m[0] * (delta + m[5])) - ((delta + m[4]) * m[1])) / ((m[0] * m[3]) - (m[2] * m[1]))))
    .filter(|(u, v)| u.fract() == 0. && v.fract() == 0. )
    .map(|(u, v)| (3. * u + v) as u64)
    .sum()
    }