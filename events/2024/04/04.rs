aoc::main!();

fn preprocessing(puzzle_input: &str) ->  HashMap<char,HashSet<(isize, isize)>> {
    let mut letters = HashMap::from([('X', HashSet::new()),('M', HashSet::new()),('A', HashSet::new()),('S', HashSet::new())]);
    puzzle_input
    .lines()
    .enumerate()
    .for_each(|(y, line)| {
        line.char_indices().for_each(|(x, c)| {
            let letter = letters.get_mut(&c).unwrap();
            letter.insert((x as isize, y as isize));
        });
    });
    letters
}

fn part_1(letters: HashMap<char,HashSet<(isize, isize)>>) -> usize {
    letters.get(&'X').unwrap()
    .iter()
    .map(|&(x, y)| 
        [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        .iter()
        .filter(|(dx, dy)|
            letters.get(&'M').unwrap().contains(&(x +     dx, y +     dy)) &&
            letters.get(&'A').unwrap().contains(&(x + 2 * dx, y + 2 * dy)) &&
            letters.get(&'S').unwrap().contains(&(x + 3 * dx, y + 3 * dy)))
        .count())
    .sum()
}

fn part_2(letters: HashMap<char,HashSet<(isize, isize)>>) -> usize {
    letters.get(&'A').unwrap()
    .iter()
    .filter(|&(x, y)| 
        [('M','S','M','S'), ('S','M','S','M'), ('M','M','S','S'), ('S','S','M','M')]
        .iter()
        .any(|l|
            letters.get(&l.0).unwrap().contains(&(x - 1, y - 1)) &&
            letters.get(&l.1).unwrap().contains(&(x + 1, y - 1)) &&
            letters.get(&l.2).unwrap().contains(&(x - 1, y + 1)) &&
            letters.get(&l.3).unwrap().contains(&(x + 1, y + 1))))
    .count()
}