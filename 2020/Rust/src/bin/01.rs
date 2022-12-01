aoc2020::main!();

fn generator(input : &str) -> Vec<u32> {
   input
        .lines()
        .map(|l| l.parse().unwrap())
        .collect_vec()
}

fn part_1(input : Vec<u32> ) -> u32 {
    iproduct!(input.clone(), input.clone())
        .into_iter()
        .find(|(a,b)| a + b == 2020)
        .map(|(a,b)| a * b)
        .unwrap()
}

fn part_2(input : Vec<u32> ) -> u32 {
    iproduct!(input.clone(), input.clone(), input.clone())
        .into_iter()
        .find(|(a,b,c)| a + b + c == 2020)
        .map(|(a,b,c)| a * b * c)
        .unwrap()
}