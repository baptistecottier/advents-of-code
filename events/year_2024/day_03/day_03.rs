aoc::main!();

fn preprocessing(puzzle_input: &str) -> &str {
    puzzle_input
}

fn part_1(program: &str) -> u32 {
    scan_mul(program)
}

fn part_2(program: &str) -> u32 {
    scan_mul(
        Regex::new(r"don't\(\)([\s\S]*?)do\(\)")
            .unwrap()
            .replace_all(program, "")
            .split_once("don't()")
            .unwrap()
            .0,
    )
}

fn scan_mul(program: &str) -> u32 {
    Regex::new(r"mul\((\d{1,3}?),(\d{1,3}?)\)")
        .unwrap()
        .captures_iter(program)
        .map(|pair| pair.extract())
        .map(|(_, [a, b])| a.parse::<u32>().unwrap() * b.parse::<u32>().unwrap())
        .sum()
}
