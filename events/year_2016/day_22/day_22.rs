aoc::main!();

#[derive(Clone, Debug, PartialEq, Eq)]
struct Node {
    x: i32,
    y: i32,
    size: i32,
    used: i32,
    available: i32,
}

impl Node {
    fn is_viable_with(&self, b: &Node) -> bool {
        self != b && self.used > 0 && self.used <= b.available
    }

    fn manhattan(&self) -> i32 {
        self.x.abs() + self.y.abs()
    }

    fn distance_with(&self, x2: i32, y2: i32) -> i32 {
        (self.x - x2).abs() + (self.y - y2).abs()
    }
}

fn preprocessing(puzzle_input: &str) -> Vec<Node> {
    puzzle_input
    .lines()
    .skip(2)
    .map(
        |entry| {
            let (x, y, z, w, t) = scan_fmt!(entry, "/dev/grid/node-x{}-y{} {}T {}T {}T {}%", i32, i32, i32, i32, i32).unwrap();
            Node { x, y, size: z, used: w, available: t }
        }
    )
    .collect()
}

fn part_1(nodes: Vec<Node>) -> usize {
    nodes
        .iter()
        .cartesian_product(nodes.iter())
        .filter(|(a, b)| a.is_viable_with(b))
        .count()
}

fn part_2(nodes: Vec<Node>) -> i32 {
    let walls = nodes
        .iter()
        .filter(|n| n.used > 100)
        .collect_vec();

    let empty_node = nodes.iter().find(|n| n.used == 0).unwrap();
    let pt_min = walls.iter().min_by_key(|n| n.manhattan()).unwrap();

    let wall = if pt_min.x != 0  {
        (pt_min.x - 1, pt_min.y)
    } else {
        let wall = walls.iter().max_by_key(|n| n.manhattan()).unwrap();
        (wall.x + 1, wall.y)
    };

    let width = nodes.iter().max_by_key(|n| n.x).unwrap().x;

    empty_node.distance_with(wall.0, wall.1) 
        + (wall.0 - width).abs() 
        + wall.1 
        + 5 * (width - 1)
}