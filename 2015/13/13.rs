aoc_2015::main!();

fn generator(input : &str) -> Vec<i16> {
    input
        .lines()
        .map(|l| l.split_whitespace().collect_vec())
        .map(|v| match v[2] {
            "gain" => v[3].parse::<i16>().unwrap(),
            "lose" => -v[3].parse::<i16>().unwrap(),
            _ => unreachable!(),
        })
        .collect_vec()
}


fn part_1(input: Vec<i16>) -> i16 {
    solve(input,1)
    }

fn part_2(input: Vec<i16>) -> i16 {
    solve(input,2)
    }

fn solve(input : Vec<i16>, part : usize) -> i16 {
    let c = ((input.len()) as f64).sqrt() as usize + part ;
    (0..c)
    .permutations(c)
    .into_iter()
    .map(|perm| {
        perm
            .iter()
            .cycle()
            .take(c+1)
            .into_iter()
            .tuple_windows()
            .fold(0, |acc, (&a,&b)| {
                if ![a,b].contains(&(c - part + 1))  {
                let index1 = (c-part) * a + b - (b > a) as usize;
                let index2 = (c-part) * b + a - (a > b) as usize;
                acc + input[index1] + input[index2]
            } else {
                acc
            }
            })}
    )
    .max()
    .unwrap()
}
