aoc2022::main!(); 

fn generator(input : &str) -> (Vec<String> , Vec<(usize, usize, usize)>) {
    let (crates, rearrangements) = input.split("\n\n").collect_tuple().unwrap() ;   
    let w = crates.trim().chars().last().unwrap().to_digit(10).unwrap() as usize;
    let h = crates.split('\n').collect_vec().len() - 1 ;

   (crates.replace("    ","_").replace(['[',']','\n',' '], "")
        .chars()
        .take(w * h)
        .enumerate()
        .sorted_by(|(m,_),(n,_)| (m % w).cmp(&(n % w)))
        .map(|(_, c)| c)
        .chunks(h)
        .into_iter()
        .map(|mut c| c.join("").replace("_", ""))
        .collect_vec() 
        ,

    rearrangements
        .lines()
        .map(|r| r.split_whitespace().collect_vec().iter().filter_map(|s| s.parse().ok()).collect_tuple().unwrap())
        .map(|(n, start, end)| (n, start-1, end-1))
        .collect_vec())
}

fn part_1(input : (Vec<String> , Vec<(usize, usize, usize)>)) -> String {
    solver(input, |c| c.rev().join(""))
}

fn part_2(input : (Vec<String> , Vec<(usize, usize, usize)>)) -> String {
    solver(input, |mut c| c.join(""))
}

fn solver<F>(input : (Vec<String> , Vec<(usize, usize, usize)>) , f : F) -> String 
where
    F: Fn(std::string::Drain) -> String,
{
    let (mut stacks, _) = input ; 
    input.1
        .iter()
        .for_each(|&(n,s,e)| { 
            let crates : &str = &f(stacks[s].drain(..n));
            stacks[e].insert_str(0 , crates) ;
            });
    stacks
        .iter()
        .map(|c| c.chars().nth(0).unwrap())
        .join("")
}