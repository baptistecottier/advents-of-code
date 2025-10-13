aoc::main!();

fn preprocessing(puzzle_input: &str) -> Vec<Vec<i32>> {
    puzzle_input
        .lines()
        .map(|report| {
            report
                .split_whitespace()
                .map(|level| level.parse().unwrap())
                .collect_vec()
        })
        .collect_vec()
}

fn part_1(reports: Vec<Vec<i32>>) -> usize {
    reports
        .iter()
        .filter(|report| is_report_safe(report))
        .count()
}

fn part_2(reports: Vec<Vec<i32>>) -> usize {
    reports
        .iter()
        .filter(|report| {
            (0..report.len()).any(|i| is_report_safe(&[&report[..i], &report[i + 1..]].concat()))
        })
        .count()
}

fn is_report_safe(report: &Vec<i32>) -> bool {
    report
        .iter()
        .tuple_windows()
        .map(|(level_a, level_b)| level_a - level_b)
        .map(|diff| {
            if (diff.abs() > 0) && (diff.abs() < 4) {
                diff.signum()
            } else {
                random()
            }
        })
        .all_equal()
}
