/// Utility functions for the CLI
pub fn _ensure_dir_exists(path: &str) -> std::io::Result<()> {
    std::fs::create_dir_all(path)
}

#[allow(dead_code)]
pub fn color(text: &str, color_name: &str) -> String {
    let code = match color_name {
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
