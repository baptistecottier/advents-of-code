aoc2016::main!() ; 

fn generator(input: &str) -> Vec<String> {
    let k = input.len() / (input.lines().count()) ;
    (0..k)
        .map(|i| input.chars().skip(i).step_by(k+1).collect::<String>())
        .collect_vec()
}

fn part_1(input: Vec<String>) -> String {
    solver(input, 1)
}

fn part_2(input: Vec<String>) -> String {
   solver(input, -1)
}

fn solver(input: Vec<String>, i: i8) -> String {
    input
        .iter()
        .map(|r| r.chars().counts().into_iter().max_by_key(|x| i * (x.1 as i8)).unwrap())
        .map(|x| x.0)
        .collect::<String>()
}