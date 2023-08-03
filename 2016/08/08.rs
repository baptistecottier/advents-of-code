aoc::main!();

fn parser(input: &str) -> Vec<(usize, usize, usize)> {
    input
    .lines()
    .map(|l| l.split([' ','=','x']).collect_vec())
    .map(|l| 
        match l.len() {
            3 => (0, l[1].parse::<usize>().unwrap(), l[2].parse::<usize>().unwrap()),
            6 => (1, l[3].parse::<usize>().unwrap(), l[5].parse::<usize>().unwrap()),
            7 => (2, l[4].parse::<usize>().unwrap(), l[6].parse::<usize>().unwrap()),
            _ => unreachable!()})
    .collect_vec()
}

fn part_1(instructions: Vec<(usize, usize, usize)>) -> usize {
    solver(instructions).len()
}

fn part_2(instructions: Vec<(usize, usize, usize)>) -> String {
    screen_reader(solver(instructions))
}


fn solver(instructions: Vec<(usize, usize, usize)>) -> HashSet<(usize, usize)> {
    instructions
    .iter()
    .fold(HashSet::<(usize, usize)>::new(), |mut acc, (op, a, b)| {
        match op {
            0 => {
                iproduct!(0..*a,0..*b).for_each(|(x, y)| {acc.insert((x, y));});
                acc},
            1 => acc.into_iter().map(|(x, y)| if y == *a {((x + b) % 50, y)} else {(x, y)}).collect(),
            2 => acc.into_iter().map(|(x, y)| if x == *a {(x, (y + b) % 6)} else {(x, y)}).collect(),
            _ => unreachable!()}})
}