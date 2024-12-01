use itertools::Itertools;
use std::collections::HashSet;

#[macro_export]
macro_rules! main {
    () => {
        #[allow(unused_import)]
        use {
            aho_corasick::{AhoCorasick, PatternID},
            aoc::screen_reader,
            grid::Grid,
            itertools::{chain, iproduct, multizip, repeat_n, FoldWhile, Itertools},
            md5::compute,
            mod_exp::mod_exp,
            num::{Integer, pow},
            regex::Regex,
            roots::find_roots_quadratic,
            roots::Roots,
            serde_json::{json, Value},
            std::cmp::Ordering,
            std::collections::{HashMap, HashSet, VecDeque},
            std::env,
            std::fs::read_to_string,
            std::iter::{successors, zip},
            std::ops::{Range, RangeInclusive},
            std::str::FromStr,
        };

        fn main() {
            let year = &module_path!()[..4];
            let day = &module_path!()[5..];
            let puzzle_input =
                read_to_string(format!("../events/{}/{}/{}.input", year, day, day).trim_end())
                    .expect("File does not exist");

            let input = preprocessing(puzzle_input.as_str());

            println!("{:?}", (part_1(input.clone()), part_2(input)));
        }
    };
}

pub fn rev_slice(input: &[u32]) -> Vec<u32> {
    let mut a = input.to_vec();
    a.reverse();
    a
}

pub fn screen_reader(pixels: HashSet<(usize, usize)>) -> String {
    pixels
        .iter()
        .map(|(x, y)| {
            (
                x - pixels.iter().min_by_key(|(x, _)| x).unwrap().0,
                y - pixels.iter().min_by_key(|(_, y)| y).unwrap().1,
            )
        })
        .sorted()
        .chunk_by(|(x, _)| x / 5)
        .into_iter()
        .map(|(k, v)| {
            (
                k,
                v.map(|(x, y)| (x % 5, y)).collect::<Vec<(usize, usize)>>(),
            )
        })
        .map(|(_, v)| match v.len() {
            9 => {
                if v.contains(&(3, 0)) {
                    'J'
                } else if v.contains(&(0, 5)) {
                    'L'
                } else {
                    'Y'
                }
            }
            10 => {
                if v.contains(&(0, 0)) {
                    'I'
                } else {
                    'C'
                }
            }
            11 => {
                if v.contains(&(0, 0)) {
                    'F'
                } else {
                    'S'
                }
            }
            12 => {
                if !v.contains(&(0, 0)) {
                    'O'
                } else if v.contains(&(1, 2)) {
                    'K'
                } else if v.contains(&(3, 5)) {
                    'Z'
                } else if v.contains(&(3, 4)) {
                    'U'
                } else {
                    'P'
                }
            }
            13 => 'G',
            14 => {
                if !v.contains(&(0, 0)) {
                    'A'
                } else if v.contains(&(1, 3)) {
                    'R'
                } else if v.contains(&(2, 0)) {
                    'E'
                } else {
                    'H'
                }
            }
            _ => 'B',
        })
        .join("")
}

/*
A: [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 3), (2, 0), (2, 3), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)]
B: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 2), (1, 5), (2, 0), (2, 2), (2, 5), (3, 1), (3, 3), (3, 4)]
C: [(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 5), (2, 0), (2, 5), (3, 1), (3, 4)]
D: Not encountered yet
E: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 2), (1, 5), (2, 0), (2, 2), (2, 5), (3, 0), (3, 5)]
F: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 2), (2, 0), (2, 2), (3, 0)]
G: [(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 5), (2, 0), (2, 3), (2, 5), (3, 1), (3, 3), (3, 4), (3, 5)]
H: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (2, 2), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)]
I: [(1, 0), (1, 5), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 0), (3, 5)]
J: [(0, 4), (1, 5), (2, 0), (2, 5), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
K: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (2, 1), (2, 3), (2, 4), (3, 0), (3, 5)]
L: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5)]
M: Not encountered yet
N: Not encountered yet
O: [(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 5), (2, 0), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4)]
P: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 3), (2, 0), (2, 3), (3, 1), (3, 2)]
Q: Not encountered yet
R: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 3), (2, 0), (2, 3), (2, 4), (3, 1), (3, 2), (3, 5)]
S: [(0, 1), (0, 2), (0, 5), (1, 0), (1, 3), (1, 5), (2, 0), (2, 3), (2, 5), (3, 0), (3, 4)]
T: Not encountered yet
U: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 5), (2, 5), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
V: Not encountered yet
W: Not encountered yet
X: Not encountered yet
Y: [(2, 5), (0, 1), (2, 4), (1, 2), (0, 0), (3, 2), (4, 1), (2, 3), (4, 0)]
Z: [(0, 0), (0, 4), (0, 5), (1, 0), (1, 3), (1, 5), (2, 0), (2, 2), (2, 5), (3, 0), (3, 1), (3, 5)]
*/
