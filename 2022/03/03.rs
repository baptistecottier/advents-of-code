aoc2022::main!();

fn generator(input : &str) -> Vec<&str> {
    input.lines().collect()
}

fn part_1(input : Vec<&str>) -> usize {
    solver(input, 1)
}

fn part_2(input : Vec<&str>) -> usize {
    solver(input, 3)
}

fn solver(input : Vec<&str>, size :usize) -> usize {
    input
    .chunks(size)
    .map(|l| 
            l[0].chars().take(l[0].len()/(1 + size % 3)).find(
                |c| 
                (0 .. size).all(
                    |i|
                    l[i].chars().skip((size % 3)*l[0].len()/2).contains(c))
            ).unwrap()
        )
    .map(|c| c as usize - 38 - (c.is_lowercase() as usize) * 58)
    .sum()
}
