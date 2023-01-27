aoc2016::main!(); 
use md5;

fn generator(input : &str) -> &str {
    input
}

fn part_1(input : &str) -> String {
    (0..)
        .map(|index| format!("{:x}", md5::compute(format!("{}{}", input, index))))
        .filter(|hash| &hash[..5] == "00000")
        .take(8)
        .map(|hash| hash.as_bytes()[5] as char)
        .collect::<String>()
}

fn part_2(input : &str) -> String {
    (0..)
        .map(|index| format!("{:x}", md5::compute(format!("{}{}", input, index))))
        .filter(|hash| &hash[..5] == "00000" && (b'0'..b'8').contains(&hash.as_bytes()[5]))
        .map(|hash| (hash.as_bytes()[5],  hash.as_bytes()[6]))
        .unique_by(|n| n.0)
        .take(8)
        .sorted_by_key(|n| n.0)
        .map(|n| n.1 as char)
        .collect::<String>()
    }