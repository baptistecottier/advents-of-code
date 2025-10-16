aoc::main!();

fn preprocessing(puzzle_input: &str) -> Vec<RangeInclusive<u32>> {
    let blacklist: Vec<RangeInclusive<u32>> = puzzle_input
        .split(['\n', '-'])
        .map(|n| n.parse().unwrap())
        .tuples()
        .map(|(start, end)| start..=end)
        .sorted_by(|a, b| Ord::cmp(&a.start(), &b.start()))
        .collect();

    let mut allowed_ip = next_allowed_ip(0, &blacklist);
    let mut intervales = Vec::new();
    while allowed_ip < u32::MAX {
        let next_ip = blacklist
            .iter()
            .find_or_first(|r| *r.start() > allowed_ip)
            .unwrap_or(&(u32::MAX - 1..=u32::MAX))
            .start();
        intervales.push(allowed_ip..=*next_ip);
        allowed_ip = next_allowed_ip(*next_ip, &blacklist);
    }
    intervales
}

fn part_1(whitelist: Vec<RangeInclusive<u32>>) -> u32 {
    *whitelist.first().unwrap().start()
}

fn part_2(blacklist: Vec<RangeInclusive<u32>>) -> u32 {
    blacklist.iter().map(|r| r.end() - r.start()).sum()
}

fn next_allowed_ip(ip: u32, blacklist: &Vec<RangeInclusive<u32>>) -> u32 {
    if ip == u32::MAX {
        return ip;
    }
    for r in blacklist {
        if r.contains(&ip) {
            return next_allowed_ip(r.end().saturating_add(1), blacklist);
        }
    }
    ip
}
