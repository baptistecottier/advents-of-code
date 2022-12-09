aoc2022::main!();

fn generator(input : &str) -> Vec<(i32, i32)> {
    input
        .lines()
        .map(|l| l.split_whitespace().collect_vec())
        .map(|v| (v[1].parse::<i32>().unwrap() , match v[0] {
            "D" => (0 , -1),
            "U" => (0 , 1),
            "R" => (1 , 0),
            "L" => (-1, 0),
            _ => unreachable!(), } ))
        .fold(vec![(0,0)] , |mut head_pos,  (n , (dx , dy))| {
            head_pos.append(&mut 
                (1..=n).scan( 
                    head_pos.last().unwrap() , | new_pos , i |{
                    Some((new_pos.0 + i * dx , new_pos.1 + i * dy))})
            .collect_vec()) ; 
            head_pos.clone()})
       
}

fn part_1(path : Vec<(i32, i32)>) -> usize {
    solver(path, 2)
}

fn part_2(path : Vec<(i32, i32)>) -> usize {
    solver(path, 10)
}

fn solver(mut path : Vec<(i32 ,i32)>, knots : usize) -> usize {
    (0 .. knots-1)
        .for_each(|_| {
            let mut tail_pos = (0 , 0) ; 
            path.clone()
                .iter()
                .enumerate()
                .for_each(|(n, head_pos)| {
                    let d = ((head_pos.0 - tail_pos.0).abs() > 1 || (head_pos.1 - tail_pos.1).abs() > 1 ) as i32 ;
                    tail_pos.0 += d * (head_pos.0 - tail_pos.0).signum() ;
                    tail_pos.1 += d * (head_pos.1 - tail_pos.1).signum() ;
                    path[n] = (tail_pos.0, tail_pos.1)
                })
        });
    path.iter().unique().count()
}