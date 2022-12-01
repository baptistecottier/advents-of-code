aoc2016::main!();

fn generator(input : &str) -> Vec<Vec<i16>> {
    let mut position = vec![0,0] ; 
    let mut direction = (0,1) ;
    input
        .split(", ")
        .map(|i| {
            let mut chars = i.chars() ;
            (chars.next().unwrap() , chars.as_str().parse::<u16>().unwrap())
        })
        .map(|(turn, d)| match turn {
            'R' => { direction = turn_right(direction);
                    (direction , d)},
            'L' => { direction = turn_left(direction);
                    (direction , d)},
            _ => unreachable!()})
        .map(move |((x ,y), l)| (0..l)
                            .map(|_| 
                                {
                                position[0] += x ;
                                position[1] += y ;
                                position.clone()
                                }
                            )
                            .collect_vec())
        .flatten()
        .collect_vec()
}

fn part_1(input : Vec<Vec<i16>> ) -> i16 {
    input
        .iter()
        .next_back()
        .unwrap()
        .iter()
        .map(|x| x.abs())
        .sum()
    }

fn part_2(input : Vec<Vec<i16>> ) -> i16 {
   input
        .iter()
        .find(|pos| input.clone().iter().filter(|x| x==pos).count() > 1)
        .unwrap()
        .iter()
        .map(|x| x.abs())
        .sum()
    }

fn turn_left(input : (i16, i16)) -> (i16, i16) {
    match input {
        (-1,0) => (0,-1),
        (0,1)  => (-1,0),
        (1,0)  => (0,1),
        (0,-1) => (1,0),
        _ => unreachable!()
    }
}

fn turn_right(input : (i16, i16)) -> (i16, i16) {
    match input {
        (-1,0) => (0,1),
        (0,1)  => (1,0),
        (1,0)  => (0,-1),
        (0,-1) => (-1,0),
        _ => unreachable!()
    }
}