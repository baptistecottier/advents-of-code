aoc2022::main!();

fn generator(input : &str) -> Vec<Vec<u32>>{
    input
        .split("\n\n")
        .map(|r| r.lines().map(|cal| cal.parse().unwrap()).collect())
        .collect()
}

fn part_1(input : Vec<Vec<u32>>) -> u32 {
    input
        .iter()
        .map(|r| r.iter().sum::<u32>())
        .max()
        .unwrap()
}

fn part_2(input : Vec<Vec<u32>>) -> u32 {
    input
        .iter()
        .map(|r| r.iter().sum::<u32>())
        .sorted_by(|a,b| b.cmp(a))
        .take(3)
        .sum()    
}