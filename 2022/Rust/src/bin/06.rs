aoc2022::main!();

fn generator(input : &str) -> &str {
    input
}

fn part_1(input : &str) -> usize {
    solver(input, 4)
}

fn part_2(input : &str) -> usize {
   solver(input, 14)
}

fn solver(input : &str, size: usize)  -> usize {
    (0.. input.len())
        .find_or_last(|n| 
            input
                .chars()
                .skip(*n)
                .take(size)
                .all_unique())
                .unwrap() 
    + size
}