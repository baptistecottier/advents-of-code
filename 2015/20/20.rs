aoc::main!();

fn preprocessing(input: &str) -> usize {
    input.parse().unwrap()
}

fn part_1(target : usize) -> usize {
    (1..1000000)
    .find_or_last(|i| 10 * sum_divisors(*i, false) >= target)
    .unwrap()
}

fn part_2(target : usize) -> usize {
    (1..1000000)
    .find_or_first(|i| 11 * sum_divisors(*i, true) >= target)
    .unwrap()
}

fn sum_divisors(target : usize, lazy_elves : bool) -> usize {
    (1.. ((target) as f32).sqrt() as usize + 1 )
    .fold(0, |acc, d| 
        if target % d == 0  { 
            match lazy_elves {
                false => 
                    if d * d == target {acc + d} else {acc + target / d + d},
                true => 
                    if target / d > 50 {
                        if d <= 50 { acc + target / d } else {acc}} else {
                        if d * d == target { acc + d } else {acc + target / d + d}}}}
        else {acc})
}