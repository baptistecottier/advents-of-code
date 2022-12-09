
aoc_2015::main!();

fn generator(input: &str) -> Vec<u16> {
    input
        .lines()
        .map(|l| l.rsplitn(2,' ').collect_vec())
        .map(|l| {
            l[0].parse::<u16>().unwrap()
        })
        .collect()
}

fn part_1(input: Vec<u16>) -> u16 {
    solve(input,1)
    }

fn part_2(input: Vec<u16>) -> u16 {
    solve(input.clone(), -1)
    }

fn solve(input: Vec<u16>, polarity : i16) -> u16 {
    let c = ((2*input.len()) as f64).sqrt() as usize + 1 ;
    (0..c)
        .permutations(c)
        .into_iter()
        .map(|perm| 
            perm
            .iter()
            .tuple_windows()
            .fold(0, |acc, (a,b)| {
                let n = if a < b { a } else { b };
                let x = a + b - 2 * n - 1;
                let index =  n * (2 * c - n - 1)/ 2 + x  ;
                acc + input[index]
            })
        )
        .sorted_by_key(|d| polarity * (*d as i16) )
        .nth(0)
        .unwrap()

}