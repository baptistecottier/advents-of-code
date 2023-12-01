aoc::main!();

fn preprocessing(input: &str) -> u32 {
    input.parse().unwrap()
}

fn part_1(square_position: u32) -> u32 {
    let circle_index = (1.0 + ((square_position - 1) as f32).sqrt() / 2.0) as u32;
    circle_index + (square_position - 1) % circle_index 
}

fn part_2(square_position: u32) -> u32 {
    square_position
}