aoc::main!();

fn preprocessing(input: &str) -> (u64, u64) {
    input.split([',',' ','.']).filter_map(|n| n.parse().ok()).collect_tuple().unwrap()
}

fn part_1(coord :(u64, u64)) -> u64 {
    20151125 * mod_exp(252533, (coord.0 + coord.1)*(coord.0 + coord.1 - 1) / 2 - coord.0, 33554393) % 33554393
}

fn part_2(_coord : (u64, u64)) -> String {
    "Merry XMAS".to_string()
}