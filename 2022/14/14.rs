aoc2022::main!() ;

fn generator(input : &str) -> ([[u8 ; 1000] ; 200] , usize) {
    let mut cave = [[0 ; 1000] ; 200];
    let mut max_depth = 0 ;
    input
        .lines()
        .map(|l| l.split(" -> ").map(|c| c.split(',').map(|n| n.parse::<usize>().unwrap()).collect_vec()).collect_vec())
        .for_each(|path| path.iter().tuple_windows().for_each(|(start, end)| 
            iproduct!(start[0].min(end[0]) .. start[0].max(end[0]) + 1 , start[1].min(end[1]) .. start[1].max(end[1]) + 1)
                .for_each(|(x, y)| {
                    max_depth = max_depth.max(y) ; 
                    cave[y][x] = 1 ; })
    ));
    (0 .. 1000).for_each(|x| cave[max_depth + 2][x] = 1) ;
    (cave, max_depth)
}

fn part_1(input :  ([[u8 ; 1000] ; 200] , usize)) -> usize {
    solver(input.0, input.1, false)
}

fn part_2(input :  ([[u8 ; 1000] ; 200] , usize)) -> usize {
    solver(input.0, input.1 , true)
}

fn solver(mut cave : [[u8 ; 1000] ; 200], max_depth : usize, floor : bool) -> usize {
    let (mut x, mut y, mut sand) = (500, 0, 0);

    while cave[0][500] == 0 && y < max_depth + (2 * (floor as usize)) {
        match (cave[y+1][x-1] , cave[y+1][x] , cave[y+1][x+1]) {
            (_, 0, _ )  => y += 1 ,
            (0, _, _)   => { (x , y) = (x - 1, y + 1) } ,
            (_, _, 0)   => { (x , y) = (x + 1, y + 1) } ,
            _           => { cave[y][x] = 1 ; (x, y) = (500, 0); sand += 1} ,
            } 
        }
        sand
    }