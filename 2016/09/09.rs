aoc2016::main!();

fn generator(input: &str) -> &str {
    input
}

fn part_1(input: &str) -> usize {
    solver(input, |c| c.len())
}

fn part_2(input: &str) -> usize {
    solver(input, part_2)
}

fn solver(input: &str, func : impl Fn(&str) -> usize) -> usize {
    let d = &input.splitn(4, &['(','x',')']).collect_vec();
    match d.len() {
        1 => input.len() ,
        4 => { 
            let (previous, width, rep, next) = (d[0],d[1].parse::<usize>().unwrap(), d[2].parse::<usize>().unwrap(),d[3]) ;
            previous.len() + solver(&next[width..], func) + rep * func(&next[..width]) 
        },
        _ => unreachable!()
    }
}