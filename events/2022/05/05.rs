
aoc::main!(); 

fn preprocessing(input: &str) -> (Vec<String> , Vec<(usize, usize, usize)>) {
    let (crates, rearrangements) = input.split("\n\n").collect_tuple().unwrap() ;   
    let h = crates.lines().count() - 1  ;
    let w = (crates.len()-h) / (4 * h);
   (crates
        .replace("    ","_")
        .replace(['[',']',' '], "")
        .lines()
        .map(|l| format!("{}{}",l, "_".repeat(w - l.len())))
        .collect::<String>()
        .chars()
        .take(w * h)
        .enumerate()
        .sorted_by(|(m,_),(n,_)| (m % w).cmp(&(n % w)))
        .map(|(_, c)| c)
        .chunks(h)
        .into_iter()
        .map(|c| c.collect::<String>().replace("_", ""))
        .collect_vec() 
        ,

    rearrangements
        .lines()
        .map(|r| r.split_whitespace().filter_map(|s| s.parse().ok()).collect_tuple().unwrap())
        .map(|(n, start, end)| (n, start-1, end-1))
        .collect_vec())
}

fn part_1(input: (Vec<String> , Vec<(usize, usize, usize)>)) -> String {
    solver(input, |c| c.rev().collect::<String>())
}

fn part_2(input: (Vec<String> , Vec<(usize, usize, usize)>)) -> String {
    solver(input, |c| c.collect::<String>())
}

fn solver<F>(input: (Vec<String> , Vec<(usize, usize, usize)>) , f: F) -> String 
where
    F: Fn(std::string::Drain) -> String,
{
    let (mut stacks, _) = input ; 
    input.1
        .iter()
        .for_each(|&(n,s,e)| { 
            let crates: &str = &f(stacks[s].drain(..n));
            stacks[e].insert_str(0 , crates) ;
            });
    stacks
        .iter()
        .map(|c| c.chars().nth(0).unwrap())
        .collect::<String>()
}