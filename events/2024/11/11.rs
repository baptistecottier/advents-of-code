aoc::main!() ; 

fn preprocessing(input: &str) -> HashMap<u64, usize> {
    blink(
        input
        .split_whitespace()
        .map(|stone| stone.parse().unwrap())
        .counts()
        , 25)
}


fn part_1(stones: HashMap<u64, usize>) -> usize {
    stones
    .values()
    .sum()
}


fn part_2(stones: HashMap<u64, usize>) -> usize {
    blink(stones, 50)
    .values()
    .sum()}
    
    
fn blink(stones: HashMap<u64, usize>, times: usize) -> HashMap<u64, usize> {
    (0..times)
    .fold(stones, |stones, _| 
        stones
        .iter()
        .fold(HashMap::new(), |mut new_stones, (stone, &n)| {
            if *stone == 0 { *new_stones.entry(1).or_insert(0) += n }
            else {
                match stone.ilog10().is_even() {
                    true => *new_stones.entry(2024 * stone).or_insert(0) += n ,
                    false => {
                        let (div, rem) = stone.div_rem_euclid(&(pow(10, 1 + (stone.ilog10() as usize) / 2)));
                        *new_stones.entry(div).or_insert(0) += n ;
                        *new_stones.entry(rem).or_insert(0) += n ;}
                };
            };
        new_stones})
    )
}
    