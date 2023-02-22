aoc2016::main!();

fn generator(input: &str) -> Vec<usize> {
    [2, 16, 17]
        .iter()
        .map(|&n| input.lines().nth(n).unwrap())
        .map(|l| l.split(' ').nth(1).unwrap().parse::<usize>().unwrap())
        .collect_vec()
}

fn part_1(input: Vec<usize>) -> usize {
    solver(input, 1)
}

fn part_2(input: Vec<usize>) -> usize {
    solver(input, 8)
}


fn solver(input: Vec<usize>, delta: usize) -> usize {
    (0..input[0] + delta)
        .fold((1,1), |acc, _| (acc.1, acc.0 + acc.1))
        .0
    + input[1] * input[2]
}