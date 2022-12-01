aoc_2015::main!() ;

fn generator(input : &str) -> String {
    input.to_string()
}

fn part_1(input : String) -> usize {
solve(input, 40)
    }

fn part_2(input : String) -> usize {
    solve(input, 50)
}

fn solve(mut input : String, loops : usize) -> usize {
    let mut i = 0 ; 
    while i<loops {
            let new_input = input.to_string()
            .chars()
            .dedup_with_count()
            .into_iter()
            .fold("".to_string(), | acc , (c, l)| acc + &c.to_string() + &l.to_string());
            input = new_input.clone();
            i += 1 ; 
        };
    input.len()
    }
