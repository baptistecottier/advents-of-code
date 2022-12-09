aoc2022::main!();

fn generator(input : &str) -> Vec<(i32, i32)> {
    let mut x = 0 ;
    let mut y = 0 ;
    input
        .lines()
        .map(|l| l.split_whitespace().collect_vec())
        .map(|v| (v[1].parse::<i32>().unwrap() , match v[0] {
            "D" => (0 , -1),
            "U" => (0 , 1),
            "R" => (1 , 0),
            "L" => (-1, 0),
            _ => unreachable!(), } ))
        .map(|(n , (dx , dy))| (0..n).map(| _ |{
            x += dx ;
            y += dy ;
            (x , y)
            })
            .collect_vec())
        .flatten()
        .collect_vec()
}

fn part_1(path : Vec<(i32, i32)>) -> usize {
    solver(path, 2)
}

fn part_2(path : Vec<(i32, i32)>) -> usize {
    solver(path, 10)
}

fn solver(mut path : Vec<(i32 ,i32)>, knots : usize) -> usize {
    (0 .. knots-1)
        .for_each(| _| {
            let mut tx = 0 ; 
            let mut ty = 0 ; 
            path.clone()
                .iter()
                .enumerate()
                .for_each(|(n, (hx, hy))| {
                    let d = ((hx - tx).abs() > 1 || (hy - ty).abs() > 1 ) as i32 ;
                    tx += d * (hx - tx).signum() ;
                    ty += d * (hy - ty).signum() ;
                    path[n] = (tx, ty)
                })
        });
    path.iter().unique().count()
}