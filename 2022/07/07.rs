aoc2022::main!() ;

fn generator(input : &str) -> Vec<&str>{
    input
        .lines()
        .collect_vec()
}

fn part_1(input : Vec<&str>) -> i32{
    solver(input, 100_000, false)
        .iter()
        .sum()
}

fn part_2(input : Vec<&str>) -> i32 {
    *solver(input.clone(), solver(input.clone(), 0, true).iter().max().unwrap() - 40_000_000, true)
        .iter()
        .min()
        .unwrap()
}

fn solver (input :Vec<&str>, bound : i32, delete : bool) -> Vec<i32> {
    let mut path : Vec<String> = ["root".to_string()].to_vec() ;
    let mut sizes : HashMap<String, i32> = HashMap::new();
    input
        .iter()
        .enumerate()
        .for_each(|(n,command)| {
            let details = command.split(' ').collect_vec() ;
            match details[0] {
            "$" => match details[1..].concat().as_str() {
                "cd.." => path.truncate(&path.len()-1),
                "cd/"  =>  () ,
                "ls"    => () ,
                _       => path.push([details[2] , n.to_string().as_str()].concat().to_string())} 
            "dir"   => (),
            _       =>  path.iter().for_each(|folder|
                            if sizes.contains_key(folder) {
                                sizes.insert(folder.to_string(), details[0].parse::<i32>().unwrap() + sizes[folder]);
                            } else { sizes.insert(folder.to_string(), details[0].parse::<i32>().unwrap()) ; })
                }      
            }
        );
        sizes
        .iter()
        .map(|(folder, _)| sizes[folder])
        .filter(|n| if delete {n > &bound} else {n <= &bound})
        .collect_vec()
        .into()
    
}