aoc2016::main!();

fn generator(input: &str) -> Vec<(usize, usize, usize)> {
    input
        .lines()
        .map(|l| l.split([' ','=','x']).collect_vec())
        .map(|l| match l.len() {
            3 => (0, l[1].parse::<usize>().unwrap(), l[2].parse::<usize>().unwrap()),
            6 => (1, l[3].parse::<usize>().unwrap(), l[5].parse::<usize>().unwrap()),
            7 => (2, l[4].parse::<usize>().unwrap(), l[6].parse::<usize>().unwrap()),
            _ => unreachable!()
        })
        .collect_vec()
}

fn part_1(input: Vec<(usize, usize, usize)>) -> usize {
    solver(input).chars().filter(|&c| c == '█').count()
}

fn part_2(input: Vec<(usize, usize, usize)>) -> String {
    solver(input)
}


fn solver(input: Vec<(usize, usize, usize)>) -> String {
    let mut screen = [[' ';50];6];
    input
        .iter()
        .for_each(|&(op, a, b)| match op {
            0 => iproduct!(0..a,0..b).for_each(|(x,y)|screen[y][x] = '█'),
            1 => screen[a].rotate_right(b) ,
            2 => (0..6).map(|y| (y,screen[y][a])).collect_vec().iter().for_each(|(y,k)| screen[(y + b) % 6][a] = *k) ,
            _ => unreachable!()
        });
    screen.iter().map(|l| l.iter().join("")).join("\n")
}