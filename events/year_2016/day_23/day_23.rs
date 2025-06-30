aoc::main!(); 

fn preprocessing(input: &str) -> i32 {
    input
    .lines()
    .skip(19)
    .take(2)
    .map(|l| l.split(' ').nth(1).unwrap())
    .map(|n| n.parse::<i32>().unwrap())
    .product()
}

fn part_1(instructions: i32) -> i32 {
    (1 .. 8).product::<i32>() + instructions
}

fn part_2(instructions: i32) -> i32 {
    (1 .. 13).product::<i32>() + instructions
}

