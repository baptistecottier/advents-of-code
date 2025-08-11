aoc::main!();

fn preprocessing(puzzle_input: &str) -> ((usize, usize), Vec<(usize, usize)>) {
    let height = puzzle_input.lines().count();
    let width = puzzle_input.len() / height ;
    let guard = puzzle_input.chars().find_position(|c| c == '^').unwrap()

    (
        (guard % width, guard / width)
    ,
        puzzle_input
        .char_indices()
        .filter(|(_, c)| c == '#')
        .map(|(n, _)| (n % width, n / height))
        .collect_vec()
    ,
        width
    ,
        height
    )
}

fn part_1(guard: (usize, usize), obstacles: Vec<(usize, usize)>, width: usize, height: usize) ->  {
    
}

fn part_2() ->  {

}