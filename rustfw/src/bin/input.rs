use std::fs;
use std::path::PathBuf;

#[allow(dead_code)]
pub fn load_input(year: u32, day: u32) -> Result<String, String> {
    load_input_from_path(year, day, None)
}

pub fn load_input_from_path(year: u32, day: u32, project_root: Option<PathBuf>) -> Result<String, String> {
    let day_str = format!("{:02}", day);
    
    let input_path = if let Some(root) = project_root {
        root.join(format!("events/year_{}/day_{}/day_{}.input", year, day_str, day_str))
    } else {
        PathBuf::from(format!("./events/year_{}/day_{}/day_{}.input", year, day_str, day_str))
    };
    
    // Try to load local input first
    if input_path.exists() {
        match fs::read_to_string(&input_path) {
            Ok(content) => {
                let trimmed = content.trim_end_matches('\n').to_string();
                if !trimmed.is_empty() {
                    return Ok(trimmed);
                }
            }
            Err(_) => {}
        }
    }
    
    // Try to fetch from aocd
    fetch_input_from_aocd(year, day)
}

fn fetch_input_from_aocd(year: u32, day: u32) -> Result<String, String> {
    // This would require calling Python or using a Rust aocd client
    // For now, return a helpful error message
    Err(format!(
        "Input file not found at events/year_{}/day_{:02}/day_{:02}.input\n\
         You can fetch it using: aocp {} {} --save-input",
        year, day, day, year, day
    ))
}

pub fn save_input_to_file(year: u32, day: u32, verbose: bool) -> bool {
    let day_str = format!("{:02}", day);
    let dir_path = PathBuf::from(format!("./events/year_{}/day_{}", year, day_str));
    let input_path = dir_path.join(format!("day_{}.input", day_str));
    
    // Create directory if it doesn't exist
    if let Err(e) = fs::create_dir_all(&dir_path) {
        if verbose {
            eprintln!("❌ Failed to create directory: {}", e);
        }
        return false;
    }
    
    // Check if file already exists and has content
    if input_path.exists() {
        if let Ok(metadata) = input_path.metadata() {
            if metadata.len() > 0 {
                if verbose {
                    println!("  📁 Input file already exists: {}", input_path.display());
                }
                return true;
            }
        }
    }
    
    // Try to fetch from aocd (would require Python subprocess or Rust aocd client)
    match fetch_input_from_aocd_impl(year, day) {
        Ok(content) => {
            match fs::write(&input_path, &content) {
                Ok(_) => {
                    if verbose {
                        println!("  💾 Saved input to: {}", input_path.display());
                    }
                    true
                }
                Err(e) => {
                    if verbose {
                        eprintln!("❌ Failed to write input: {}", e);
                    }
                    false
                }
            }
        }
        Err(e) => {
            if verbose {
                eprintln!("❌ Failed to fetch input: {}", e);
            }
            false
        }
    }
}

fn fetch_input_from_aocd_impl(year: u32, day: u32) -> Result<String, String> {
    // Try to call the Python aocd library via subprocess
    // This is a fallback - ideally would use a Rust aocd client
    
    let output = std::process::Command::new("python3")
        .arg("-c")
        .arg(format!(
            "from aocd.models import Puzzle; p = Puzzle({}, {}); print(p.input_data)",
            year, day
        ))
        .output()
        .map_err(|e| format!("Failed to call Python: {}", e))?;
    
    if output.status.success() {
        Ok(String::from_utf8_lossy(&output.stdout).trim_end_matches('\n').to_string())
    } else {
        let stderr = String::from_utf8_lossy(&output.stderr);
        Err(format!("aocd error: {}", stderr))
    }
}
