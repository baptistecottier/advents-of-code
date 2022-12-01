aoc2018::main!();

fn generator(input : &str) -> Vec<i32> {
    input
        .lines()
        .map(|value| value.parse::<i32>().unwrap())
        .collect_vec()
}

fn part_1(input : Vec<i32>) -> i32 {
    input
        .iter()
        .sum()
}

fn part_2(input : Vec<i32>) -> i32 {
    input
        .iter()
        .cycle()
        .fold_while((0, HashSet::new()), |(frequence, mut reached_frequences) , change| 
            if !reached_frequences.insert(frequence + change) {
                FoldWhile::Done((frequence + change, reached_frequences))
            } else {
                FoldWhile::Continue((frequence + change, reached_frequences))
            })
            .into_inner()
            .0
        }