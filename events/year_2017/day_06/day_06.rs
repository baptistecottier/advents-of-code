aoc::main!();

fn preprocessing(puzzle_input: &str) -> Vec<usize> {
    puzzle_input
    .split_whitespace()
    .map(|n| n.parse().unwrap())
    .collect_vec()
}

fn part_1(banks: Vec<usize>) -> usize {
    solver(banks, 0)
}

fn part_2(banks: Vec<usize>) -> usize {
    solver(banks, 1)
}

fn solver(mut banks: Vec<usize>, pas_ouf: usize) -> usize {
    *(1..)
    .fold_while(HashMap::from([(banks.clone(), 0)]), |mut acc, n| {
        banks = redistribute(banks.clone());
        if acc.contains_key(&banks) {
            acc.insert(banks.clone(), n - pas_ouf * acc.get(&banks).unwrap());
            FoldWhile::Done(acc)}
        else {
            acc.insert(banks.clone(), n);
            FoldWhile::Continue(acc)}})
    .into_inner()
    .get(&banks)
    .unwrap()
}

fn redistribute(banks: Vec<usize>) -> Vec<usize> {
    let binding = banks.clone();

    let (i, b) = 
        binding
        .iter()
        .find_position(|bank| *bank == banks.iter().max().unwrap())
        .unwrap();
    

    banks
    .iter()
    .enumerate()
    .map(|(k, bank)|
        (k != i) as usize * bank 
        + b / 16 
        + (((k + 16 - (i + 1)) % 16 < (b % 16)) as usize))
    .collect_vec()
}