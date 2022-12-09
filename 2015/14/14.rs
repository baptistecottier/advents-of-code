aoc_2015::main!();

fn generator(input : &str) -> Vec<(usize, usize, usize)> {
    input   
        .lines()
        .map(|l| l.split_whitespace().collect_vec())
        .map(|v| (v[3].parse::<usize>().unwrap(), v[6].parse::<usize>().unwrap(), v[13].parse::<usize>().unwrap()))
        .collect_vec()
}

fn part_1(input : Vec<(usize, usize, usize)>) -> usize {
    *solver(input.clone(), 2503)
        .iter()
        .max()
        .unwrap()
}

fn part_2(input : Vec<(usize, usize, usize)>) -> usize {
    let mut bonus = [0 ; 9] ; 
    (1..2503)
        .for_each(|s| {
            let score = solver(input.clone(),s);
            score.iter()
                .positions(|v| v == score.iter().max().unwrap())
                .for_each(|v|  bonus[v] += 1) ;
        });
        *bonus.iter().max().unwrap()
    }

fn solver(input : Vec<(usize, usize, usize)>, seconds : usize) -> Vec<usize> {
    input
    .iter()
    .map(|(speed, time, rest)| {
        let q = seconds / (time + rest);
        let r = if *time < (seconds % (*time + *rest)) {*time} else {seconds % (*time + *rest)} ;
        q * time * speed + speed*  r
    }
)
.collect_vec()
}