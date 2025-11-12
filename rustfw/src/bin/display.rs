use regex::Regex;

pub fn parse_output(output: &str) -> (Option<String>, Option<String>) {
    let output = output.trim();
    
    // Try to parse tuple format with optional quotes: (val1, val2) or ("val1", "val2")
    if let Ok(re) = Regex::new(r#"^\s*\(\s*["\']?([^",\)]+)["\']?\s*,\s*["\']?([^",\)]+)["\']?\s*\)\s*$"#) {
        if let Some(caps) = re.captures(output) {
            if let (Some(part1_cap), Some(part2_cap)) = (caps.get(1), caps.get(2)) {
                let part1 = part1_cap.as_str().trim().to_string();
                let part2 = part2_cap.as_str().trim().to_string();
                return (Some(part1), Some(part2));
            }
        }
    }
    
    // Try to parse individual lines with "Part 1:" and "Part 2:" format
    let lines: Vec<&str> = output.lines().collect();
    let mut part1 = None;
    let mut part2 = None;
    
    if let Ok(part1_re) = Regex::new(r"(?i)(?:Part\s*1|Part\s*A|P1)[\s:]+([^\s]+)") {
        if let Ok(part2_re) = Regex::new(r"(?i)(?:Part\s*2|Part\s*B|P2)[\s:]+([^\s]+)") {
            for line in &lines {
                let trimmed = line.trim();
                if !trimmed.is_empty() {
                    if part1.is_none() {
                        if let Some(caps) = part1_re.captures(trimmed) {
                            if let Some(m) = caps.get(1) {
                                part1 = Some(m.as_str().to_string());
                            }
                        }
                    }
                    if part2.is_none() {
                        if let Some(caps) = part2_re.captures(trimmed) {
                            if let Some(m) = caps.get(1) {
                                part2 = Some(m.as_str().to_string());
                            }
                        }
                    }
                }
            }
        }
    }
    
    (part1, part2)
}

pub fn parse_and_display_output(output: &str, _year: u32, _day: u32) {
    let output = output.trim();
    
    // Try to parse tuple format with optional quotes: (val1, val2) or ("val1", "val2")
    if let Ok(re) = Regex::new(r#"^\s*\(\s*["\']?([^",\)]+)["\']?\s*,\s*["\']?([^",\)]+)["\']?\s*\)\s*$"#) {
        if let Some(caps) = re.captures(output) {
            if let (Some(part1_cap), Some(part2_cap)) = (caps.get(1), caps.get(2)) {
                let part1 = part1_cap.as_str().trim();
                let part2 = part2_cap.as_str().trim();
                println!("  🥇 Part 1: {}", part1);
                println!("  🥈 Part 2: {}", part2);
                return;
            }
        }
    }
    
    // Try to parse individual lines with "Part 1:" and "Part 2:" format
    let lines: Vec<&str> = output.lines().collect();
    let mut part1_found = false;
    let mut part2_found = false;
    
    if let Ok(part1_re) = Regex::new(r"(?i)(?:Part\s*1|Part\s*A|P1)[\s:]+([^\s]+)") {
        if let Ok(part2_re) = Regex::new(r"(?i)(?:Part\s*2|Part\s*B|P2)[\s:]+([^\s]+)") {
            for line in &lines {
                let trimmed = line.trim();
                if !trimmed.is_empty() {
                    if !part1_found {
                        if let Some(caps) = part1_re.captures(trimmed) {
                            if let Some(m) = caps.get(1) {
                                println!("  🥇 Part 1: {}", m.as_str());
                                part1_found = true;
                            }
                        }
                    }
                    if !part2_found {
                        if let Some(caps) = part2_re.captures(trimmed) {
                            if let Some(m) = caps.get(1) {
                                println!("  🥈 Part 2: {}", m.as_str());
                                part2_found = true;
                            }
                        }
                    }
                }
            }
        }
    }
    
    // If no structured format detected, show raw output
    if !part1_found && !part2_found {
        println!("  📄 Output:");
        for line in output.lines() {
            if !line.trim().is_empty() {
                println!("    {}", line);
            }
        }
    }
}

pub fn display_extracted_examples(year: u32, day: u32, _force_refresh: bool) {
    println!("📖 Extracting examples from puzzle description...");
    
    let examples = extract_examples(year, day);
    if !examples.is_empty() {
        println!("  📋 Extracted {} examples:", examples.len());
        for (i, (input, expected)) in examples.iter().enumerate() {
            let preview = if input.len() > 50 {
                format!("{}...", &input[..50])
            } else {
                input.clone()
            };
            println!("    {}. Input: {}", i + 1, preview);
            if let Some(exp) = expected {
                println!("       Expected: {}", exp);
            }
        }
    } else {
        println!("  ❓ No examples extracted");
    }
}

fn extract_examples(year: u32, day: u32) -> Vec<(String, Option<String>)> {
    // Known examples for demonstration
    let known_examples = vec![
        // 2015 Day 1
        ((2015, 1), vec![
            ("(())".to_string(), Some("0".to_string())),
            ("()()".to_string(), Some("0".to_string())),
            ("((((".to_string(), Some("4".to_string())),
        ]),
        // 2020 Day 1
        ((2020, 1), vec![
            ("1721\n979\n366\n299\n675\n1456".to_string(), Some("514579".to_string())),
        ]),
    ];
    
    for ((y, d), examples) in known_examples {
        if y == year && d == day {
            return examples;
        }
    }
    
    Vec::new()
}

fn _color_text(text: &str, color: &str) -> String {
    let code = match color {
        "red" => "31",
        "green" => "32",
        "yellow" => "33",
        "blue" => "34",
        "magenta" => "35",
        "cyan" => "36",
        _ => return text.to_string(),
    };
    format!("\x1b[{}m{}\x1b[0m", code, text)
}
