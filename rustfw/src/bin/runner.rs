use crate::args::Args;
use crate::input;
use crate::display;
use std::process::{Command, Stdio};
use std::path::PathBuf;
use std::io::Write;

fn find_project_root() -> Result<PathBuf, String> {
    // First check if we're already in the project
    let current = std::env::current_dir()
        .map_err(|e| format!("Failed to get current directory: {}", e))?;
    
    if current.join("events").exists() && current.join("rustfw").exists() {
        return Ok(current);
    }
    
    // Search upward for project root (containing 'events' and 'rustfw')
    let mut current = current.clone();
    for _ in 0..10 {
        if current.join("events").exists() && current.join("rustfw").exists() {
            return Ok(current);
        }
        if !current.pop() {
            break;
        }
    }
    
    Err("Could not find project root. Make sure you're in the advents-of-code directory or a subdirectory.".to_string())
}

pub fn run_day(day_num: u32, year: u32, args: &Args) -> Result<(bool, Option<String>, Option<String>), String> {
    let day_str = format!("{:02}", day_num);
    println!("\n🦀 Advent of Code Rust - Year {} - Day {}", year, day_str);
    
    // Find project root
    let project_root = find_project_root()?;
    
    // Check if solver exists
    let solver_path = project_root.join(format!("events/year_{}/day_{}/day_{}.rs", year, day_str, day_str));
    if !solver_path.exists() {
        eprintln!("🚧 Rust solver not found: {}", solver_path.display());
        return Ok((false, None, None));
    }
    
    // Save input if requested
    if args.save_input {
        if input::save_input_to_file(year, day_num, true) {
            println!("  ✅ Input saved successfully");
            return Ok((true, None, None));
        } else {
            eprintln!("❌ Failed to save input");
            return Ok((false, None, None));
        }
    }
    
    // Extract examples if requested
    if args.extract_examples || args.refresh_examples {
        display::display_extracted_examples(year, day_num, args.refresh_examples);
    }
    
    // Check if input file exists, auto-save if needed
    let input_path = project_root.join(format!("events/year_{}/day_{}/day_{}.input", year, day_str, day_str));
    if !input_path.exists() || input_path.metadata().ok().map(|m| m.len()) == Some(0) {
        if input::save_input_to_file(year, day_num, false) {
            println!("  💾 Input auto-saved for future use");
        }
    }
    
    // Load input with project root path
    let input_data = match input::load_input_from_path(year, day_num, Some(project_root.clone())) {
        Ok(data) => data,
        Err(e) => {
            eprintln!("⚠️  Could not load input: {}", e);
            String::new()
        }
    };
    
    // Build and run the solver from the rustfw directory
    let binary_name = format!("{}-{}", year, day_str);
    
    println!("🔧 Building and running {}...", binary_name);
    
    // Change to rustfw directory
    let rustfw_dir = project_root.join("rustfw");
    let original_dir = std::env::current_dir()
        .map_err(|e| format!("Failed to get current directory: {}", e))?;
    
    std::env::set_current_dir(&rustfw_dir)
        .map_err(|e| format!("Failed to change directory to {}: {}", rustfw_dir.display(), e))?;
    
    let mut cargo_cmd = Command::new("cargo");
    cargo_cmd.arg("run").arg("--bin").arg(&binary_name);
    
    if args.release {
        cargo_cmd.arg("--release");
    }
    
    // Pass input via stdin
    let mut child = cargo_cmd
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .map_err(|e| format!("Failed to spawn cargo: {}", e))?;
    
    if let Some(mut stdin) = child.stdin.take() {
        stdin.write_all(input_data.as_bytes())
            .map_err(|e| format!("Failed to write input: {}", e))?;
    }
    
    let output = child.wait_with_output()
        .map_err(|e| format!("Failed to wait for process: {}", e))?;
    

    let _ = std::env::set_current_dir(&original_dir);
    
    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        eprintln!("❌ Solver failed");
        if !stderr.is_empty() {
            eprintln!("{}", stderr);
        }
        return Ok((false, None, None));
    }
    
    let stdout = String::from_utf8_lossy(&output.stdout);
    if !stdout.is_empty() {
        println!("📊 Results:");
        let (part1, part2) = display::parse_output(&stdout);
        display::parse_and_display_output(&stdout, year, day_num);
        println!("✅ Execution completed!");
        return Ok((true, part1, part2));
    }
    
    println!("✅ Execution completed!");
    Ok((true, None, None))
}
