aoc::main!(); 

fn preprocessing(input: &str) -> Vec<Vec<Vec<i64>>> {
    input
    .lines()
    .map(|story| story.split_whitespace().map(|n| n.parse::<i64>().unwrap()).collect_vec())
    .map(|story| 
        successors(Some(story), |line|
            Some(line
                .iter()
                .tuple_windows()
                .map(|(a, b)| b - a)
                .collect_vec()))
        .take_while(|line| line.into_iter().any(|n| *n != 0))
        .collect_vec())
    .collect_vec()
}

fn part_1(stories: Vec<Vec<Vec<i64>>>) -> i64 {
    stories
    .iter()
    .map(|story| story.iter().map(|s| s.iter().next_back().unwrap()).sum::<i64>())
    .sum::<i64>()
}

fn part_2(stories: Vec<Vec<Vec<i64>>>) -> i64 {
    stories
    .iter()
    .map(|story| 
        story
        .iter()
        .map(|s| s.iter().next().unwrap())
        .enumerate()
        .map(|(n, &v)| if n % 2 == 0 {v} else {-v})
        .sum::<i64>())
    .sum::<i64>()
}