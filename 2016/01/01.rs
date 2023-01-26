aoc2016::main!();

fn generator(input: &str) -> Vec<(i32,i32)> {
    let mut dir = (1,0);
    let mut pos = (0,0);
    input
        .split(", ")
        .map(move |info| {
            let turn = info.clone().chars().nth(0).unwrap() ;
            let l = info[1..].parse::<i32>().unwrap() ;
            match turn {
                'R' => dir = turn_right(dir),
                'L' => dir = turn_left(dir),
                _ => unreachable!()} ;
                (dir, l) })
        .map(|(dir, l)| {(1..l+1)
            .scan(pos, |_,_| {pos = (pos.0 + dir.0, pos.1 + dir.1);
                Some(pos)})
            .collect_vec()})
        .flatten()
        .collect_vec()
}


fn part_1(input: Vec<(i32,i32)>) -> i32 {
    input
        .iter()
        .last()
        .map(|d| d.0.abs() + d.1.abs())
        .unwrap()
}

fn part_2(input: Vec<(i32,i32)>) -> i32 {
    input
        .iter()
        .enumerate()
        .find(|&(n,pos)| input.iter().take(n).contains(pos))
        .map(|(_,d)| d.0.abs() + d.1.abs())
        .unwrap()
}


fn turn_left(input: (i32, i32)) -> (i32, i32){
    match input {
        (1,0) => (0,1),
        (0,1) => (-1,0),
        (-1,0) => (0,-1),
        (0,-1) => (1,0),
        _ => unreachable!()
    }
}

fn turn_right(input: (i32, i32)) -> (i32, i32){
    match input {
        (1,0) => (0,-1),
        (0,-1) => (-1,0),
        (-1,0) => (0,1),
        (0,1) => (1,0),
        _ => unreachable!()
    }
}