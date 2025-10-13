aoc::main!();

fn preprocessing(input: &str) -> Vec<&str> {
    input.lines().collect_vec()
}

fn part_1(strings: Vec<&str>) -> usize {
    strings
        .iter()
        .filter(|string| {
            string.matches(['a', 'e', 'i', 'o', 'u']).count() >= 3
                && !["ab", "cd", "pq", "xy"]
                    .iter()
                    .any(|substring| string.contains(substring))
                && string.chars().tuple_windows().any(|(a, b)| a == b)
        })
        .count()
}

fn part_2(strings: Vec<&str>) -> usize {
    strings
        .iter()
        .filter(|string| {
            string.chars().tuple_windows().any(|(a, _, c)| a == c)
                && string
                    .chars()
                    .tuple_windows()
                    .any(|(a, b)| string.matches(&[a, b].iter().collect::<String>()).count() >= 2)
        })
        .count()
}
