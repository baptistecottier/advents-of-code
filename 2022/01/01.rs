aoc::main!();

fn preprocessing(input: &str) -> Vec<Vec<u32>>{
    input
        .split("\n\n")
        .map(|r| r.lines().map(|cal| cal.parse().unwrap()).collect())
        .collect()
}

fn part_1(input: Vec<Vec<u32>>) -> u32 {
    solver(input, 1)
}

fn part_2(input: Vec<Vec<u32>>) -> u32 {
    solver(input, 3)   
}

fn solver(input: Vec<Vec<u32>>, n: usize) -> u32 {
    input
    .iter()
    .map(|r| r.iter().sum::<u32>())
    .sorted_by(|a,b| b.cmp(a))
    .take(n)
    .sum() 
}