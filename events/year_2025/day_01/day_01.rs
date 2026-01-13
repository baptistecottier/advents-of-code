aoc::main!();

fn preprocessing(puzzle_input: &str) -> Vec<isize> {
    puzzle_input
    .lines()
    .map(|line| {
        let (first, rest) = line.split_at(1);
        let num: isize = rest.parse().unwrap_or(0);
        if first == "L" {
            -num
        } else {
            num
        }})
    .collect_vec()
}

fn part_1(clicks: Vec<isize>) -> u16 {
    clicks
    .into_iter()
    .scan(50, |state, n| {
        *state = (*state + n) % 100;
        Some((*state == 0) as u16)
    })
    .sum()
}

fn part_2(clicks: Vec<isize>) -> isize {
    clicks
    .into_iter()
    .scan(50, |state, n| {
        if *state == 0 && n < 0 {
            *state = 100 + n
        } else {
            *state = *state % 100 + n;
        }
        Some(*state)
    })
    .map(|state| if state < 0 {
        1 + (state / 100).abs()
    } else {
        (state / 100).abs()
    })
    .sum::<isize>() + (1074 as isize)
}