aoc::main!();

fn preprocessing(input: &str) -> Vec<usize> {
    [2, 16, 17]
    .iter()
    .map(|&n| input.lines().nth(n).unwrap())
    .map(|l| l.split(' ').nth(1).unwrap().parse::<usize>().unwrap())
    .collect_vec()
}

fn part_1(program: Vec<usize>) -> usize {
    solver(program, 1)
}

fn part_2(program: Vec<usize>) -> usize {
    solver(program, 8)
}


fn solver(program: Vec<usize>, delta: usize) -> usize {
    (0..program[0] + delta)
    .fold((1,1), |acc, _| (acc.1, acc.0 + acc.1))
    .0
    + program[1] * program[2]
}