aoc::main!();

fn preprocessing(puzzle_input: &str) -> Vec<(&str, i16, &str, fn(&i16, &i16) -> bool, i16)> {
    puzzle_input
    .lines()
    .map(|instruction| instruction.split_whitespace().collect_vec())
    .map(|args| (
        args[0], 
        if args[1] == "inc" {args[2].parse().unwrap()}
        else {- args[2].parse::<i16>().unwrap()},
        args[4],
        match args[5] {
            ">"     => i16::gt,
            "<"     => i16::lt,
            ">="    => i16::ge,
            "<="    => i16::le,
            "=="    => i16::eq,
            "!="    => i16::ne,
            _       => unreachable!()
        },
        args[6].parse().unwrap()))
    .collect_vec()
}

fn part_1(instructions: Vec<(&str, i16, &str, fn(&i16, &i16) -> bool, i16)>) -> i16 {
    *solver(instructions)
    .0
    .values()
    .max()
    .unwrap()
}

fn part_2(instructions: Vec<(&str, i16, &str, fn(&i16, &i16) -> bool, i16)>) -> i16 {
    solver(instructions)
    .1
}

fn solver<'a>(instructions: Vec<(&'a str, i16, &'a str, fn(&i16, &i16) -> bool, i16)>) -> (HashMap<&'a str, i16>, i16) {    instructions
    .iter()
    .fold((HashMap::new(), 0), |(mut acc, mut m), (ra, na, rb, f, nb)| {
            if f(acc.get(rb).unwrap_or(&0), nb) {
                m = m.max(acc.insert(ra, acc.get(ra).unwrap_or(&0) + na).unwrap_or(0))};
            (acc, m) })
}