aoc::main!();

fn preprocessing(input: &str) -> Vec<bool> {
    input.chars().map(|b| b == '1').collect()
}

fn part_1(state: Vec<bool>) -> String {
    solver(state, 272)
}

fn part_2(state: Vec<bool>) -> String {
    solver(state, 35651584)
}

fn solver(state: Vec<bool>, disk_length: usize) -> String {
    (0..)
        .fold_while(
            (0..)
                .fold_while(state, |memory, _| {
                    if memory.len() > disk_length {
                        FoldWhile::Done(memory[..disk_length].to_vec())
                    } else {
                        FoldWhile::Continue(
                            [
                                memory.clone(),
                                [false].to_vec(),
                                memory.iter().rev().map(|b| !b).collect_vec(),
                            ]
                            .concat(),
                        )
                    }
                })
                .into_inner(),
            |memory, _| {
                if memory.len() % 2 == 1 {
                    FoldWhile::Done(memory)
                } else {
                    FoldWhile::Continue(
                        memory
                            .chunks(2)
                            .map(|chunk| !chunk[0] ^ chunk[1])
                            .collect_vec(),
                    )
                }
            },
        )
        .into_inner()
        .iter()
        .map(|&b| if b { '1' } else { '0' })
        .join("")
}
