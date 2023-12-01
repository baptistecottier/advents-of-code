aoc::main!() ; 

fn preprocessing(input: &str) -> Vec<String> {
    let k = input.len() / (input.lines().count()) ;
    
    (0..k)
    .map(|i| 
        input
        .chars()
        .skip(i)
        .step_by(k + 1)
        .collect::<String>())
    .collect_vec()
}

fn part_1(message: Vec<String>) -> String {
    solver(message, 1)
}

fn part_2(message: Vec<String>) -> String {
   solver(message, -1)
}

fn solver(message: Vec<String>, i: i8) -> String {
    message
    .iter()
    .map(|r| 
        r
        .chars()
        .counts()
        .into_iter()
        .max_by_key(|x| i * (x.1 as i8))
        .unwrap())
    .map(|x| x.0)
    .collect::<String>()
}