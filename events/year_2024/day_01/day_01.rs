aoc::main!();

fn preprocessing(input: &str) -> (Vec<i32>, Vec<i32>) {
    input
        .lines()
        .map(|l| l.split_once("   ").unwrap())
        .map(|(l, r)| (l.parse::<i32>().unwrap(), r.parse::<i32>().unwrap()))
        .unzip()
}

fn part_1(lists: (Vec<i32>, Vec<i32>)) -> i32 {
    zip(lists.0.iter().sorted(), lists.1.iter().sorted())
        .map(|(l, r)| (l - r).abs())
        .sum()
}

fn part_2(lists: (Vec<i32>, Vec<i32>)) -> usize {
    lists
        .0
        .iter()
        .counts()
        .iter()
        .map(|(&&l, n)| n * (l as usize) * lists.1.iter().filter(|&&r| l == r).count())
        .sum()
}
