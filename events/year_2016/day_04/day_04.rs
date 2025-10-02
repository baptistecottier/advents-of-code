aoc::main!();

fn preprocessing(input: &str) -> Vec<(String, u32, String)> {
    input
        .lines()
        .map(|l| l.rsplitn(4, ['-', '[', ']']).collect_vec())
        .map(|l| {
            (
                l[3].replace('-', ""),
                l[2].parse::<u32>().unwrap(),
                l[1].to_string(),
            )
        })
        .collect_vec()
}

fn part_1(rooms: Vec<(String, u32, String)>) -> u32 {
    rooms
        .iter()
        .map(|(name, id, cs)| {
            (
                name.chars()
                    .counts()
                    .into_iter()
                    .sorted_by(|a, b| Ord::cmp(&b.1, &a.1).then(Ord::cmp(&a.0, &b.0)))
                    .map(|(c, _)| c)
                    .take(5)
                    .collect::<String>(),
                id,
                cs,
            )
        })
        .filter(|(name, _, cs)| *cs == name)
        .map(|(_, id, _)| id)
        .sum::<u32>()
}

fn part_2(rooms: Vec<(String, u32, String)>) -> u32 {
    rooms
        .iter()
        .find(|(name, id, _)| {
            name.as_bytes()
                .iter()
                .map(move |&c| (97 + ((id - 97 + c as u32) % 26)) as u8 as char)
                .collect::<String>()
                .contains("north")
        })
        .unwrap()
        .1
}
