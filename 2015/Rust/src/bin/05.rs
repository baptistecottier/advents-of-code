aoc_2015::main!(); 

fn generator(input : &str) -> Vec<&str> {
    input
    .lines()
    .collect_vec()
}

fn part_1(input : Vec<&str>) -> usize {
    input
        .iter()
        .filter( |s| {
            s.matches(['a','e','i','o','u']).count() >= 3 &&
            ! ["ab", "cd", "pq", "xy"].iter().any(|ss| s.contains(ss)) &&
            ["aa","zz","ee","rr","tt","yy","uu","ii","oo","pp","qq","ss","dd","ff","gg","hh","jj","kk","ll","mm","ww","xx","cc","vv","bb","nn"].iter().any(|ss| s.contains(ss)) 
})
        .count()

}

fn part_2(input : Vec<&str>) -> usize {
    input
    .iter()
    .filter(|s|{
        s.chars().tuple_windows::<(char, char, char)>().any(|(a,_,c)| a==c) &&
        s.chars().tuple_windows::<(char, char)>().any(|(a,b)| s.matches(&[a,b].iter().collect::<String>()).count()>=2)
    })    
    .count()
}