aoc2022::main!(); 

fn generator(input : &str) -> (Vec<String> , Vec<(usize, usize, usize)>) {
    let (crates, rearrangements) = input.split("\n\n").collect_tuple().unwrap() ; 
    
    let mut cargo = vec!["".to_string() ; crates.chars().nth_back(1).unwrap().to_digit(10).unwrap() as usize] ;
        crates
            .lines()
            .for_each( |c| {
                let v = c.split('[').collect_vec() ; 
                let mut s = v[0].len() / 4 ;
                (v[1..])
                .iter()
                .for_each( |cc| {
                    cargo[s].push(cc.chars().nth(0).unwrap()) ;
                    s += 1 + cc.chars().filter(|ch| ch.is_whitespace()).count() / 4 ;
                })
            });

    (cargo , rearrangements
                .lines()
                .map(|r| r.split_whitespace().collect_vec().iter().filter_map(|s| s.parse().ok()).collect_tuple().unwrap())
                .collect_vec())
}

fn part_1(input : (Vec<String> , Vec<(usize, usize, usize)>)) -> String {
    solver(input, 3000)
}

fn part_2(input : (Vec<String> , Vec<(usize, usize, usize)>)) -> String {
    solver(input, 3001)
}

fn solver(input : (Vec<String> , Vec<(usize, usize, usize)>) , old_version : u16) -> String {
    let (mut cargo, rearrangements) = input ; 
    rearrangements
        .iter()
        .for_each(
            |(l,s,e)| {
                let to_push : String = match old_version {
                    3000 => cargo[s-1].drain(..l).rev().collect() ,
                    3001 => cargo[s-1].drain(..l).collect() ,
                    _ => unreachable!()
                };
                cargo[e-1].insert_str(0 , to_push.as_str()) ;
            });
    cargo
        .iter()
        .map(|c| c.chars().nth(0).unwrap())
        .join("")
}