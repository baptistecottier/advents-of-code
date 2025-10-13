aoc::main!();

fn preprocessing(input: &str) -> String {
    input.to_string()
}

fn part_1(passwords: String) -> String {
    solver(passwords.clone())
}

fn part_2(passwords: String) -> String {
    solver(next_pw(solver(passwords.clone())))
}

fn solver(mut passwords: String) -> String {
    let mut new_pw: bool = false;
    while !new_pw {
        if !passwords.contains('o')
            && !passwords.contains('i')
            && !passwords.contains('l')
            && (passwords
                .chars()
                .into_iter()
                .tuple_windows::<(_, _, _)>()
                .map(|(a, b, c)| ((a == b && b != c) | (b == c && a != b)) as usize)
                .fold(0, |acc, b| acc + b)
                > 2)
            && (passwords
                .chars()
                .into_iter()
                .tuple_windows::<(_, _, _)>()
                .any(|(a, b, c)| b as usize == a as usize + 1 && c as usize == b as usize + 1))
        {
            new_pw = true;
        } else {
            passwords = next_pw(passwords);
        }
    }
    passwords
}

fn next_pw(passwords: String) -> String {
    let mut letters = passwords.chars().collect_vec();
    match letters[7] {
        'i' | 'l' | 'o' => letters[7] = (letters[7] as u8 + 2) as char,
        'z' => {
            letters[7] = 'a';
            let mut c = 6;
            while letters[c] == 'z' {
                letters[c] = 'a';
                c -= 1;
            }
            letters[c] = (letters[c] as u8 + 1) as char;
        }
        _ => letters[7] = (letters[7] as u8 + 1) as char,
    }

    letters.into_iter().collect()
}
