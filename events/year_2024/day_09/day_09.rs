aoc::main! {}

fn preprocessing(puzzle_input: &str) -> Vec<(i64, usize)> {
    puzzle_input
        .char_indices()
        .map(|(i, c)| (i as i64, c.to_digit(10).unwrap() as usize))
        .map(|(i, c)| (if i % 2 == 0 { i / 2 } else { -1 }, c))
        .collect_vec()
}

fn part_1(mut _disk: Vec<(i64, usize)>) -> i64 {
    let mut position: i64 = 0;
    let mut checksum: i64 = 0;

    let mut disk = VecDeque::from(
        _disk
            .iter()
            .map(|&(i, c)| vec![i; c])
            .flatten()
            .collect_vec(),
    );

    while !disk.is_empty() {
        let mut disk_id = disk.pop_front().unwrap();
        while disk_id == -1 && !disk.is_empty() {
            disk_id = disk.pop_back().unwrap();
        }
        checksum += position * disk_id;
        position += 1;
    }
    checksum
}

fn part_2(mut disk: Vec<(i64, usize)>) -> i64 {
    let mut index = disk.len() - 1;

    while index > 0 {
        let (mut to_move_value, mut to_move_size) = disk[index];
        while to_move_value == -1 && index > 0 {
            index -= 1;
            (to_move_value, to_move_size) = disk[index];
        }

        if let Some((found_pos, (_, found_size))) =
            disk.clone()
                .iter()
                .take(index)
                .find_position(|(candidate_value, candidate_size)| {
                    *candidate_value == -1 && *candidate_size >= to_move_size
                })
        {
            if found_pos < index {
                disk[found_pos] = (to_move_value, to_move_size);
                if *found_size > to_move_size {
                    disk.insert(found_pos + 1, (-1, found_size - to_move_size));
                    index += 1;
                }
                disk[index] = (-1, to_move_size);
            }
        }
        index -= 1;
    }

    disk.iter()
        .map(|&(i, c)| vec![i; c])
        .flatten()
        .enumerate()
        .map(|(pos, n)| (pos as i64) * n.max(0))
        .sum()
}
