aoc::main!();

fn preprocessing(input_: &str) -> String {
    input_.to_string()
}


fn part_1(polymer: String) -> usize {
    react(polymer)
}


fn part_2(polymer: String) -> usize {
    zip('a'..='z', 'A'..='Z')
    .map(|(l, r)| polymer.clone().replace(r, "").replace(l, ""))
    .map(|poly| react(poly))
    .min()
    .unwrap()
}


fn react(polymer: String) -> usize {
    successors(Some(polymer.clone()), |polymer_|
        Some(
            zip('a'..='z', 'A'..='Z')
            .map(|(a, b)| 
                (
                    [a.to_string(), b.to_string()].concat()
                ,
                    [b.to_string(), a.to_string()].concat()
                    ))
        .fold(polymer_.to_string(), |poly: String, (l, r)|
            poly.replace(&r, "").replace(&l, ""))))
    .tuple_windows()
    .take_while(|(p1, p2)| p1 != p2)
    .last()
    .unwrap()
    .1
    .len()
}
