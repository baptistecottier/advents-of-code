aoc::main!();

fn preprocessing(puzzle_input: &str) -> Vec<(&str, i32, i32)> {
    puzzle_input
        .lines()
        .map(|line| line.split_once(' ').unwrap())
        .map(|(f, args)| (f, args.split_once(", ").unwrap_or_else(|| (args, "0"))))
        .map(|(f, (reg, offset))| {
            (
                f,
                match reg {
                    "a" => 0,
                    "b" => 1,
                    _ => reg.parse().unwrap(),
                },
                offset.parse().unwrap(),
            )
        })
        .collect_vec()
}

fn part_1(program: Vec<(&str, i32, i32)>) -> u32 {
    run_program(program, 0)
}

fn part_2(program: Vec<(&str, i32, i32)>) -> u32 {
    run_program(program, 1)
}

fn run_program(program: Vec<(&str, i32, i32)>, reg_a: u32) -> u32 {
    *(0..)
        .fold_while((0, [reg_a, 0]), |(mut i, mut reg), _| {
            let (f, r, offset) = program[i];
            match f {
                "hlf" => reg[r as usize] = reg[r as usize] / 2,
                "tpl" => reg[r as usize] = reg[r as usize] * 3,
                "inc" => reg[r as usize] = reg[r as usize] + 1,
                "jmp" => i = (i as i32 + r - 1) as usize,
                "jie" => {
                    if reg[r as usize].is_even() {
                        i = (i as i32 + offset - 1) as usize;
                    }
                }
                "jio" => {
                    if reg[r as usize] == 1 {
                        i = (i as i32 + offset - 1) as usize;
                    }
                }
                _ => unreachable!(),
            };
            if i + 1 < program.len() {
                FoldWhile::Continue((i + 1, reg))
            } else {
                FoldWhile::Done((i, reg))
            }
        })
        .into_inner()
        .1
        .get(1)
        .unwrap()
}
