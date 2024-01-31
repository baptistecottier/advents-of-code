aoc::main!();

fn preprocessing(input: &str) -> Vec<(i32,i32)> {
    let mut dir = (1,0);
    let mut pos = (0,0);

    input
    .split(", ")
    .map(move |info| {
        let turn = info.chars().nth(0).unwrap() ;
        let l = info[1..].parse::<i32>().unwrap() ;
        match turn {
            'R' => dir = turn_right(dir),
            'L' => dir = turn_left(dir),
            _ => unreachable!()} ;
            (dir, l) })
    .map(|(dir, l)| {(1..l+1)
        .scan(pos, |_, _| {
            pos = (pos.0 + dir.0, pos.1 + dir.1);
            Some(pos)})
        .collect_vec()})
    .flatten()
    .collect_vec()
}

fn part_1(path: Vec<(i32,i32)>) -> i32 {
    path
    .iter()
    .last()
    .map(|d| d.0.abs() + d.1.abs())
    .unwrap()
}

fn part_2(path: Vec<(i32,i32)>) -> i32 {
    path
    .iter()
    .enumerate()
    .find(|&(n, pos)| path.iter().take(n).contains(pos))
    .map(|(_, d)| d.0.abs() + d.1.abs())
    .unwrap()
}


fn turn_left(input: (i32, i32)) -> (i32, i32){
    match input {
        (n, 0) => (0, n),
        (0, n) => (-n, 0),
        _ => unreachable!()
    }
}

fn turn_right(input: (i32, i32)) -> (i32, i32){
    match input {
        (n, 0) => (0, -n),
        (0, n) => (n, 0),
        _ => unreachable!()
    }
}