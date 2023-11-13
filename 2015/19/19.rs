aoc::main!();

fn preprocessing(input: &str) -> (Vec<Vec<&str>>,&str) {
    let length = input.lines().count();
    
    (
    input
    .lines()
    .take(length - 2)
    .map(|l| l.split(" => ").collect_vec())
    .collect_vec() 
    ,
    input.lines().nth(length - 1).unwrap()
    )
}

fn part_1(data: (Vec<Vec<&str>>,&str)) -> usize {
    apply_replacements(data.1.to_string(), data.0)
        .len()
    }

fn part_2(data: (Vec<Vec<&str>>,&str)) -> usize {
    data.1
    .chars()
    .tuple_windows::<(char, char)>()
    .fold(0, |mut acc, (a, b)| {
        if a.is_uppercase() {acc += 1};
        if a == 'Y' {acc -= 2};
        if ((a, b) == ('R', 'n'))| ((a, b) == ('A', 'r')) {acc -= 1};
        acc})
    - 1
    }

fn apply_replacements(data: String, replacements: Vec<Vec<&str>>) -> Vec<String> {
    replacements
        .iter()
        .map(|pattern|  (data.match_indices(pattern[0]).collect_vec(),pattern[1]))
        .map(| (matches , out)| {
            matches
                .iter()
                .map(|(indice , pattern)| {
                    let mut new_molecule = data.clone() ;
                    new_molecule.replace_range(*indice..*indice+pattern.len(), out);
                    new_molecule
                })
                .collect_vec()
        })
        .flatten()
        .unique()
        .collect_vec()
}