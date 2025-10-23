aoc::main!();

#[derive(Clone)]
enum Operation {
    SwapPositions(usize, usize),
    SwapLetters(char, char),
    ReversePositions(usize, usize),
    RotateLeft(usize),
    RotateRight(usize),
    MovePos(usize, usize),
    RotateBasedOnLetter(char),
}

impl Operation {
    fn apply(&self, password: Vec<char>) -> Vec<char> {
        match self {
            Operation::SwapPositions(src, dst) => swap_positions(password, *src, *dst),
            Operation::SwapLetters(src, dst) => swap_letters(password, *src, *dst),
            Operation::ReversePositions(start, end) => reverse_positions(password, *start, *end),
            Operation::RotateLeft(steps) => rotate(password.clone(), password.len() - *steps),
            Operation::RotateRight(steps) => rotate(password, *steps),
            Operation::MovePos(from, to) => move_pos(password, *from, *to),
            Operation::RotateBasedOnLetter(letter) => {
                let pos = password.iter().position(|&c| c == *letter).unwrap();
                let steps = if pos >= 4 { pos + 2 } else { pos + 1 };
                rotate(password, steps)
            }
        }
    }
}

fn preprocessing(puzzle_input: &str) -> Vec<Operation> {
    puzzle_input
        .lines()
        .map(|line| {
            let words: Vec<&str> = line.split_whitespace().collect();
            match &words[..] {
                ["swap", "position", a, "with", "position", b] => {
                    Operation::SwapPositions(a.parse().unwrap(), b.parse().unwrap())
                }
                ["swap", "letter", a, "with", "letter", b] => {
                    Operation::SwapLetters(a.chars().next().unwrap(), b.chars().next().unwrap())
                }
                ["rotate", "left", steps, ..] => Operation::RotateLeft(steps.parse().unwrap()),
                ["rotate", "right", steps, ..] => Operation::RotateRight(steps.parse().unwrap()),
                ["rotate", "based", "on", "position", "of", "letter", letter] => {
                    Operation::RotateBasedOnLetter(letter.chars().next().unwrap())
                }
                ["reverse", "positions", start, "through", end] => {
                    Operation::ReversePositions(start.parse().unwrap(), end.parse().unwrap())
                }
                ["move", "position", from, "to", "position", to] => {
                    Operation::MovePos(from.parse().unwrap(), to.parse().unwrap())
                }
                _ => panic!("Unknown operation: {}", line),
            }
        })
        .collect()
}

fn part_1(operations: Vec<Operation>) -> String {
    operations
        .iter()
        .fold(
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].to_vec(),
            |acc, op| op.apply(acc),
        )
        .iter()
        .join("")
}

fn part_2(operations: Vec<Operation>) -> String {
    let mut password = vec!['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
    let target = vec!['f', 'b', 'g', 'd', 'c', 'e', 'a', 'h'];

    let mut next_password = operations
        .iter()
        .fold(password.clone(), |acc, op| op.apply(acc));

    while next_password != target {
        password = next_password;
        next_password = operations
            .iter()
            .fold(password.clone(), |acc, op| op.apply(acc));
    }

    password.iter().collect()
}

fn swap_letters(mut password: Vec<char>, src: char, dst: char) -> Vec<char> {
    let a = password.iter().position(|&c| c == src).unwrap();
    let b = password.iter().position(|&c| c == dst).unwrap();
    password.swap(a, b);
    password
}

fn swap_positions(mut password: Vec<char>, src: usize, dst: usize) -> Vec<char> {
    password.swap(src, dst);
    password
}

fn rotate(password: Vec<char>, steps: usize) -> Vec<char> {
    let len = password.len();
    let steps = steps % len;
    [
        password.get(len - steps..).unwrap(),
        password.get(..len - steps).unwrap(),
    ]
    .concat()
}

fn reverse_positions(mut password: Vec<char>, start: usize, end: usize) -> Vec<char> {
    password[start..=end].reverse();
    password
}

fn move_pos(mut password: Vec<char>, from: usize, to: usize) -> Vec<char> {
    let a = password.remove(from);
    password.insert(to, a);
    password
}
