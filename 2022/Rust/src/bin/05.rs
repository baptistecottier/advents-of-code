aoc2022::main!(); 

fn generator(input : &str) -> (Vec<String> , Vec<(usize, usize, usize)>) {
    let (a, r) = input
        .split("\n\n")
        .collect_tuple().unwrap() ; 
    
    let rearrangements = 
        r
            .lines()
            .map(|r| {
                let rr =r.split_whitespace().collect_vec() ;
                (rr[1].parse::<usize>().unwrap(), rr[3].parse::<usize>().unwrap(), rr[5].parse::<usize>().unwrap())  
            })
            .collect_vec() ;
    let cargo_width : usize = a.trim_end().rsplit_once(' ').unwrap().1.parse().unwrap() ;
    let mut cargo = vec!["".to_string() ; cargo_width] ;
        a
            .lines()
            .for_each(| c | {
                let v = c.split('[').collect_vec() ; 
                let mut s = v[0].len() / 4 ;
                (v[1..])
                    .iter()
                    .for_each(|cc| {
                        cargo[s].push(cc.chars().nth(0).unwrap()) ;
                        s += 1 + (cc.chars().filter(|ch| ch.is_whitespace()).count() / 4) ;
                    })
            }) ;

    (cargo , rearrangements)
}

fn part_1(input : (Vec<String> , Vec<(usize, usize, usize)>)) -> String {
    solver(input, true)
}

fn part_2(input : (Vec<String> , Vec<(usize, usize, usize)>)) -> String {
    solver(input, false)
}

fn solver(input : (Vec<String> , Vec<(usize, usize, usize)>) , old_version : bool) -> String {
    let (mut cargo, rearrangements) = input ; 
    rearrangements
        .iter()
        .for_each(
            |(l,s,e)| {
                let mut to_push : String = cargo[s-1].drain(..l).collect() ;
                if old_version {to_push = to_push.chars().rev().join("")}
                cargo[e-1].insert_str(0 , to_push.as_str()) ;
            });
    cargo
        .iter()
        .map(|c| c.chars().nth(0).unwrap())
        .join("")
}