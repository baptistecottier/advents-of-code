aoc::main!();

fn preprocessing(input: &str) -> Vec<usize> {
    input
        .lines()
        .map(|l| {
            l.split(' ')
                .filter(|&w| ["microchip", "generator"].iter().any(|p| w.contains(p)))
                .count()
        })
        .collect_vec()
}

fn part_1(objects: Vec<usize>) -> usize {
    solver(objects, 0)
}

fn part_2(objects: Vec<usize>) -> usize {
    solver(objects, 4)
}

fn solver(objects: Vec<usize>, extra_parts: usize) -> usize {
    (1..4)
        .map(|n| 2 * (extra_parts + objects.iter().take(n).sum::<usize>()) - 3)
        .sum()
}
