aoc::main!() ;

fn preprocessing(input: &str) -> String {
    input.to_string()
}

fn part_1(digits: String) -> usize {
solve(digits, 40)
    }

fn part_2(digits: String) -> usize {
    solve(digits, 50)
}

fn solve(mut digits: String, loops: usize) -> usize {
    let mut i = 0 ; 
    while i < loops {
        let new_input = 
            digits
            .to_string()
            .chars()
            .dedup_with_count()
            .into_iter()
            .fold("".to_string(), | acc , (c, l)| acc + &c.to_string() + &l.to_string());
        digits = new_input.clone();
        i += 1 ;};
    digits.len()
    }
