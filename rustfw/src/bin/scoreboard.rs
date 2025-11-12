#[derive(Debug, Clone)]
pub struct DayResult {
    pub day: u32,
    pub success: bool,
    pub part1: Option<String>,
    pub part2: Option<String>,
    pub error: Option<String>,
}

pub fn display_scoreboard(year: u32, days_to_run: &[u32], results: &[DayResult]) {
    let total_days = days_to_run.len();
    let successful_days = results.iter().filter(|r| r.success).count();
    
    // Only show detailed scoreboard for full year or many days
    if days_to_run.len() < 5 {
        return;
    }
    
    println!("\n{}", "=".repeat(70));
    println!("🏆 Scoreboard - Advent of Code {}", year);
    println!("{}", "=".repeat(70));
    println!("{:<6} {:<20} {:<42}", "Day", "Status", "Notes");
    println!("{}", "-".repeat(70));
    
    for result in results {
        let day_str = format!("{:02}", result.day);
        let (emoji, status) = if result.success {
            ("✅", "Complete")
        } else if let Some(ref err) = result.error {
            if err.contains("not found") {
                ("🚧", "Not solved")
            } else {
                ("❌", "Failed")
            }
        } else {
            ("❌", "Failed")
        };
        
        let notes = if result.success && result.part1.is_some() && result.part2.is_some() {
            format!("Part 1: {} | Part 2: {}", 
                result.part1.as_ref().unwrap_or(&"?".to_string()),
                result.part2.as_ref().unwrap_or(&"?".to_string()))
        } else if let Some(ref err) = result.error {
            err.chars().take(40).collect::<String>()
        } else {
            String::new()
        };
        
        println!("{:<6} {} {:<17} {:<42}", day_str, emoji, status, notes);
    }
    
    println!("{}", "=".repeat(70));
    
    // Calculate stars (simplified)
    let stars = results.iter()
        .filter(|r| r.success)
        .count() * 2;
    
    let percentage = if total_days > 0 {
        (successful_days * 100) / total_days
    } else {
        0
    };
    
    println!("📊 Summary: Total: {}, Successful: {}/{} ({}%), Stars: {} ⭐",
        total_days, successful_days, total_days, percentage, stars);
    println!("{}\n", "=".repeat(70));
}
