aoc::main!();

fn preprocessing(input: &str) -> Vec<Vec<char>> {
    (0..50)
    .map(|y| 
        (0..50)
        .map(|x| x * x + 3 * x + 2 * x * y + y + y * y + input.parse::<usize>().unwrap())
        .map(|x| format!("{:b}", x))
        .map(|x| x.chars().filter(|&c| c == '1').count() % 2 == 1)
        .map(|x| 
            match x {
                true => '#',
                false => '.'})
        .collect_vec())
    .collect_vec()
}

fn part_1(maze: Vec<Vec<char>> ) -> usize {
    bfs(maze, (1,1), (31, 39))
}

fn part_2(maze: Vec<Vec<char>> ) -> usize {
    iproduct!(0..50, 0..50)
    .map(|(x,y)| bfs(maze.clone(), (1,1), (x, y)))
    .filter(|&v| v <= 50)
    .count()
}


fn bfs(maze: Vec<Vec<char>>, start: (usize, usize), end: (usize, usize)) -> usize {
    let (h, w) = (maze.len(), maze.iter().next().unwrap().len()) ;
    let mut seen = HashSet::from([start]);
    let mut queue = [[start].to_vec()].to_vec();
    while !queue.is_empty() {
        let path = queue.pop().unwrap() ;
        let (x, y) = path[0] ;
        let temp_seen = seen.clone();
        if (x, y) == end  {return path.len()-1}
        
        neighbors(x, y)
        .iter()
        .filter(|(x2, y2)| *x2 < w && *y2 < h && !temp_seen.contains(&(*x2, *y2)) && maze[*y2][*x2] == '.')
        .for_each(|&(x2, y2)| {
            queue.insert(0, [[(x2, y2)].to_vec(), path.clone()].concat()) ;
            seen.insert((x2, y2));})};
    usize::MAX
}

fn neighbors(x: usize, y: usize) -> Vec<(usize, usize)> {
    let mut next = vec![(x + 1, y), (x, y + 1)];
    if x >= 1 {
        next.push((x - 1, y));
    }
    if y >= 1 {
        next.push((x, y - 1));
    }
    next
}
