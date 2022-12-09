aoc_2015::main!();

fn generator(input : &str) -> Vec<(u8, char, i32)> {
    input
        .lines()
        .map(|l| l.splitn(1, ' ').collect())
        .map(|l| 
            match l[0] {
                "hlf" => (1,l[1],0),
                "tpl" => (2,l[1],0),
                "inc" => (3,l[1],0),
                _ => {
                    let [r, j] = l[1].split(", ");
                    match l[0] {
                        "jmp" => (4,r.chars().nth(0),j.parse::<i32>()),
                        "jie" => (5,r.chars().nth(0),j.parse::<i32>()),
                        "jio" => (6,r.chars().nth(0),j.parse::<i32>()),
                    }}
            })
        .collect_vec()

}

fn part_1(input : Vec<(u8, char, i32)>) -> usize {
    3
}

fn part_2(input : Vec<(u8, char, i32)>) -> usize {
    3
}