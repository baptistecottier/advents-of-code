aoc::main!(); 

fn preprocessing(input_: &str) -> HashMap<(u16, Vec<u16>)> {
    input_
    .lines()
    .map(|pipe| 
        pipe
        .split(" <-> ")
        .collect_tuple()
        .unwrap())
    .map(|(left, right)| 
        (left.parse::<u16>().unwrap(),
        right
        .split(", ")
        .map(|n| n.parse::<u16>().unwrap())
        .collect_vec()))
    .collect_vec()
    .iter()
    .fold(HashMap::<u16, Vec<u16>>::new(), |pipes, (&left, &right)|
        pipes.insert(left, right))
}

fn part_1(pipes: HashMap<(u16, Vec<u16>)>) -> usize {
    pipes
    .iter()
    .for_each(|&(left, right)|
        if right.

}