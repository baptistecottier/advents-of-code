aoc2021::main!();

fn generator(input: &str) -> Vec<(i32, i32)> {
    input
    .lines()
    .map(|command| command
        .splitn(2,' ')
        .collect_tuple()
        .unwrap())
    .map(|(dir, steps)| match dir {
        "forward"   => (steps.parse().unwrap(), 0),
        "down"      => (0, steps.parse().unwrap()),
        "up"        => (0, -steps.parse::<i32>().unwrap()),
        _ => unreachable!()})
    .collect_vec()   
}

fn part_1(input: Vec<(i32, i32)>) -> i32 {
    solver(input, false)
}

fn part_2(input: Vec<(i32, i32)>) -> i32 {
    solver(input, true)
}

fn solver(commands: Vec<(i32, i32)>, track_aim: bool) -> i32 {
    let (a, b, _) = commands
    .iter()
    .fold((0,0,0), |(x, y, aim), (dx, dy)| {
    if track_aim {(x + dx, y + dx * aim, aim + dy)}
    else {(x + dx, y + dy, 0)}});
    a * b
}