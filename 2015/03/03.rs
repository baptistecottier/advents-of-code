aoc::main!();

fn preprocessing(input: &str) -> Vec<(i32, i32)> {
    input
    .chars()
    .map(|s| 
        match s {
            '^' => (0 , 1 ),
            'v' => (0 , -1),
            '>' => (1 , 0 ),
            '<' => (-1, 0 ),
            _ => unreachable!(),})
    .collect()
}

fn part_1(instructions: Vec<(i32, i32)>) -> usize {
    instructions
    .iter()
    .scan((0,0), |pos, i| {
        pos.0 += i.0 ;
        pos.1 += i.1 ;
        Some((pos.0, pos.1))})
    .unique()
    .count()
    +1
}

fn part_2(instructions: Vec<(i32, i32)>) -> usize {
    instructions
    .iter()
    .step_by(2)
    .scan((0,0), |pos, i| {
        pos.0 += i.0 ;
        pos.1 += i.1 ;
        Some((pos.0, pos.1))})
    .chain(
        instructions
        .iter()
        .skip(1)
        .step_by(2)
        .scan((0,0), |pos, i| {
            pos.0 += i.0 ;
            pos.1 += i.1 ;
            Some((pos.0, pos.1))}))
    .unique()
    .count()
}
