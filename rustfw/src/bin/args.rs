use std::env;

#[derive(Debug, Clone)]
pub struct Args {
    pub year: u32,
    pub days_to_run: Vec<u32>,
    #[allow(dead_code)]
    pub examples: bool,
    #[allow(dead_code)]
    pub examples_verbose: bool,
    #[allow(dead_code)]
    pub no_local: bool,
    #[allow(dead_code)]
    pub force: bool,
    pub save_input: bool,
    #[allow(dead_code)]
    pub extract_examples: bool,
    #[allow(dead_code)]
    pub refresh_examples: bool,
    #[allow(dead_code)]
    pub timeout_seconds: u64,
    pub release: bool,
    #[allow(dead_code)]
    pub verbose: bool,
}

pub fn parse_arguments() -> Args {
    let args: Vec<String> = env::args().collect();
    
    if args.len() < 2 {
        print_usage();
        std::process::exit(1);
    }
    
    let year = match args[1].parse::<u32>() {
        Ok(y) => y,
        Err(_) => {
            eprintln!("❌ Invalid year: {}", args[1]);
            std::process::exit(1);
        }
    };
    
    let mut days_to_run = Vec::new();
    let mut examples = false;
    let mut examples_verbose = false;
    let mut no_local = false;
    let mut force = false;
    let mut save_input = false;
    let mut extract_examples = false;
    let mut refresh_examples = false;
    let mut timeout_seconds = 60u64;
    let mut release = false;
    let mut verbose = false;
    
    let mut i = 2;
    let mut explicit_day = false;
    
    while i < args.len() {
        match args[i].as_str() {
            arg if arg.parse::<u32>().is_ok() && !explicit_day => {
                if let Ok(day) = arg.parse::<u32>() {
                    days_to_run.push(day);
                    explicit_day = true;
                }
            }
            "-e" | "--examples" => examples = true,
            "-ev" | "--examples-verbose" => {
                examples = true;
                examples_verbose = true;
            }
            "--no-local" => no_local = true,
            "--force" => force = true,
            "--save-input" => save_input = true,
            "--extract-examples" => extract_examples = true,
            "--refresh-examples" => refresh_examples = true,
            "-r" | "--release" => release = true,
            "-v" | "--verbose" => verbose = true,
            "--timeout" => {
                i += 1;
                if i < args.len() {
                    if let Ok(t) = args[i].parse::<u64>() {
                        timeout_seconds = t;
                    }
                }
            }
            "--days" => {
                i += 1;
                if i < args.len() {
                    days_to_run = parse_days_string(&args[i]);
                }
            }
            _ => {}
        }
        i += 1;
    }
    
    // If no explicit day specified, run all days
    if days_to_run.is_empty() {
        days_to_run = (1..=25).collect();
    }
    
    Args {
        year,
        days_to_run,
        examples,
        examples_verbose,
        no_local,
        force,
        save_input,
        extract_examples,
        refresh_examples,
        timeout_seconds,
        release,
        verbose,
    }
}

pub fn parse_days_string(days_str: &str) -> Vec<u32> {
    let mut days = Vec::new();
    
    for part in days_str.split(',') {
        let part = part.trim();
        if part.contains('-') {
            if let Some(dash_idx) = part.find('-') {
                if let (Ok(start), Ok(end)) = (
                    part[..dash_idx].parse::<u32>(),
                    part[dash_idx + 1..].parse::<u32>(),
                ) {
                    for d in start..=end {
                        days.push(d);
                    }
                }
            }
        } else if let Ok(day) = part.parse::<u32>() {
            days.push(day);
        }
    }
    
    days.sort();
    days.dedup();
    days
}

fn print_usage() {
    eprintln!("🦀 Advent of Code Rust Runner");
    eprintln!("\nUsage: aocr <year> [day] [OPTIONS]");
    eprintln!("\nExamples:");
    eprintln!("  aocr 2024 1                    # Run day 1 of 2024");
    eprintln!("  aocr 2024 1 --examples         # Test examples first");
    eprintln!("  aocr 2024                      # Run all days of 2024");
    eprintln!("  aocr 2024 --days 1-5           # Run days 1 through 5");
    eprintln!("  aocr 2024 --days 1,3,5         # Run specific days");
    eprintln!("\nOptions:");
    eprintln!("  -e, --examples                 Test examples before running");
    eprintln!("  -ev, --examples-verbose        Test examples with verbose output");
    eprintln!("  --no-local                     Use remote input only");
    eprintln!("  --force                        Run real input even if examples fail");
    eprintln!("  --save-input                   Save puzzle input to local file");
    eprintln!("  --extract-examples             Extract examples from puzzle");
    eprintln!("  --refresh-examples             Force refresh cached examples");
    eprintln!("  --timeout <seconds>            Solver timeout in seconds (default: 60)");
    eprintln!("  -r, --release                  Build in release mode");
    eprintln!("  -v, --verbose                  Verbose output");
    eprintln!("  --days <range|list>            Specify days: '1-5' or '1,3,5'");
}
