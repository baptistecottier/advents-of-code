aoc::main!();

fn preprocessing(input: &str) -> Vec<(u16, u16, u16, u16, u16)> {
    input
        .lines()
        .map(|claim| {
            claim
                .split(&['#', ' ', ',', ':', 'x'])
                .map(|n| n.parse().ok())
                .flatten()
                .collect_tuple()
                .unwrap()
        })
        .collect_vec()
}

fn part_1(claims: Vec<(u16, u16, u16, u16, u16)>) -> usize {
    claims
        .iter()
        .map(|&(_, x, y, dx, dy)| iproduct!((x..dx + x), (y..y + dy)))
        .flatten()
        .counts()
        .into_values()
        .filter(|&n| n > 1)
        .count()
}

fn part_2(claims: Vec<(u16, u16, u16, u16, u16)>) -> u16 {
    claims
        .iter()
        .find(|(id, x, y, dx, dy)| {
            claims
                .iter()
                .filter(|&(idd, ..)| id != idd)
                .all(|&(_, a, b, da, db)| a + da < *x || a > x + dx || b + db < *y || b > y + dy)
        })
        .unwrap()
        .0
}
