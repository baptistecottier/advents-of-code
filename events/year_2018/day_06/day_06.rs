aoc::main!(); 


fn preprocessing(input: &str) -> (HashSet<(i16, i16)>, i16, i16, i16, i16) {
    input
    .lines()
    .map(|coord| coord.split_once(", ").unwrap())
    .map(|(x, y)| (x.parse().unwrap(), y.parse().unwrap()))
    .fold((HashSet::<(i16, i16)>::new(), 500, 0, 500, 0), |(mut coord, nx, xx, ny, xy), (x, y)|{
        coord.insert((x, y));
        (coord, nx.min(x), xx.max(x), ny.min(y), xy.max(y))})
}


fn part_1((coordinates, nx, xx, ny, xy): (HashSet<(i16, i16)>, i16, i16, i16, i16)) -> usize {
    *iproduct!((nx..=xx), (ny..=xy))
    .map(|(x, y)| 
        coordinates
        .iter()
        .min_set_by_key(|&&(cx, cy)| (cx - x).abs() + (cy - y).abs())
        .into_iter()
        .exactly_one()
        .unwrap_or(&&(0, 0)))
    .counts()
    .iter()
    .filter(|((x, y), _)| 
        ![(nx, ny), (nx, xy), (xx, ny), (xx, xy)]
        .iter()
        .map(|(cx, cy)| coordinates.iter().min_by_key(|(tx, ty)| (tx - cx).abs() + (ty - cy).abs()).unwrap())
        .contains(&(*x, *y)))
    .max_by_key(|cnt| cnt.1)
    .unwrap()
    .1
}

fn part_2((coordinates, nx, xx, ny, xy): (HashSet<(i16, i16)>, i16, i16, i16, i16)) -> usize {
    iproduct!((nx..=xx), (ny..=xy))
    .map(|(x, y)| 
        coordinates
        .iter()
        .map(|(cx, cy)| (cx - x).abs() + (cy - y).abs())
        .sum())
    .filter(|size: &i16| *size < 10_000) 
    .count()
}
