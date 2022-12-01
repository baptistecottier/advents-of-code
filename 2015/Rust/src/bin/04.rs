aoc_2015::main!();

use md5;


fn generator(input : &str) -> &str {
    input
}

fn part_1(input : &str) -> usize {
    (1..)
        .find(|n|
                &format!("{:x}", md5::compute(format!("{}{}", input, n)))[..5] == "00000"
    )
        .unwrap()
}

fn part_2(input : &str) -> usize {
    (1..)
        .find(|n|
                &format!("{:x}", md5::compute(format!("{}{}", input, n)))[..6] == "000000"
    )
        .unwrap()
}