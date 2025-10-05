aoc::main!();

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
struct Pt {
    x: isize,
    y: isize,
}

#[derive(Clone, Debug, PartialEq, Eq, Hash)]
struct Guard {
    pos: Pt,
    d: Pt,
}

#[derive(Clone, Debug)]
struct Grid {
    obstacles: Vec<Pt>,
    width: isize,
    height: isize,
    visited: HashSet<Guard>,
}

impl Guard {
    fn proceed(&mut self, grid: &mut Grid) -> bool {
        while (0..grid.width).contains(&self.pos.x) && (0..grid.height).contains(&self.pos.y) {
            let mut candidate = Pt {
                x: self.pos.x + self.d.x,
                y: self.pos.y + self.d.y,
            };
            while grid.obstacles.contains(&candidate) {
                self.d = Pt {
                    x: -self.d.y,
                    y: self.d.x,
                };
                candidate = Pt {
                    x: self.pos.x + self.d.x,
                    y: self.pos.y + self.d.y,
                };
            }
            self.pos.x += self.d.x;
            self.pos.y += self.d.y;
            if grid.visited.contains(&self) {
                return true;
            } else {
                grid.visited.insert(self.clone());
            }
        }
        false
    }
}

fn preprocessing(puzzle_input: &str) -> (Guard, Grid) {
    let height = puzzle_input.lines().count() as isize;
    let width = (puzzle_input.len() as isize / (height - 1)) as isize - 1;
    let guard = puzzle_input.chars().find_position(|&c| c == '^').unwrap().0 as isize;

    let pos = Pt {
        x: (guard % width) as isize,
        y: (guard / width) as isize,
    };

    let guard = Guard {
        pos: pos.clone(),
        d: Pt { x: 0, y: -1 },
    };
    let grid = Grid {
        obstacles: puzzle_input
            .char_indices()
            .filter(|&(_, c)| c == '#')
            .map(|(n, _)| Pt {
                x: (n as isize % width) as isize,
                y: (n as isize / width),
            })
            .collect_vec(),
        width: width as isize,
        height: height as isize,
        visited: HashSet::from([guard.clone()]),
    };
    (guard, grid)
}

fn part_1(guard_data: (Guard, Grid)) -> usize {
    let (mut guard, mut grid) = guard_data;
    guard.proceed(&mut grid);
    grid.visited
        .iter()
        .map(|guard| guard.pos.clone())
        .unique()
        .count()
        - 1
}

fn part_2(guard_data: (Guard, Grid)) -> usize {
    let (guard, grid) = guard_data;
    let mut t_guard = guard.clone();
    let mut t_grid = grid.clone();
    t_guard.proceed(&mut t_grid);

    t_grid
        .clone()
        .visited
        .iter()
        .map(|v| v.pos)
        .unique()
        .filter(|v| {
            let mut test_grid = grid.clone();
            test_grid.obstacles.push(v.clone());
            guard.clone().proceed(&mut test_grid)
        })
        .count()
}
