aoc::main!();

fn preprocessing(input: &str) -> HashMap<String, Vec<(usize, String)>> {
    input
        .replace(" bags", "")
        .replace(" bag", "")
        .replace(".", "")
        .lines()
        .map(|luggage| {
            luggage
                .split(" contain ")
                .collect_tuple::<(_, _)>()
                .unwrap()
        })
        .map(|(big_bag, content)| {
            (
                big_bag.to_string(),
                content
                    .split(", ")
                    .map(|bag| bag.split_once(" ").unwrap())
                    .map(|(n, color)| (n.parse().unwrap_or(0), color.to_string()))
                    .collect_vec(),
            )
        })
        .collect::<HashMap<String, Vec<(usize, String)>>>()
}

fn part_1(rules: HashMap<String, Vec<(usize, String)>>) -> usize {
    rules
        .keys()
        .filter(|&bag| contains_shiny_gold(&rules, bag))
        .count()
        - 1
}

fn part_2(rules: HashMap<String, Vec<(usize, String)>>) -> usize {
    rules["shiny gold"]
        .iter()
        .map(|(n, bag)| n * count_bags(&rules.clone(), bag))
        .sum()
}

fn contains_shiny_gold(rules: &HashMap<String, Vec<(usize, String)>>, bag: &String) -> bool {
    bag == "shiny gold"
        || rules
            .get(bag)
            .unwrap_or(&Vec::new())
            .iter()
            .any(|(_, subbag)| contains_shiny_gold(rules, subbag))
}

fn count_bags(rules: &HashMap<String, Vec<(usize, String)>>, bag: &String) -> usize {
    1 + rules
        .get(bag)
        .unwrap_or(&Vec::new())
        .iter()
        .map(|(n, c)| n * count_bags(rules, c))
        .sum::<usize>()
}
