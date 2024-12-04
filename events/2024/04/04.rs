aoc::main!();

fn preprocessing(puzzle_input: &str) ->  HashMap<char,HashSet<(isize, isize)>> {
    let mut letters = HashMap::from([('X', HashSet::new()),('M', HashSet::new()),('A', HashSet::new()),('S', HashSet::new())]);
    puzzle_input
    .lines()
    .enumerate()
    .for_each(|(y, line)| {
        line.char_indices().for_each(|(x, c)| {
            let temp = letters.get_mut(&c).unwrap();
            temp.insert((x as isize, y as isize));
        });
    });
    letters
}

fn part_1(letters: HashMap<char,HashSet<(isize, isize)>>) -> usize {
    letters.get(&'X').unwrap()
    .iter()
    .map(|&(x, y)| 
        // right
        ((letters.get(&'M').unwrap().contains(&(x+1, y)) &&
        letters.get(&'A').unwrap().contains(&(x+2, y)) &&
        letters.get(&'S').unwrap().contains(&(x+3, y))) as usize) +
        // left
        ((letters.get(&'M').unwrap().contains(&(x-1, y)) &&
        letters.get(&'A').unwrap().contains(&(x-2, y)) &&
        letters.get(&'S').unwrap().contains(&(x-3, y)))as usize) +
        // top
        ((letters.get(&'M').unwrap().contains(&(x, y-1)) &&
        letters.get(&'A').unwrap().contains(&(x, y-2)) &&
        letters.get(&'S').unwrap().contains(&(x, y-3))) as usize) +
        // bottom
        ((letters.get(&'M').unwrap().contains(&(x, y+1)) &&
        letters.get(&'A').unwrap().contains(&(x, y+2)) &&
        letters.get(&'S').unwrap().contains(&(x, y+3))) as usize) +
        // bottom right
        ((letters.get(&'M').unwrap().contains(&(x+1, y+1)) &&
        letters.get(&'A').unwrap().contains(&(x+2, y+2)) &&
        letters.get(&'S').unwrap().contains(&(x+3, y+3))) as usize) +
        // top right
        ((letters.get(&'M').unwrap().contains(&(x+1, y-1)) &&
        letters.get(&'A').unwrap().contains(&(x+2, y-2)) &&
        letters.get(&'S').unwrap().contains(&(x+3, y-3))) as usize) +
        // bottom left
        ((letters.get(&'M').unwrap().contains(&(x-1, y+1)) &&
        letters.get(&'A').unwrap().contains(&(x-2, y+2)) &&
        letters.get(&'S').unwrap().contains(&(x-3, y+3))) as usize) +
        // top left
        (((letters.get(&'M').unwrap().contains(&(x-1, y-1)) &&
        letters.get(&'A').unwrap().contains(&(x-2, y-2)) &&
        letters.get(&'S').unwrap().contains(&(x-3, y-3)))) as usize)
    )
    .sum()
}

fn part_2(letters: HashMap<char,HashSet<(isize, isize)>>) -> usize {
    letters.get(&'A').unwrap()
    .iter()
    .filter(|&(x, y)| 
        // right
        (letters.get(&'M').unwrap().contains(&(x-1, y-1)) &&
        letters.get(&'M').unwrap().contains(&(x+1, y-1)) &&
        letters.get(&'S').unwrap().contains(&(x+1, y+1)) &&
        letters.get(&'S').unwrap().contains(&(x-1, y+1))) ||

        (letters.get(&'M').unwrap().contains(&(x-1, y-1)) &&
        letters.get(&'M').unwrap().contains(&(x-1, y+1)) &&
        letters.get(&'S').unwrap().contains(&(x+1, y-1)) &&
        letters.get(&'S').unwrap().contains(&(x+1, y+1))) ||

        (letters.get(&'M').unwrap().contains(&(x+1, y-1)) &&
        letters.get(&'M').unwrap().contains(&(x+1, y+1)) &&
        letters.get(&'S').unwrap().contains(&(x-1, y-1)) &&
        letters.get(&'S').unwrap().contains(&(x-1, y+1))) ||

        (letters.get(&'M').unwrap().contains(&(x-1, y+1)) &&
        letters.get(&'M').unwrap().contains(&(x+1, y+1)) &&
        letters.get(&'S').unwrap().contains(&(x+1, y-1)) &&
        letters.get(&'S').unwrap().contains(&(x-1, y-1))))
    .count()
}