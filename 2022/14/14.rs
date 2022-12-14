aoc2022::main!() ;

fn generator(input : &str) -> ([[u32 ; 1000] ; 200] , usize) {
    let mut cave = [[0 ; 1000] ; 200];
    let mut max_depth = 0 ;
    input
        .lines()
        .map(|l| l.split(" -> ").map(|c| c.split(',').map(|n| n.parse::<usize>().unwrap()).collect_vec()).collect_vec())
        .for_each(|path| path.iter().tuple_windows().for_each(|(start, end)| 
            iproduct!(start[0].min(end[0]) .. start[0].max(end[0]) + 1 , start[1].min(end[1]) .. start[1].max(end[1]) + 1)
                .for_each(|(x, y)| {
                max_depth = max_depth.max(y) ; 
                cave[y][x]=1 ; })
    ));
    ( cave, max_depth)
}

fn part_1(input :  ([[u32 ; 1000] ; 200] , usize)) -> u32 {
    solver(input.0, input.1, false)
}

fn part_2(input :  ([[u32 ; 1000] ; 200] , usize)) -> u32 {
    solver(input.0, input.1 , true)
}

fn solver(mut cave : [[u32 ; 1000] ; 200], mut max_depth : usize, floor : bool) -> u32 {

    let mut sand = 0 ; 
    let (mut x, mut y) = (500 ,0);

    if floor { 
        max_depth += 2 ;
        (0 .. 1000).for_each(|x| cave[max_depth][x] = 1)} ;
        
    loop {
        if cave[0][500] == 1 || y >= max_depth {return sand} 
        else if cave[y+1][x] == 0  {y += 1}
        else if cave[y+1][x-1] == 1 && cave[y+1][x+1] == 1 {
            cave[y][x] = 1 ;
            sand += 1 ;
            (x, y) = (500, 0)  ; 
        } 
        else if cave[y+1][x-1] == 0 { (x , y) = (x - 1, y + 1) }
        else if cave[y+1][x+1] == 0 { (x , y) = (x + 1, y + 1) }
    }
    }