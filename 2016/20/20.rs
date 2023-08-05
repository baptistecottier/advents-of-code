aoc::main!(); 

fn preprocessing(input: &str) -> Vec<(u32, u32)> {
    input
    .lines()
    .map(|range| 
        range
        .split('-')
        .map(|bound| 
            bound
            .parse::<u32>()
            .unwrap())
        .collect_tuple().unwrap())
    .collect_vec()
}

fn part_1(intervales: Vec<(u32,u32)>) -> usize {
    2
}

fn part_2(intervales: Vec<(u32,u32)>) -> usize {
    3
}


fn solver(start: u32, intervales: Vec<(u32,u32)>){
    
}