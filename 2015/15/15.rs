aoc_2015::main!(); 

fn generator(input : &str) -> Vec<[i64 ; 5]> {
    input
        .lines()
        .map(|l| l.split([' ',',']).collect_vec())
        .map(|v| [v[2].parse::<i64>().unwrap(), v[5].parse::<i64>().unwrap(), v[8].parse::<i64>().unwrap(), v[11].parse::<i64>().unwrap(), v[14].parse::<i64>().unwrap()])
        .collect_vec()
}


fn part_1(input : Vec<[i64 ; 5]>) -> i64 {
    solver(input, false)
}



fn part_2(input : Vec<[i64 ; 5]>) -> i64 {
    solver(input, true)
}


fn solver(input : Vec<[i64 ; 5]>, check_calories : bool) -> i64 {
(0..100).map(|i| {
    let sprinkles = &input[0].iter().map(|elem| i * elem).collect_vec();
    (0..100-i).map(|j| {
        let peanutbutter = input[1].iter().map(|elem| j * elem).collect_vec();
        (0..100-(i+j)).map(|k| {
            let frosting = input[2].iter().map(|elem| k * elem).collect_vec();
            let sugar = input[3].iter().map(|elem| (100-(i+j+k)) * elem).collect_vec();
            let calories = sprinkles[4] + peanutbutter[4] + frosting[4] + sugar[4];
            if check_calories && calories != 500 {0} 
            else {
            (0..4).map(|v|  {
                let s = sprinkles[v]+peanutbutter[v]+frosting[v]+sugar[v];
                if  s < 0 {0} else {s}
                }
            )
            .fold(1 , |acc, elem| acc * elem)
        }}).max().unwrap()
    }).max().unwrap()
}).max().unwrap() 
}