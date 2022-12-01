
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
    *solve(input)
            .iter()
            .min()
            .unwrap()
    }

fn part_2(input: Vec<u16>) -> u16 {
    *solve(input)
            .iter()
            .max()
            .unwrap()
    }

fn solve(input: Vec<u16>) -> Vec<u16>{
    let l = input.len(); 
    let c = ((2*l) as f64).sqrt() as usize + 1 ;
    (0..c)
        .permutations(c)
        .into_iter()
        .map(|perm| perm
                                .iter()
                                .tuple_windows()
                                .fold(0, |acc, (a,b)| {
                                    let n = if a < b { a } else { b };
                                    let x = a + b - 2 * n - 1;
                                    let index =  n * (2 * c - n - 1)/ 2 + x  ;
                                    acc + input[index]
                                })
        )
        .collect_vec()
}