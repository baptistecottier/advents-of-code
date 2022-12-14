#[macro_export]
macro_rules! main {
    () => {
        #[allow(unused_import)]
        use {
            aoc2022::{rev_slice},
            itertools::{chain, iproduct, repeat_n, FoldWhile, Itertools},
            std::cmp::Ordering,
            std::collections::{HashMap, HashSet, VecDeque},
            std::iter::zip,
            std::ops::{Range, RangeInclusive},
            std::str::FromStr,
            std::env,
        };
        

        fn main() {
            let input_path = include_str!(concat!("../", module_path!(), "/",module_path!(),".txt")).trim_end() ;
            let input =
                generator(input_path);

            println!("{}", part_1(input.clone()));
            println!("{}", part_2(input));
        }
    };
}

pub fn rev_slice(input : &[u32]) -> Vec<u32> {
    let mut a = input.to_vec() ;
    a.reverse() ; 
    a
}

