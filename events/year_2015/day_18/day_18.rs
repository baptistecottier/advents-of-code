aoc::main!();

fn preprocessing(input: &str) -> [[u8 ; 102] ; 102] {
    let mut grid = [[0 ; 102] ; 102];
    input
    .lines()
    .enumerate()
    .for_each(|(i,l)| {
        l.chars().enumerate().for_each(|(j,c)| {
            if c == '#' {grid[i+1][j+1]=1};
        })
    });
    grid
}

fn switch(bulb: u8, ngb: u8) -> u8 {
    (ngb == 3 || (bulb == 1 && ngb == 2)) as u8 
}

fn neighbours(row: usize, col: usize, grid: [[u8 ; 102] ; 102]) -> u8 {
    [grid[row-1][col-1], grid[row-1][col], grid[row-1][col+1], 
    grid[row][col-1], grid[row][col+1], 
    grid[row+1][col-1], grid[row+1][col], grid[row+1][col+1]].iter().sum()
}

fn turn_on_corners(mut grid: [[u8 ; 102] ; 102]) -> [[u8 ; 102] ; 102] {
    grid[1][1]=1;
    grid[1][100]=1;
    grid[100][1]=1;
    grid[100][100]=1;
    grid
}

fn solver(mut grid: [[u8 ; 102] ; 102] , corners: bool) -> usize {
    let mut temp_grid = [[0 ; 102] ; 102];
    (0..100)
    .for_each(|_| {
        (1..101)
        .for_each(|row| {
            (1..101)
            .for_each(|col| {
                temp_grid[row][col] = switch(grid[row][col] , neighbours(row, col, grid))
            })
        });
        if corners {grid = turn_on_corners(temp_grid)} else {grid = temp_grid};
        temp_grid = [[0 ; 102] ; 102];
        
    }) ;
    grid
    .iter()
    .map(|v| v.iter().fold(0, |acc, b| acc + b))
    .fold(0, |acc: usize, b| acc + b as usize)
}

fn part_1(grid: [[u8 ; 102] ; 102]) -> usize {
    solver(grid, false)
}

fn part_2(grid: [[u8 ; 102] ; 102]) -> usize {
    solver(turn_on_corners(grid), true)
}