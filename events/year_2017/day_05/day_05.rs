aoc::main!();

fn preprocessing(input: &str) -> Vec<isize> {
    input
        .lines()
        .map(|line| line.parse().unwrap())
        .collect_vec()
}

fn part_1(mut offsets: Vec<isize>) -> usize {
    (0..)
        .fold_while(0, |mut acc, n| {
            offsets[acc] += 1;
            acc = (acc as isize + offsets[acc] - 1) as usize;
            if acc >= offsets.len() {
                FoldWhile::Done(n)
            } else {
                FoldWhile::Continue(acc)
            }
        })
        .into_inner()
        + 1
}

fn part_2(mut offsets: Vec<isize>) -> usize {
    (0..)
        .fold_while(0, |mut acc, n| {
            if offsets[acc] < 3 {
                offsets[acc] += 1;
                acc = (acc as isize + offsets[acc] - 1) as usize;
            } else {
                offsets[acc] -= 1;
                acc = (acc as isize + offsets[acc] + 1) as usize;
            }

            if acc >= offsets.len() {
                FoldWhile::Done(n)
            } else {
                FoldWhile::Continue(acc)
            }
        })
        .into_inner()
        + 1
}
