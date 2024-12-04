aoc::main!();


//     Preprocessing consists in going through the puzzle input 
//     and stock position of the letters 'X', 'M', 'A' and 'S'.
fn preprocessing(puzzle_input: &str) ->  HashMap<char,HashSet<(isize, isize)>> {
    let mut letters = HashMap::from([
                       ('X', HashSet::new()), ('M', HashSet::new()),
                       ('A', HashSet::new()), ('S', HashSet::new())]);
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


//     Patterns to be detected are:
//     XMAS    X...    X...    ...X    SAMX    S...    S...    ...S
//     ....    .M..    M...    ..M.    ....    .A..    A...    ..A.
//     ....    ..A.    A...    .A..    ....    ..M.    M...    .M..
//     ....    ...S    S...    S...    ....    ...X    X...    X...
//     This function starts from every detected 'X' then check if a 
//     "MAS" is formed in any of the possible directions
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


//     Patterns to be detected are:
//     M.S     S.M     M.M     S.S
//     .A.     .A.     .A.     .A.
//     M.S     S.M     S.S     M.M
//     
//     Readind left-to-right, top-to-bottom without considering the 'A', 
//     the patterns are "MSMS", "SMSM", "MMSS" and "SSMM".
//     This function therefore look for this patterns around all 'A'. 
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