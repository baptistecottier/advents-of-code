aoc::main!();

fn parser(input: &str) -> Vec<&str> {
    input
    .lines()
    .collect_vec()
 }

 fn part_1(procedure: Vec<&str>) -> String {
    solver(procedure.clone(), false)
    .into_iter()
    .map(|(x,y) :(i32, i32)| (1 + 3 * y + x).to_string())
    .join("")
    }
    
fn part_2(procedure: Vec<&str>) -> String {
    solver(procedure.clone(), true)
    .into_iter()
    .map(|(x,y) :(i32, i32)| {format!("{:X}", 1 + y * (y - ((y == 4) as i32)) - (2 - y).abs() + x)})
    .join("")
}


fn solver(procedure: Vec<&str>, bathroom_keyboard: bool) -> Vec<(i32, i32)> {
    procedure
    .iter()
    .map(|instr|{
        instr
        .chars()
        .fold((1,1), |acc : (i32, i32), c| {
            let bounds = 
                match bathroom_keyboard { 
                    false => (0, 2, 2, 0),
                    true => ((acc.0 - 2).abs(), 4 - (acc.0 - 2).abs(), 4 - (acc.1 - 2).abs(), (acc.1 - 2).abs())};
            match c {
                'U' => (acc.0, (bounds.0).max(acc.1 - 1)),
                'D' => (acc.0, (bounds.1).min(acc.1 + 1)),
                'R' => ((bounds.2).min(acc.0 + 1), acc.1),
                'L' => ((bounds.3).max(acc.0 - 1), acc.1),
                _ => unreachable!()}})})
    .collect_vec()
}
