aoc::main!();

use std::usize::MAX;

fn preprocessing(input: &str) -> Vec<(usize, usize, usize)> {
    let n_bots = 
        input
        .lines()
        .filter(|l| ! l.contains("value"))
        .count();

    input
    .lines()
    .map(|l| l.split(' ').collect_vec())
    .map(|w| 
        match w.len() {
            6 => (MAX, w[1].parse::<usize>().unwrap(),w[5].parse::<usize>().unwrap()),
            _ => {
                let v = 
                    [1, 6, 11]
                    .iter()
                    .map(|&n| w[n].parse::<usize>().unwrap())
                    .collect_vec();
                
                match (w[5] == "bot", w[10] == "bot") {
                    (true , true)  => (v[0], v[1],          v[2]),
                    (true , false) => (v[0], v[1],          v[2] + n_bots),
                    (false, true)  => (v[0], v[1] + n_bots, v[2]),
                    (false, false) => (v[0], v[1] + n_bots, v[2] + n_bots)}}})
    .sorted()
    .collect_vec()
 }

 fn part_1(input: Vec<(usize, usize, usize)>) -> usize {
    solver(input).0
 }

 fn part_2(input: Vec<(usize, usize, usize)>) -> usize {
    solver(input).1
 }


 fn solver(instructions: Vec<(usize, usize, usize)>) -> (usize, usize) {
    let n_bots = 
        instructions
        .iter()
        .filter(|(a,_,_)| *a != MAX)
        .count();

    let n_outputs = 
        instructions
        .iter()
        .filter(|(_, b, c)| *b > n_bots ||  *c > n_bots)
        .count();
                
    let mut bots: Vec<Vec<usize>> = 
        (0..=1 + n_bots + n_outputs)
        .map(|_| Vec::new())
        .collect_vec();

    let mut answer = 0;

    instructions
    .clone()
    .iter()
    .filter(|inst| inst.0 == MAX)
    .for_each(|&(_, v, b)| bots[b].push(v)) ;

    loop {
        let binding = bots.clone();

        let to_distribute = 
            binding
            .iter()
            .enumerate()
            .filter(|(_, b)| b.len() == 2)
            .map(|(n, b)| (n,b.iter().sorted().collect_vec()))
            .collect_vec(); 

        if to_distribute.len() == 0 {break;}

        to_distribute
        .iter()
        .for_each(|(n, b)| {
            if *b == [&17, &61] {answer = *n;}
            let (_, i_low, i_high) = instructions[*n];
            bots[i_low].push(*b[0]);
            bots[i_high].push(*b[1]);
            bots[*n] = Vec::new();})}

    (answer , (0..3).map(|n| bots[n_bots + n][0]).product())
 }