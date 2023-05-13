aoc2017::main!();

fn generator(input: &str) -> Vec<u32> {
    input.chars().map(|n| n.to_digit(10).unwrap()).collect_vec()
}

fn part_1(input: Vec<u32>) -> u32 {
    solver(input, 1)

}

fn part_2(input: Vec<u32>) -> u32 {
    solver(input.clone(), input.len()/2)
}

fn solver(input: Vec<u32>, shift: usize) -> u32 {
    let l = input.len() ;
    (0..l)
        .filter(|&i| input[i] == input[(i + shift) % l])
        .fold(0, |acc, i| acc + input[i])
}