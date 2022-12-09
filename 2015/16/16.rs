aoc_2015::main!();

fn generator(input : &str) -> Vec<[u32 ; 10]> {
    let mut aunts_sue = [[0,0,0,0,1000,0,1000,0,0,0] ; 500];
    input
        .lines()
        .map(|l| l.split([':',',',' ']).collect_vec())
        .enumerate()
        .for_each(|(aunt,v)| {
                        [3,7,11].iter()
                        .for_each(|i| match v[*i] {
                            "akitas" => aunts_sue[aunt][0] = v[i+2].parse().unwrap() ,
                            "cars" => aunts_sue[aunt][1] = v[i+2].parse().unwrap(),
                            "cats" => aunts_sue[aunt][2] = v[i+2].parse().unwrap(),
                            "children" => aunts_sue[aunt][3] = v[i+2].parse().unwrap(),
                            "goldfish" => aunts_sue[aunt][4] = v[i+2].parse().unwrap(),
                            "perfumes" => aunts_sue[aunt][5] = v[i+2].parse().unwrap(),
                            "pomeranians" => aunts_sue[aunt][6] = v[i+2].parse().unwrap(),
                            "samoyeds" => aunts_sue[aunt][7] = v[i+2].parse().unwrap(),
                            "trees" => aunts_sue[aunt][8] = v[i+2].parse().unwrap(),
                            "vizslas" => aunts_sue[aunt][9] = v[i+2].parse().unwrap(),
                            _ => unreachable!(),
                        })
                    }) ;
        aunts_sue.into()
}

fn part_1(input : Vec<[u32 ; 10]>) -> usize {
    solver(input, false)
}

fn part_2(input : Vec<[u32 ; 10]>) -> usize {
    solver(input, true)
}

fn solver(input : Vec<[u32 ; 10]>, ranges : bool) -> usize {
    input
        .iter()
        .find_position(|v| 
            [v[0] == 0, v[1] == 2, v[3] == 3, v[5] == 1,  v[7] == 2 , v[9] == 0].into_iter().filter(|b| *b).count()+
            if ranges == true {[v[2] > 7, v[4] < 5,v[6] < 3 , v[8] > 3].into_iter().filter(|b| *b).count()} 
            else {[v[2] == 7, v[4] == 5,v[6] == 3 , v[8] == 3].into_iter().filter(|b| *b).count()} > 4)
        .map(|(pos,_)| pos + 1)
        .unwrap()
        }