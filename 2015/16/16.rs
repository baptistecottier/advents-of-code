aoc::main!();

fn parser(input: &str) -> Vec<HashMap<&str, u16>> {
    input
    .lines()
    .map(|l| -> Vec<&str> {l.split(&[':',',',' ']).collect_vec()})
    .map(|v| 
        HashMap::from([
            (v[3], v[5].parse().unwrap()),
            (v[7],  v[9].parse().unwrap()),
            (v[11], v[13].parse().unwrap())]))
    .collect_vec()
}


fn part_1(aunts : Vec<HashMap<&str, u16>>) -> usize {
    find_sue(aunts, Vec::new(), Vec::new())
}

fn part_2(aunts : Vec<HashMap<&str, u16>>) -> usize {
    find_sue(aunts, Vec::from(["cats", "trees"]), Vec::from(["pomeranians", "goldfish"]))
}

fn find_sue(aunts : Vec<HashMap<&str, u16>>, lower: Vec<&str>, greater: Vec<&str>) -> usize {
    let sue = HashMap::from([
        ("akitas", 0)  , ("children", 3)   ,  ("cars", 2)    ,  ("cats", 7) , ("goldfish", 5), 
        ("perfumes", 1), ("pomeranians", 3),  ("samoyeds", 2),  ("trees", 3), ("vizslas", 0)]);
    
    aunts
    .iter()
    .find_position(|aunt| 
        aunt
        .iter()
        .all(|(k, v)| 
            if lower.contains(k) {sue.get(k).unwrap() < v}
            else if greater.contains(k) {sue.get(k).unwrap() > v} 
            else {sue.get(k).unwrap() == v}))
    .unwrap()
    .0 
    + 1
    }