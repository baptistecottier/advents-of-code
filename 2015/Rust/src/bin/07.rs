aoc_2015::main!();

fn generator(input: &str) -> Vec<(u8, &str, &str, &str)> {
    input
        .lines()
        .map(|l| l.split(' ').collect_vec())
        .map(|l| 
                match l[1] {
                    "->" => (0, l[0] , "0",l[2]),
                    "AND" => (1,l[0], l[2], l[4]),
                    "OR" => (2, l[0], l[2], l[4]),
                    "LSHIFT" => (3, l[0], l[2], l[4]),
                    "RSHIFT" => (4, l[0], l[2], l[4]),
                    _ => (5, l[1], "0", l[3]),
                })
                .sorted_by_key(|k| k.3)
                .sorted_by_key(|k| k.3.len())
                .collect()
}

fn part_1(input : Vec<(u8, &str, &str, &str)> ) -> usize {
    let mut wire : HashMap<&str, u16> = HashMap::new();
        input
        .iter()
            .cycle()
            .skip(1)
            .take(input.len())
            .for_each(|(i, in1, in2, out)|{
                match i {
                0 => wire.insert(out, match in1.parse::<u16>(){
                                                                    Ok(v) => v ,
                                                                    _ => wire[in1],
                                                                }) ,
                1 => wire.insert(out, match in1.parse::<u16>(){
                                                                Ok(v) => v ,
                                                                _ => wire[in1],
                                                            } & wire[in2]),
                2 => wire.insert(out, match in1.parse::<u16>(){
                                                                Ok(v) => v ,
                                                                _ => wire[in1],
                                                            } | wire[in2]),
                3 => wire.insert(out, wire[in1] << in2.parse::<u16>().unwrap()),
                4 => wire.insert(out, wire[in1] >> in2.parse::<u16>().unwrap()),
                5 => wire.insert(out, !wire[in1]),
                _ => unreachable!(),
            };});
         wire["a"].into()
}

fn part_2(input :  Vec<(u8, &str, &str, &str)> ) -> usize {
        let mut wire : HashMap<&str, u16> = HashMap::new();
        wire.insert("b", part_1(input.clone()) as u16);
        input
            .iter()
                .cycle()
                .skip(2)
                .take(input.len())
                .for_each(|(i, in1, in2, out)|{
                    match i {
                    0 => wire.insert(out, match in1.parse::<u16>(){
                                                                        Ok(v) => v ,
                                                                        _ => wire[in1],
                                                                    }) ,
                    1 => wire.insert(out, match in1.parse::<u16>(){
                                                                    Ok(v) => v ,
                                                                    _ => wire[in1],
                                                                } & wire[in2]),
                    2 => wire.insert(out, match in1.parse::<u16>(){
                                                                    Ok(v) => v ,
                                                                    _ => wire[in1],
                                                                } | wire[in2]),
                    3 => wire.insert(out, wire[in1] << in2.parse::<u16>().unwrap()),
                    4 => wire.insert(out, wire[in1] >> in2.parse::<u16>().unwrap()),
                    5 => wire.insert(out, !wire[in1]),
                    _ => unreachable!(),
                };});
             wire["a"].into()
    }

