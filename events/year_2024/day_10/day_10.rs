use grid::Grid;

aoc::main!();

fn preprocessing(input: &str) -> Vec<HashMap<(usize, usize), u32>> {
    let width = input.find('\n').unwrap();

    let grid = Grid::from_vec(
        input.chars().filter_map(|c| c.to_digit(10)).collect_vec(),
        width,
    );

    let starts = grid
        .indexed_iter()
        .filter(|&(_, value)| *value == 0)
        .map(|(pos, _)| pos)
        .collect_vec();

    cnt_hiking_trails(starts, grid)
}


fn part_1(hiking_trails: Vec<HashMap<(usize, usize), u32>>) -> usize {
    hiking_trails.iter().map(|hm| hm.len()).sum()
}


fn part_2(hiking_trails: Vec<HashMap<(usize, usize), u32>>) -> u32 {
    hiking_trails
        .iter()
        .map(|hm| hm.values().sum::<u32>())
        .sum()
}


fn cnt_hiking_trails(
    starts: Vec<(usize, usize)>,
    grid: Grid<u32>,
) -> Vec<HashMap<(usize, usize), u32>> {
    let neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)];

    starts
        .iter()
        .map(|&start| {
            let mut hiking_trails = HashMap::new();
            let mut queue = VecDeque::from([start]);

            while !queue.is_empty() {
                let (x, y) = queue.pop_back().unwrap();
                let value = grid.get(x, y).unwrap();
                for (dx, dy) in neighbours {
                    let (x2, y2) = (x.saturating_add_signed(dx), y.saturating_add_signed(dy));
                    if let Some(&n) = grid.get(x2, y2) {
                        if n == value + 1 {
                            if n == 9 {
                                let score = hiking_trails.entry((x2, y2)).or_insert(0);
                                *score += 1;
                            } else {
                                queue.push_back((x2, y2));
                            }
                        }
                    }
                }
            }
            hiking_trails
        })
        .collect_vec()
}
