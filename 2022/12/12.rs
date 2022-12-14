aoc2022::main!(); 

fn generator(input : &str) ->  Vec<Vec<i16>> {
    input
        .lines()
        .map(|l| l.chars().map(|c| match c {
            'S' => 0 , 
            'E' => 27, 
            _ => c as i16 - 96,
        } ).collect_vec())
        .collect_vec()
}

fn part_1(input:  Vec<Vec<i16>>) -> usize {
    solver(input, 0)
}


fn part_2(input :  Vec<Vec<i16>>) -> usize {
    solver(input, 1)
}

fn solver(input : Vec<Vec<i16>>, start : i16) -> usize {
    let (h, w) = (input.len(), input.iter().next().unwrap().len()) ;
    let starting_positions : Vec<(usize, usize)> =
        iproduct!((0..h), (0..w))
            .filter(|&(x,y)| input[x][y] == start)
            .collect_vec() ;
    let end : (usize, usize) =  
        iproduct!((0..h), (0..w))
            .find(|&(x,y)| input[x][y] == 27)
            .unwrap();

    starting_positions
        .iter()
        .map(|&(x,y)| bfs(input.clone(), (x,y), end))
        .collect_vec()
        .iter()
        .min()
        .unwrap()
        .to_owned()
}

fn bfs(maze : Vec<Vec<i16>>, start : (usize, usize), end : (usize, usize)) -> usize {
    let (h, w) = (maze.len(), maze.iter().next().unwrap().len()) ;
    let mut seen = HashSet::new();
    seen.insert(start) ; 
    let mut queue = [[start].to_vec()].to_vec();
    while !queue.is_empty() {
        let path = queue.pop().unwrap() ;
        let (x, y) = path[0] ;
        let temp_seen = seen.clone();
        if (x,y) == end  {return path.len()-1}
        neighbors(x,y)
            .iter()
            .filter(|(x2, y2)| *y2 < w && *x2 < h && !temp_seen.contains(&(*x2, *y2)) && (maze[*x2][*y2]-maze[x][y] < 2))
            .for_each(|&(x2, y2)| {
                queue.insert(0, [[(x2, y2)].to_vec(), path.clone()].concat()) ;
                seen.insert((x2, y2));
            })
    };
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