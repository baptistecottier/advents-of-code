aoc::main!();

fn preprocessing(input: &str) -> Vec<HashMap<&str, &str>> {
    input
        .split("\n\n")
        .map(|passport| {
            passport
                .split(&['\n', ':', ' '])
                .collect_vec()
                .chunks(2)
                .map(|chunk| (chunk[0], chunk[1]))
                .collect::<HashMap<_, _>>()
        })
        .collect_vec()
}

fn part_1(passports: Vec<HashMap<&str, &str>>) -> usize {
    passports
        .iter()
        .filter(|passport| {
            passport.len() == 8 || (passport.len() == 7 && !passport.contains_key("cid"))
        })
        .count()
}

fn part_2(passports: Vec<HashMap<&str, &str>>) -> usize {
    passports
        .iter()
        .filter(|passport| {
            (passport.len() == 8 || (passport.len() == 7 && !passport.contains_key("cid")))
                && (1920..=2002).contains(&passport["byr"].parse::<u16>().unwrap())
                && (2010..=2020).contains(&passport["iyr"].parse::<u16>().unwrap())
                && (2020..=2030).contains(&passport["eyr"].parse::<u16>().unwrap())
                && ((passport["hgt"].contains("in")
                    && (59..=76).contains(&passport["hgt"][..2].parse::<u16>().unwrap_or(0)))
                    || (passport["hgt"].contains("cm")
                        && (150..=193).contains(&passport["hgt"][..3].parse::<u16>().unwrap_or(0))))
                && (passport["hcl"].starts_with('#')
                    && passport["hcl"][1..].chars().all(|c| c.is_ascii_hexdigit()))
                && ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].contains(&passport["ecl"])
                && passport["pid"].len() == 9
        })
        .count()
}
