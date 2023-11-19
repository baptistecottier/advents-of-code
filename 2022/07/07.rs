aoc::main!() ;

fn preprocessing(input: &str) -> Vec<&str>{
    input.lines().collect_vec()
}

fn part_1(input: Vec<&str>) -> u32{
    solver(input, 100_000, false).iter().sum()
}

fn part_2(input: Vec<&str>) -> u32 {
    let to_free = input
        .iter()
        .filter(|cmd| ! (cmd.contains("$") || cmd.contains("dir")))
        .map(|n| n.split(' ').collect_vec().iter().nth(0).unwrap().parse::<u32>().unwrap())
        .sum::<u32>() 
        - 40_000_000 ;
    *solver(input.clone(), to_free, true).iter().min().unwrap()

}

fn solver (input :Vec<&str>, bound: u32, delete: bool) -> Vec<u32> {
    let mut path: String = root();
    let mut sizes: HashMap<String, u32> = HashMap::new();
    input
        .iter()
        .for_each(| command | {
            let details = command.split(' ').collect_vec() ;
            match details[0] {
            "dir"   => (),
            "$" => match details[1..].concat().as_str() {
                "ls"    => (),
                "cd/"   => path = root(),
                "cd.."  => path = back(path.clone()),
                _       => path = open(path.clone(), details[2])} 
            _       =>  sizes = update_sizes(path.clone() , sizes.clone(), details[0])}
            }
        );
    
    sizes
        .iter()
        .map(|(folder, _)| sizes[folder])
        .filter(|&n|   (n > bound) == delete )
        .collect_vec()    
}

fn root() -> String {
    return "root/".to_string()
}

fn back(path: String) -> String {
    return [path.rsplitn(3 , '/').collect_vec().iter().nth_back(0).unwrap().to_string(),"/".to_string()].concat()
}

fn open(path: String, new_folder: &str) -> String {
    return [path.to_string(),new_folder.to_string(),"/".to_string()].concat()
}

fn update_sizes(path: String, mut sizes: HashMap<String, u32>, size: &str) -> HashMap<String, u32> {
    let paths = path.split_terminator('/').collect_vec() ;
    let file_size = size.parse::<u32>().unwrap() ;
    paths
        .iter()
        .scan("".to_string(), |p , &f| {
            p.push_str(f) ; 
            Some(p.clone())})
        .for_each(|folder| {
        if sizes.contains_key(&folder) { 
            sizes.insert(folder.clone(), file_size + sizes[&folder])} else {
            sizes.insert(folder.clone(), file_size)};
        }) ;
    return sizes
}