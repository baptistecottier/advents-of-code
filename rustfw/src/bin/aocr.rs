/// Advent of Code Rust CLI - Companion to aocp (Python version)
/// Provides a unified interface for running, testing, and managing AOC solutions in Rust

mod args;
mod runner;
mod input;
mod display;
mod utils;
mod scoreboard;

use args::parse_arguments;
use runner::run_day;
use scoreboard::{DayResult, display_scoreboard};

fn main() {
    let args = parse_arguments();
    
    // Validate days
    let invalid_days: Vec<_> = args.days_to_run.iter()
        .filter(|&&d| d < 1 || d > 25)
        .copied()
        .collect();
    
    if !invalid_days.is_empty() {
        eprintln!("❌ Invalid day numbers: {:?} (must be 1-25)", invalid_days);
        std::process::exit(1);
    }
    
    println!("🎯 Running {} day(s) for year {}", args.days_to_run.len(), args.year);
    if args.days_to_run.len() > 1 {
        println!("📅 Days: {}", 
            args.days_to_run.iter()
                .map(|d| d.to_string())
                .collect::<Vec<_>>()
                .join(", "));
    }
    
    // Run each day and collect results
    let mut results = Vec::new();
    let mut success_count = 0;
    
    for day_num in &args.days_to_run {
        match run_day(*day_num, args.year, &args) {
            Ok((true, part1, part2)) => {
                results.push(DayResult {
                    day: *day_num,
                    success: true,
                    part1,
                    part2,
                    error: None,
                });
                success_count += 1;
            }
            Ok((false, _, _)) => {
                results.push(DayResult {
                    day: *day_num,
                    success: false,
                    part1: None,
                    part2: None,
                    error: Some("Solver not found".to_string()),
                });
            }
            Err(e) => {
                results.push(DayResult {
                    day: *day_num,
                    success: false,
                    part1: None,
                    part2: None,
                    error: Some(e),
                });
            }
        }
    }
    
    // Show scoreboard if running full year or multiple days
    if args.days_to_run.len() >= 5 {
        display_scoreboard(args.year, &args.days_to_run, &results);
    }
    
    println!("🏁 Completed {}/{} days successfully", success_count, args.days_to_run.len());
    
    if success_count == 0 {
        std::process::exit(1);
    }
}
