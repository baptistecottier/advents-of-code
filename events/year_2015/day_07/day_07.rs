aoc::main!();

fn preprocessing(input: &str) -> Vec<(u8, &str, &str, &str)> {
    input
        .lines()
        .map(|gate| gate.split(' ').collect_vec())
        .map(|gate| match gate[1] {
            "->" => (0, gate[0], "0", gate[2]),
            "AND" => (1, gate[0], gate[2], gate[4]),
            "OR" => (2, gate[0], gate[2], gate[4]),
            "LSHIFT" => (3, gate[0], gate[2], gate[4]),
            "RSHIFT" => (4, gate[0], gate[2], gate[4]),
            _ => (5, gate[1], "0", gate[3]),
        })
        .sorted_by_key(|gate| (gate.3.len(), gate.3))
        .collect()
}

fn part_1(circuit: Vec<(u8, &str, &str, &str)>) -> u16 {
    solver(circuit, HashMap::new())
}

fn part_2(circuit: Vec<(u8, &str, &str, &str)>) -> u16 {
    solver(
        circuit.clone(),
        HashMap::from([("b", solver(circuit.clone(), HashMap::new()))]),
    )
}

fn solver(circuit: Vec<(u8, &str, &str, &str)>, wires: HashMap<&str, u16>) -> u16 {
    circuit
        .iter()
        .cycle()
        .skip(1 + wires.len())
        .take(circuit.len())
        .fold(wires, |mut wire, &(i, in1, in2, out)| {
            let temp = match in1.parse::<u16>() {
                Ok(value) => value,
                _ => wire[in1],
            };

            match i {
                0 => wire.insert(out, temp),
                1 => wire.insert(out, temp & wire[in2]),
                2 => wire.insert(out, temp | wire[in2]),
                3 => wire.insert(out, wire[in1] << in2.parse::<u16>().unwrap()),
                4 => wire.insert(out, wire[in1] >> in2.parse::<u16>().unwrap()),
                5 => wire.insert(out, !wire[in1]),
                _ => unreachable!(),
            };
            wire
        })
        .get("a")
        .unwrap()
        .to_owned()
}
