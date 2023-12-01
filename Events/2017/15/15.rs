aoc::main!();

fn preprocessing(input_: &str) -> (i64, i64) {
    input_
    .lines()
    .map(|generator| 
        generator
        .rsplit_once(' ')
        .unwrap()
        .1
        .parse()
        .unwrap())
    .collect_tuple()
    .unwrap()
}

fn part_1((gen_a, gen_b): (i64, i64)) -> usize {
    successors(Some((gen_a, gen_b)), |(a, b)|
        Some(((a * 16_807) % 2_147_483_647 , (b * 48_271) % 2_147_483_647)))
    .take(40_000_000)
    .filter(|(a, b)| (a - b) & 0xFFFF == 0)
    .count()
}

fn part_2((gen_a, gen_b): (i64, i64)) -> usize {
    zip(
        successors(Some(gen_a), |a| Some((a * 16_807) % 2_147_483_647))
        .filter(|a| a % 4 == 0)
    , 
        successors(Some(gen_b), |b| Some((b * 48_271) % 2_147_483_647))
        .filter(|b| b % 8 == 0)
    )
    .take(5_000_000)
    .filter(|(a, b)| (a - b) & 0xFFFF == 0)
    .count()
}