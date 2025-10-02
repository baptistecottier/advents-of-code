aoc::main!();

fn preprocessing(puzzle_input: &str) -> Vec<isize> {
    puzzle_input
        .split(',')
        .scan((0, 0), |(x, y), dir| {
            match dir {
                "n" => *y += 1,
                "s" => *y -= 1,
                "nw" => *x -= 1,
                "se" => *x += 1,
                "ne" => (*x, *y) = (*x + 1, *y + 1),
                "sw" => (*x, *y) = (*x - 1, *y - 1),
                _ => unreachable!(),
            };
            Some((*x, *y))
        })
        .map(|(x, y): (isize, isize)| x.abs() + y.abs())
        .collect_vec()
}

fn part_1(distances: Vec<isize>) -> isize {
    *distances.last().unwrap()
}

fn part_2(distances: Vec<isize>) -> isize {
    *distances.iter().max().unwrap()
}
