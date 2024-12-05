aoc::main!();

//  Preprocessing mainly consists in parsing the puzzle input, returning the
//  list of all rules pages have to follow and the incoming updates
fn preprocessing(puzzle_input: &str) -> (Vec<(i16, i16)>, Vec<Vec<i16>>) {
    let (rules, updates) = puzzle_input.split_once("\n\n").unwrap();
    (   
        rules
        .lines()
        .into_iter()
        .map(|rule| rule.split_once('|').unwrap())
        .map(|(l, r)| (l.parse().unwrap(), r.parse().unwrap()))
        .collect_vec()
    ,   
        updates
        .lines()
        .into_iter()
        .map(|update| update.split(",").map(|n| n.parse().unwrap()).collect())
        .collect()
    )
}


//  Solving part 1 consists in browsing updates keeping only those that are 
//  ordered and then summing their mid value
fn part_1(elf_data: (Vec<(i16, i16)>, Vec<Vec<i16>>)) -> i16 {
    let (rules, updates) = elf_data;
    updates
    .into_iter()
    .filter(|update| is_ordered(update.to_vec(), rules.clone()) == 100)
    .map(|update| update[update.len() / 2])
    .sum()
}


//  To solve part 2, we extract unordered updates then we swap pages number 
//  not respecting rules until pages are correctly ordered. Finally, we 
//  compute the sum of their mid value.
fn part_2(elf_data: (Vec<(i16, i16)>, Vec<Vec<i16>>)) -> i16 {
    let (rules, updates) = elf_data;
    updates
    .into_iter()
    .filter(|update| is_ordered(update.to_vec(), rules.clone()) != 100)
    .map(|mut update| {
        let mut i = is_ordered(update.to_vec(), rules.clone());
        while i != 100 {
            update.swap(i, i + 1);
            i = is_ordered(update.to_vec(), rules.clone());};
        update})
    .map(|update| update[update.len() / 2])
    .sum()
}


//  This function checks if all pages of an update are ordered. If not, the
//  function returns the postion of the pages not respecting the rule. 
//  Otherwise, as all value are below 100, we set 100 as the value asserting
//  ordering is correct.
fn is_ordered(update: Vec<i16>, rules: Vec<(i16, i16)>) -> usize {
    update
    .into_iter()
    .tuple_windows()
    .find_position(|(a, b)| !rules.contains(&(*a, *b)))
    .unwrap_or_else(|| (100, (0, 0)))
    .0
}