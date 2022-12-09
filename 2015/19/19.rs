aoc_2015::main!();

fn generator(input : &str) -> (Vec<Vec<&str>>,&str) {
    let length = input.lines().count();
    (input
        .lines()
        .take(length - 2)
        .map(|l| l.split(" => ").collect_vec())
        .collect_vec() ,
     input.lines().nth(length - 1).unwrap())
            }

fn part_1(input : (Vec<Vec<&str>>,&str)) -> usize {
    apply_replacements(input.1.to_string(), input.0)
        .len()
    }

fn part_2(input : (Vec<Vec<&str>>,&str)) -> usize {
    let mut round = 0 ;
    let replacements = input.0.iter().map(|v| [v[1], v[0]].to_vec()).collect_vec();
    let mut molecules = [input.1.to_string()].to_vec() ;
    while !molecules.contains(&"e".to_string()) {
        molecules = molecules
                        .iter()
                        .map(|mol| apply_replacements(mol.to_string(), replacements.clone()))
                        .flatten()
                        .collect_vec()
                        ;
                        round += 1 ;
        println!("{:?}",round);
    };
        round
        }

fn apply_replacements(input : String, replacements : Vec<Vec<&str>>) -> Vec<String> {
    replacements
        .iter()
        .map(|pattern|  (input.match_indices(pattern[0]).collect_vec(),pattern[1]))
        .map(| (matches , out)| {
            matches
                .iter()
                .map(|(indice , pattern)| {
                    let mut new_molecule = input.clone() ;
                    new_molecule.replace_range(*indice..*indice+pattern.len(), out);
                    new_molecule
                })
                .collect_vec()
        })
        .flatten()
        .unique()
        .collect_vec()
}