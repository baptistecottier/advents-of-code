aoc::main!();

fn preprocessing(input_: &str) -> Vec<(u32, u32)> {
    input_
    .lines()
    .map(|layer|
        layer
        .split(": ")
        .map(|n| n.parse::<u32>().unwrap())
        .collect_tuple()
        .map(|(layer, depth)| (layer, 2 * (depth - 1)))
        .unwrap())
    .collect_vec()
}

fn part_1(record: Vec<(u32, u32)>) -> u32 {
    record
    .iter()
    .map(|(layer, depth)|
        if layer % depth == 0 {layer * (depth / 2 + 1)}
        else {0})
    .sum()
}

fn part_2(record: Vec<(u32, u32)>) -> u32 {
    (1..)
    .find(|&delay| 
        record
        .iter()
        .all(|(layer, depth)| ((delay + layer) % depth) != 0))
    .unwrap()
}