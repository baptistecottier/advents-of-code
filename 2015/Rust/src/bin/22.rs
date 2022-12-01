aoc_2015::main!();

fn generator(input : &str) -> Vec<i16> {
    input
        .lines()
        .map(|l| l.split(": ").collect_vec()[1].parse::<i16>().unwrap())
        .collect_vec()
}

const SPELLS: [(i16, i16, i16, i16, i16, i16); 5] = [ // (cost, duration, damage, heal, armor, mana recharhe)
    (53,1,4,0,0,0),
    (73,1,2,2,0,0),
    (113,6,0,0,7,0),
    (173,6,3,0,0,0),
    (229,5,0,0,0,101)
];

fn part_1(input : Vec<i16>) -> i16 {
    
    
    2
}