aoc2022::main!(); 

fn generator(input : &str) -> (Vec<(u64, usize)>, Vec<[u64; 3]>, Vec<Vec<u64>>){
    let mut starting_items = Vec::new();
    let mut ops = Vec::new();
    let mut pred = Vec::new();
    input.split("\n\n")
    .enumerate()
    .for_each(|(i ,monkey)| {
        let details = monkey.split('\n').skip(1).collect_vec() ;
        starting_items.append(&mut details[0].trim().replace(", "," ").split(' ').skip(2).map(|n| (n.parse::<u64>().unwrap(),i)).collect_vec());
        ops.append(&mut match details[1].split("= old ").nth(1).unwrap().split(' ').collect_vec()[..2] {
            ["*", "old"] => [[0,0,1]].to_vec(),
            ["*", n] =>[ [0, n.parse().unwrap(), 0]].to_vec(),
            ["+", n] => [[n.parse().unwrap(), 1, 0]].to_vec(),
            _ => unreachable!(),
        });
        pred.append(&mut [(2..5).map(|n| details[n].rsplitn(2, ' ').nth(0).unwrap().parse::<u64>().unwrap()).collect_vec()].to_vec());
    });
    (starting_items, ops, pred)
}

fn part_1(input : (Vec<(u64, usize)>, Vec<[u64; 3]>, Vec<Vec<u64>>)) -> u64 {
    solver(input, 20, 3)
}

fn part_2(input : (Vec<(u64, usize)>, Vec<[u64; 3]>, Vec<Vec<u64>>)) -> u64 {
    solver(input, 10_000, 1)

}

fn solver(input : (Vec<(u64, usize)>, Vec<[u64; 3]>, Vec<Vec<u64>>), rounds : usize, div : u64 ) -> u64 {
    let (items, ops, preds) = input ;
    let modulo = preds.iter().map(|p| p[0]).product::<u64>();
    let mut inspected_items = [0 ; 8];
    items
        .iter()
        .for_each(|&(mut v, mut new_monkey)| {
            (0..rounds)
                .for_each(|_| {
                    let mut old_monkey = 0 ; 
                    while new_monkey >= old_monkey {
                        let [add, mul, sq] = ops[new_monkey];
                        let pred = &preds[new_monkey];
                        inspected_items[new_monkey] += 1;
                        v = (((v * mul + sq * v * v) + add) / div) % (div * modulo) ;
                        old_monkey = new_monkey ;
                        new_monkey = pred[1 + ((v % pred[0]) != 0) as usize] as usize;
                    }
                }
            )
        });
    inspected_items.iter().sorted().rev().take(2).product()
}