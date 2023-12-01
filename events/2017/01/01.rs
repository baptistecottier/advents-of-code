aoc::main!();

fn preprocessing(input_: &str) -> Vec<u32> {
    input_.chars().map(|n| n.to_digit(10).unwrap()).collect_vec()
}

fn part_1(captcha: Vec<u32>) -> u32 {
    solver(captcha, 1)
}

fn part_2(captcha: Vec<u32>) -> u32 {
    solver(captcha.clone(), captcha.len()/2)
}

fn solver(captcha: Vec<u32>, shift: usize) -> u32 {
    zip(captcha.clone(), [&captcha[shift..], &captcha[..shift + 1]].concat())
    .filter(|(a, b)| a == b)
    .map(|(a, _)| a)
    .sum()
}