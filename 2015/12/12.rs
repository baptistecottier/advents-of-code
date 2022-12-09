aoc_2015::main!(); 

fn part_1(input : String) -> i32 {
    input
        .split(['{','}','[',']',',',':'])
        .map(|c| match c.parse::<i32>() {
            Ok(v) => v ,
            Err(_) => 0 ,
        })
        .sum()
}

fn part_2(input : String) -> i32 {
    input
        .split(['{','}','[',']',',',':'])
        .map(|c| match c.parse::<i32>() {
            Ok(v) => v ,
            Err(_) => 0 ,
        })
        .sum()
}
