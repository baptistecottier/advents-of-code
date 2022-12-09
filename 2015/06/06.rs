aoc_2015::main!();

use grid::Grid;

fn generator(input: &str) -> Vec<(usize, usize, u8)> {
    input
        .lines()
        .map(|l| l.rsplitn(6, [' ',',']).collect_vec())
        .map(|l| {
            (
                match l[5] {
                    "turn off" => 0,
                    "turn on" => 1,
                    "toggle" => 2,
                    _ => unreachable!(),
                },
                l,
            )
        })
        .flat_map(|(a, l)| {
            iproduct!(
                l[3].parse::<usize>().unwrap()..=l[0].parse::<usize>().unwrap(),
                l[4].parse::<usize>().unwrap()..=l[1].parse::<usize>().unwrap()
            )
            .map(move |(x, y)| (x, y, a))
        })
        .collect()
}

fn part_1(input : Vec<(usize, usize, u8)>) -> usize {
    let mut grid : Grid<u8> = Grid::new(1000,1000); 
    input
        .iter()
        .for_each(|(x,y,a)| {
            match a {
            2 => grid[*x][*y] =grid[*x][*y] ^ 1,
            _ => grid[*x][*y] = *a,
            };
        });
        grid.iter().filter(|&n| *n == 1).count()
}

fn part_2(input : Vec<(usize, usize, u8)>) -> u32 {
    let mut grid : Grid<u32> = Grid::new(1000,1000); 
    input
        .iter()
        .for_each(|(x,y,a)| {
            match a {
            0 => grid[*x][*y]= grid[*x][*y].saturating_sub(1),
            _ => grid[*x][*y] += *a as u32,
            };
        });
        grid.flatten().iter().sum()
}