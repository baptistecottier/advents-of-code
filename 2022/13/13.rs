aoc::main!();

fn preprocessing(input: &str) -> Vec<&str> {
    input.split("\n\n").collect()
}

fn part_1(input :  Vec<&str>) -> usize {
    let test = input
        .iter()
        .map(|l| {
            let pair : Vec<&str> = l.split('\n').collect() ;
            is_list_sorted(pair[0], pair[1])}).collect_vec()  ;
    println!("{:?}", test );
    2
}

fn part_2(input :  Vec<&str>) -> usize {
    2
}



fn is_list_sorted(la : &str, lb : &str) {
    
}