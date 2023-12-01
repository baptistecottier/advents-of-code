aoc::main!();

fn preprocessing(input: &str) -> Vec<&str> {
    input
    .lines()
    .collect_vec()
}

fn part_1(box_ids: Vec<&str>) -> usize {
    box_ids
    .iter()
    .map(|box_id| box_id.chars().counts().into_values().collect_vec())
    .map(|cnts| (cnts.contains(&2) as usize, cnts.contains(&3) as usize))
    .fold((0, 0, 0), |acc, cnt| (acc.0 + cnt.0, acc.1 + cnt.1, (acc.0 + cnt.0) * (acc.1 + cnt.1)))
    .2
}

fn part_2(box_ids: Vec<&str>) -> String {
    iproduct!(box_ids.clone(), box_ids)
    .map(|(ida, idb)| 
        zip(ida.chars(), idb.chars())
        .filter(|(a, b)| a == b)
        .map(|(a, _)| a)
        .join(""))
    .find(|ida| ida.len() == 25)
    .unwrap()
}