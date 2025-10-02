aoc::main!();

fn preprocessing(puzzle_input: &str) -> (HashSet<(i32, i32)>, (i32, i32), (i32, i32)) {
    let mut kiosk = HashSet::new();
    let mut start = (0, 0);
    let mut end = (0, 0);

    for (y, line) in puzzle_input.lines().enumerate() {
        for (x, c) in line.chars().enumerate() {
            match c {
                '#' => {
                    kiosk.insert((x as i32, y as i32));
                }
                'S' => {
                    start = (x as i32, y as i32);
                }
                'E' => {
                    end = (x as i32, y as i32);
                }
                _ => {}
            }
        }
    }
    (kiosk, start, end)
}

fn part_1(kiosk: HashSet<(i32, i32)>, start: (i32, i32), end: (i32, i32)) -> i32 {
    let mut paths = VecDeque::new();
    paths.push_back(vec![(start, (1, 0), 0)]);
    let mut scores = HashMap::new();
    let mut best_paths_tiles = HashSet::new();
    let mut lowest_score = 1_000_000;

    while let Some(path) = paths.pop_front() {
        let ((x, y), (dx, dy), path_score) = path.last().unwrap();
        if (*x, *y) == end {
            if *path_score == lowest_score {
                for (pos, _, _) in &path {
                    best_paths_tiles.insert(*pos);
                }
            } else if *path_score < lowest_score {
                best_paths_tiles.clear();
                for (pos, _, _) in &path {
                    best_paths_tiles.insert(*pos);
                }
                lowest_score = *path_score;
            }
        } else {
            for (vx, vy) in [(dx, dy), (-dy, dx), (dy, -dx)] {
                let pos = (x + vx, y + vy);
                let pos_score = *scores.get(&pos).unwrap_or(&1_000_000);
                if *path_score < pos_score + 1_000 && !kiosk.contains(&pos) {
                    let delta = if vx == *dx { 1 } else { 1_001 };
                    let mut new_path = path.clone();
                    new_path.push((pos, (vx, vy), path_score + delta));
                    paths.push_back(new_path);
                    scores.insert(pos, pos_score.min(path_score + delta));
                }
            }
        }
    }
    lowest_score
}

fn part_2(kiosk: HashSet<(i32, i32)>, start: (i32, i32), end: (i32, i32)) -> usize {
    let mut paths = VecDeque::new();
    paths.push_back(vec![(start, (1, 0), 0)]);
    let mut scores = HashMap::new();
    let mut best_paths_tiles = HashSet::new();
    let mut lowest_score = 1_000_000;

    while let Some(path) = paths.pop_front() {
        let ((x, y), (dx, dy), path_score) = path.last().unwrap();
        if (*x, *y) == end {
            if *path_score == lowest_score {
                for (pos, _, _) in &path {
                    best_paths_tiles.insert(*pos);
                }
            } else if *path_score < lowest_score {
                best_paths_tiles.clear();
                for (pos, _, _) in &path {
                    best_paths_tiles.insert(*pos);
                }
                lowest_score = *path_score;
            }
        } else {
            for (vx, vy) in [(dx, dy), (-dy, dx), (dy, -dx)] {
                let pos = (x + vx, y + vy);
                let pos_score = *scores.get(&pos).unwrap_or(&1_000_000);
                if *path_score < pos_score + 1_000 && !kiosk.contains(&pos) {
                    let delta = if vx == *dx { 1 } else { 1_001 };
                    let mut new_path = path.clone();
                    new_path.push((pos, (vx, vy), path_score + delta));
                    paths.push_back(new_path);
                    scores.insert(pos, pos_score.min(path_score + delta));
                }
            }
        }
    }
    best_paths_tiles.len()
}
