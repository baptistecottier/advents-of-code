aoc2017::main!();

fn generator(input : &str) -> Vec<u32> {
    input
        .chars()
        .map(|digit| digit.to_digit(10).unwrap()) 
        .collect_vec()
}

fn part_1(input : Vec<u32>) -> u32 {
    solver(input, 1)

}

fn part_2(input : Vec<u32>) -> u32 {
    solver(input.clone(), input.len()/2)
}

fn solver(input : Vec<u32>, shift : usize) -> u32 {
    input
    .iter()
    .enumerate()
    .filter(|(pos, digit)| *digit == input.iter().nth((pos + shift) % input.len()).unwrap())
    .fold(0, |acc, digit| acc + digit.1)
}