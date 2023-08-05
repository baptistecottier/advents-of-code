aoc::main!();

fn preprocessing(input: &str) -> &str {
    input
}

fn part_1(file: &str) -> usize {
    solver(file, |c| c.len())
}

fn part_2(file: &str) -> usize {
    solver(file, part_2)
}

fn solver(file: &str, func : impl Fn(&str) -> usize) -> usize {
    let d = &file.splitn(4, &['(','x',')']).collect_vec();

    match d.len() {
        1 => file.len() ,
        4 => { 
            let (previous, width, rep, next) = (d[0],d[1].parse::<usize>().unwrap(), d[2].parse::<usize>().unwrap(),d[3]) ;
            rep * func(&next[..width]) + previous.len() + solver(&next[width..], func)},
        _ => unreachable!()}
}