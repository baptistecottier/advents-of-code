aoc::main!();

fn preprocessing(input: &str) -> Vec<&str> {
    input
    .split(',')
    .collect_vec()
}

fn hash(s: &str) -> u32 {
    s
    .chars()
    .fold(0, |acc, c| 17 * (acc + (c as u32)) % 256)
}

fn part_1(instructions: Vec<&str>) -> u32 {
    instructions
    .iter()
    .map(|s| hash(s))
    .sum()
}

fn part_2(instructions: Vec<&str>) -> u32 {
    instructions
    .into_iter()
    .map(|s| 
        if s.contains('-') {
            (s[..s.len()-1].to_string(), 0)
        } else {
            (s[..s.len()-2].to_string(), s.chars().next_back().unwrap() as u8)
        })
    .map(|(label, focal)| (hash(label.as_str()), label, focal))
    .fold(HashMap::<u32, HashMap<String, u8>>::new(), |lenses, (h, label, focal)| {
        if focal == 0 {
            lenses[&h].remove_entry(&label).unwrap();
        } else {
            lenses[&h].insert(label, focal);
        };
        lenses})
        .into_iter()
    .map(|(b, v)| (b as u32 + 1) * v.into_iter().enumerate().map(|(n, (_, f))| ((n + 1) as u32) * (*f as u32)).sum::<u32>())
    .sum()
}