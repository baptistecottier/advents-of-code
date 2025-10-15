aoc::main! {}

fn preprocessing(puzzle_input: &str) -> (Vec<String>, usize) {
    let mut reaching_paths = Vec::new();

    let candidates = [("U", (0, -1)), ("D", (0, 1)), ("L", (-1, 0)), ("R", (1, 0))];
    let opens = b"bcdef";

    let mut paths = VecDeque::from([(puzzle_input.to_string(), (0, 0))]);
    let in_bounds = |(x, y): (i32, i32)| (0..=3).contains(&x) && (0..=3).contains(&y);
    while let Some((path, pos)) = paths.pop_front() {
        let digest = format!("{:x}", &md5::compute(&path));
        for (i, (s, (dx, dy))) in candidates.iter().enumerate() {
            if opens.contains(&digest.as_bytes()[i]) {
                let next_pos = (pos.0 + dx, pos.1 + dy);
                if next_pos == (3, 3) {
                    reaching_paths.push(path.clone() + s);
                } else if in_bounds(next_pos) {
                    paths.push_back((format!("{path}{s}"), next_pos));
                }
            }
        }
    }
    (reaching_paths, puzzle_input.len())
}

fn part_1((reaching_paths, salt_len): (Vec<String>, usize)) -> String {
    reaching_paths.first().unwrap()[salt_len..].to_string()
}

fn part_2((reaching_paths, salt_len): (Vec<String>, usize)) -> usize {
    reaching_paths.last().unwrap().len() - salt_len
}
