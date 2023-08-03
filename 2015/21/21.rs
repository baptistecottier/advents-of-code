aoc::main!();


const WEAPONS: [(i16, i16, i16); 5] = [
    (8, 4, 0), 
    (10, 5, 0), 
    (25, 6, 0), 
    (40, 7, 0), 
    (74, 8, 0)];

const ARMORS: [(i16, i16, i16); 6] = [
    (0, 0, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5)];

const RINGS: [(i16, i16, i16); 7] = [
    (0, 0, 0),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (80, 0, 3),
    (40, 0, 2)];

fn parser(input: &str) -> Vec<i16> {
    input
        .lines()
        .map(|l| l.split(": ").collect_vec()[1].parse::<i16>().unwrap())
        .collect_vec()
}

fn part_1(boss_stats : Vec<i16>) -> i16 {
    *solver(boss_stats, true)
        .iter()
        .min()
        .unwrap()
}

fn part_2(boss_stats : Vec<i16>) -> i16 {
    *solver(boss_stats, false)
        .iter()
        .max()
        .unwrap()
}

fn solver(boss_stats : Vec<i16> , winner : bool) -> Vec<i16> {
    iproduct!(WEAPONS, ARMORS, RINGS, RINGS)
        .filter(|(_, _, r1, r2)| r1 != r2 || *r1 == (0,0,0))
        .filter(|(w,a,r1,r2)| {
            let weapon = 1.max(w.1 + r1.1 + r2.1 - boss_stats[2]); 
            let armor = 1.max(boss_stats[1] - (a.2 + r1.2 + r2.2)) ;
            match winner {
                true => boss_stats[0] * armor <= 100 * weapon,
                false => boss_stats[0] * armor > 100 * weapon }})
        .map(|(w,a,r1,r2)| w.0 + a.0 + r1.0 + r2.0)
        .collect_vec()
}