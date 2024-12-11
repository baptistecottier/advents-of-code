aoc::main!() ; 

fn preprocessing(input: &str) -> HashMap<u64, usize> {
    input
    .split_whitespace()
    .map(|stone| stone.parse().unwrap())
    .counts()
}


fn part_1(stones: HashMap<u64, usize>) -> usize {
    (0..25)
    .fold(stones, |stones, _| blink(stones))
    .values()
    .sum()
}


fn part_2(stones: HashMap<u64, usize>) -> usize {
    (0..75)
    .fold(stones, |stones, _| blink(stones))
    .values()
    .sum()}


fn blink(stones: HashMap<u64, usize>) -> HashMap<u64, usize> {
    stones
    .iter()
    .fold(HashMap::new(), |mut new_stones, (stone, &n)| {
        if *stone == 0 { *new_stones.entry(1).or_insert(0) += n }
        else {
            match stone.ilog10().is_even() {
                False => *new_stones.entry(2024 * stone).or_insert(0) += n ,
                True => {
                    let (div, rem) = stone.div_rem_euclid(&(pow(10, 1 + (stone.ilog10() as usize) / 2)));
                    *new_stones.entry(div).or_insert(0) += n ;
                    *new_stones.entry(rem).or_insert(0) += n ;
                }};
            };
        new_stones})
        }
    