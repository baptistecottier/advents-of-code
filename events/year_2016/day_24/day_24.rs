aoc::main!();

fn preprocessing(puzzle_input: &str) -> Vec<(usize, usize)> {
    let mut coordinates: HashMap<u32, (usize, usize)> = HashMap::new();
    let mut grid: HashSet<(usize, usize)> = HashSet::new();

    puzzle_input.lines().enumerate().for_each(|(y, line)| {
        line.chars().enumerate().for_each(|(x, c)| {
            if c != '#' {
                grid.insert((x, y));
            }
            if c.is_ascii_digit() {
                coordinates.insert(c.to_digit(10).unwrap(), (x, y));
            }
        })
    });

    let n = coordinates.keys().copied().max().unwrap() as usize + 1;
    let mut coords_vec = vec![(0, 0); n];
    for (&label, &pos) in coordinates.iter() {
        coords_vec[label as usize] = pos;
    }

    
    let mut dist = vec![vec![0usize; n]; n];

    for i in 0..n {
        for j in (i + 1)..n {
            let start = coords_vec[i];
            let goal = coords_vec[j];

            let d = bfs(
                &start,
                |&(x, y)| {
                    [
                        (x + 1, y),
                        (x.saturating_sub(1), y),
                        (x, y.saturating_sub(1)),
                        (x, y + 1),
                    ]
                    .iter()
                    .filter(|&pos| grid.contains(pos))
                    .copied()
                    .collect::<Vec<_>>()
                },
                |&p| p == goal,
            )
            .unwrap()
            .len()
                - 1;

            dist[i][j] = d;
            dist[j][i] = d;
        }
    }

    (1..n)
        .permutations(n - 1)
        .map(|mut route| {
            route.insert(0, 0);
            let trip: usize = route.windows(2).map(|w| dist[w[0]][w[1]]).sum();
            let back: usize = dist[*route.last().unwrap()][0];
            (trip, back)
        })
        .collect::<Vec<_>>()
}

fn part_1(path_lengths: Vec<(usize, usize)>) -> usize {
    path_lengths
        .iter()
        .map(|(trip, _)| *trip)
        .min()
        .unwrap_or(0)
}

fn part_2(path_lengths: Vec<(usize, usize)>) -> usize {
    path_lengths
        .iter()
        .map(|(trip, back)| trip + back)
        .min()
        .unwrap_or(0)
}
