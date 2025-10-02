aoc::main!();

fn preprocessing(input: &str) -> i32 {
    input.parse().unwrap()
}

fn part_1(square_position: i32) -> i32 {
    let circle_index = (1.0 + ((square_position - 1) as f32).sqrt() / 2.0) as i32;
    circle_index + (square_position - 1) % circle_index
}

fn part_2(square_position: i32) -> i32 {
    let (mut x, mut y) = (0, 0);
    let mut memory: HashMap<(i32, i32), i32> = HashMap::new();
    let (mut dx, mut dy) = (0, -1);
    let mut value = 1;
    let turn = HashMap::from([
        ((1, 0), (0, 1)),
        ((0, 1), (-1, 0)),
        ((-1, 0), (0, -1)),
        ((0, -1), (1, 0)),
    ]);
    while value < square_position {
        let (tx, ty) = turn[&(dx, dy)];
        memory.insert((x, y), value);
        if !memory.contains_key(&(x + tx, y + ty)) {
            (dx, dy) = (tx, ty)
        };
        (x, y) = (x + dx, y + dy);
        value = iproduct!(x - 1..x + 2, y - 1..y + 2)
            .map(|(a, b)| memory.get(&(a, b)).unwrap_or(&0))
            .sum::<i32>();
    }
    value
}
