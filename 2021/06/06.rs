aoc::main!(); 

fn preprocessing(input: &str) -> Vec<usize> {
    input
    .split(',')
    .counts()
    .into_iter()
    .sorted()
    .map(|(_, cnt)| cnt)
    .pad_using(9, |_| 0)
    .collect_vec()
}

fn part_1(lanternfishes: Vec<usize>) -> usize {
    get_lf_qty_after_n_days(lanternfishes, 80)
}
 
fn part_2(lanternfishes: Vec<usize>) -> usize {
    get_lf_qty_after_n_days(lanternfishes, 256)
}

fn get_lf_qty_after_n_days(lanternfishes: Vec<usize>, days: usize) -> usize {
    (0..days)
    .fold(lanternfishes, |mut lf, _| {
        lf.rotate_left(1);
        lf[5] += lf[7];
        lf})
    .iter()
    .sum()
}
