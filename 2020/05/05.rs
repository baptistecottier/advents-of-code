aoc::main!();

fn preprocessing(input: &str) -> Vec<usize> {
    input
    .lines()
    .map(|bp| bp.replace('B', "1").replace('F', "0").replace('R', "1").replace('L', "0"))
    .map(|bp| 
        8 * usize::from_str_radix(&bp[..7], 2).unwrap()
        +   usize::from_str_radix(&bp[7..], 2).unwrap())
    .sorted()
    .collect_vec()
}

fn part_1(boarding_passes: Vec<usize>) -> usize {
    boarding_passes[boarding_passes.len() - 1]
}

fn part_2(boarding_passes: Vec<usize>) -> usize {
    *boarding_passes
    .iter()
    .enumerate()
    .find(|(n, b)| (n + boarding_passes[0]) != **b)
    .unwrap()
    .1
    - 1
}