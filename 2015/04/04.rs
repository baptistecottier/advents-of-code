aoc::main!();

fn preprocessing(input: &str) -> &str {
    input
}

fn part_1(target : &str) -> usize {
    get_adventcoin(target, 5)
}

fn part_2(target : &str) -> usize {
    get_adventcoin(target, 6)
}

fn get_adventcoin(target : &str, length: usize) -> usize {
    (1..)
    .find(|n| &format!("{:x}", md5::compute(format!("{}{}", target, n)))[..length] == "0".repeat(length))
    .unwrap()
}