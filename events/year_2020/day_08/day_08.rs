aoc::main!(); 

fn preprocessing(input: &str) -> Vec<(i32, i32)> {
    input
    .lines()
    .map(|instruction| instruction.split_once(" ").unwrap())
    .map(|(inst, step)| 
        (
            match inst {
                "nop" => 0,
                "acc" => 1,
                "jmp" => 2,
                _     => unreachable!()
            }
        ,
            step.parse().unwrap()
        ))
    .collect_vec()
}


fn part_1(program: Vec<(i32, i32)>) -> i32 {
    solver(program, -1).0
}


fn part_2(program: Vec<(i32, i32)>) -> i32 {
    (0..program.len())
    .map(|n| solver(program.clone(), n as i32))
    .take_while_inclusive(|(_, index)| (*index as usize + 1) < program.len())
    .last()
    .unwrap()
    .0
}


fn solver(program: Vec<(i32, i32)>, to_modify: i32) -> (i32, i32) {
    let mut visited: HashSet<i32> = HashSet::new();
    successors(Some((0, 0 as i32)), |(acc, index)|{
        let (mut inst, val) = program[*index as usize];
        if *index == to_modify {inst = 2 - inst};
        match inst {
            0 => Some((*acc      , *index + 1  )),
            1 => Some((*acc + val, *index + 1  )),
            2 => Some((*acc      , *index + val)),
            _ => unreachable!()}})
    .take_while_inclusive(|(_, index)| 
        (*index as usize + 1) < program.len() && visited.insert(*index))
    .last()
    .unwrap()
}

