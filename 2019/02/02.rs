aoc2019::main!(); 

fn generator(input: &str) -> Vec<usize> {
    input
    .split(',')
    .map(|n| n.parse().unwrap())
    .collect_vec()
}

fn part_1(mut input: Vec<usize>) -> usize {
    (0..)
    .map(|n| (input[4 * n], input[4 * n + 1], input[4 * n + 2], input[4 * n + 3]))
    .to_owned()
    .for_each(|(a,b,c,d)| 
        match a {
            1 => input[d] = input[b] + input[c],
            2 => input[d] = input[b] * input[c],
            99 => return input[0],
            _ => unreachable!()
        });
    input[0]
}

fn part_2(input: Vec<usize>) -> usize {
    println!("{:?}", input);
    2
}