aoc_2015::main!();

fn generator(input : &str) -> usize {
    input.parse().unwrap()
}

fn part_1(input : usize) -> usize {
    (1..1000000)
        .find_or_last(|i| 10 * sum_divisors(*i, false) >= input)
        .unwrap()
}

fn part_2(input : usize) -> usize {
    (1..1000000)
        .find_or_first(|i| 11 * sum_divisors(*i, true) >= input)
        .unwrap()
}

fn sum_divisors(input : usize, lazy_elves : bool) -> usize {
    (1.. ((input) as f32).sqrt() as usize + 1 )
        .fold(0, |acc, d| if input % d == 0  { match lazy_elves {
            false => if d * d == input {acc + d} else {acc + input / d + d},
            true => if input / d > 50 {
                if d <= 50 { acc + input / d } else {acc}} else {
                if d * d == input { acc + d } else {acc + input / d + d}
            }
        }}
        else {acc})
}