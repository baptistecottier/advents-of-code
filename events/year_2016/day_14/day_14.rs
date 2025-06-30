aoc::main!(); 
use md5;

fn preprocessing(input: &str) -> &str {
    input
}

fn part_1(salt: &str) -> usize {
    solver(salt, 0)
}

fn part_2(salt: &str) -> usize {
    solver(salt, 2016)
}


fn solver(salt: &str, rec: usize) -> usize {
    (1..)
    .map(|n| (n, (0..rec).fold(format!("{:x}", md5::compute(format!("{}{}", salt, n))), |h, _| format!("{:x}", md5::compute(h)))))
    .map(|(n, h)| (n, h.chars().tuple_windows::<(_,_,_,_,_)>().find(|(a, b, c, d, e)| [a, b, c, d, e].iter().all_equal())))
    .filter(|(_, h)| ! h.is_none())
    .map(|(n, h)| (n, h.unwrap().0))
    .map(|(n, c)| (n-1001.min(n) .. n)
        .map(|nn| (nn, 
            (0..rec)
            .fold(format!("{:x}", md5::compute(format!("{}{}", salt, nn))), |h, _| format!("{:x}", md5::compute(h)))))
        .map(|(nn, hh)| 
            (nn, hh
            .chars()
            .tuple_windows::<(_,_,_)>()
            .find(|(a, b, c)| a == b && b ==c)))
        .filter(|(_, hh)| ! hh.is_none())
        .map(|(nn, hh)| (nn, hh.unwrap().0))
        .filter(|(_, cc)| *cc == c)
        .map(|(nn, _)| nn)
        .collect_vec())
    .flatten()
    .take(70)
    .sorted()
    .dedup()
    .nth(63)
    .unwrap()
}