aoc::main!();

fn preprocessing(puzzle_input: &str) -> String {
    Regex::new(r"\!.")
        .unwrap()
        .replace_all(puzzle_input, "")
        .to_string()
}

fn part_1(record: String) -> usize {
    record
        .chars()
        .fold((0, 0, 0), |(garbage, score, step), char| {
            match (garbage, char) {
                (1, '>') => (0, score, step),
                (0, '<') => (1, score, step),
                (0, '{') => (garbage, score + step + 1, step + 1),
                (0, '}') => (garbage, score, step - 1),
                _ => (garbage, score, step),
            }
        })
        .1
}

fn part_2(record: String) -> usize {
    record
        .chars()
        .fold((0, 0), |(garbage, count), char| match (garbage, char) {
            (1, '>') => (0, count),
            (0, '<') => (1, count),
            (1, _) => (garbage, count + 1),
            _ => (garbage, count),
        })
        .1
}
