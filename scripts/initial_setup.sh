#!/bin/bash
# Initial Project Setup - Run once after cloning
# This script sets up everything needed for a fresh AOC environment

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "🎄 Initial Advent of Code Project Setup"
echo "========================================"

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install Python packages
install_python_deps() {
    echo "📦 Installing Python dependencies..."
    echo "This includes core packages (aocd, requests) and solution dependencies"
    echo "(numpy, networkx, z3-solver, parse, regex, etc.)"
    echo ""
    
    # Check if we should use virtual environment
    if [[ -z "$VIRTUAL_ENV" ]] && command_exists python3; then
        echo "💡 Consider using a virtual environment for isolation:"
        echo "   python3 -m venv .venv"
        echo "   source .venv/bin/activate"
        echo "   python3 -m pip install -r requirements.txt"
        echo ""
    fi
    
    # Install requirements
    if [[ -f "$PROJECT_ROOT/requirements.txt" ]]; then
        if python3 -m pip install -r "$PROJECT_ROOT/requirements.txt"; then
            echo "✅ Python dependencies installed"
        else
            echo "❌ Failed to install Python dependencies"
            echo "💡 Try: python3 -m pip install --user -r requirements.txt"
            return 1
        fi
    else
        echo "⚠️  requirements.txt not found"
        return 1
    fi
}

# Function to setup AOC session token
setup_aoc_session() {
    echo ""
    echo "🔑 AOC Session Token Setup"
    echo "To automatically fetch puzzles and submit answers, you need your session token."
    echo ""
    echo "1. Go to https://adventofcode.com"
    echo "2. Log in to your account" 
    echo "3. Open browser dev tools (F12)"
    echo "4. Go to Application/Storage -> Cookies -> https://adventofcode.com"
    echo "5. Find the 'session' cookie and copy its value"
    echo ""
    
    if [[ -f ~/.config/aocd/token ]] && [[ -s ~/.config/aocd/token ]]; then
        echo "✅ AOC session token already configured"
    else
        read -p "🔑 Enter your AOC session token (or press Enter to skip): " session_token
        if [[ -n "$session_token" ]]; then
            mkdir -p ~/.config/aocd
            echo "$session_token" > ~/.config/aocd/token
            echo "✅ Session token saved to ~/.config/aocd/token"
        else
            echo "⚠️  Skipping session token setup. You can set it later with:"
            echo "   mkdir -p ~/.config/aocd && echo 'YOUR_TOKEN' > ~/.config/aocd/token"
        fi
    fi
}

# Function to create year structure
create_year_structure() {
    local year=${1:-$(date +%Y)}
    echo "📁 Creating structure for year $year..."
    
    mkdir -p "events/year_$year"
    for day in {01..25}; do
        day_dir="events/year_$year/day_$day"
        mkdir -p "$day_dir"
        
        # Create template files if they don't exist
        if [[ ! -f "$day_dir/day_$day.py" ]]; then
            cat > "$day_dir/day_$day.py" << 'EOF'
def solver(data):
    """Solver for this day's puzzle."""
    # Part 1
    part1 = 0
    
    # Part 2  
    part2 = 0
    
    return part1, part2

if __name__ == "__main__":
    with open(f"day_{__file__[-5:-3]}.input", "r") as f:
        data = f.read().strip()
    
    result = solver(data)
    print(f"Part 1: {result[0]}")
    print(f"Part 2: {result[1]}")
EOF
        fi
    done
    
    echo "✅ Year $year structure created"
}

# Main setup process
main() {
    echo "🔍 Checking system requirements..."
    
    # Check Python 3
    if ! command_exists python3; then
        echo "❌ Python 3 is required but not installed."
        echo "💡 Install Python 3.8+ from: https://www.python.org/downloads/"
        exit 1
    fi
    
    python_version=$(python3 --version 2>&1 | cut -d' ' -f2)
    echo "✅ Python $python_version found"
    
    # Check pip
    if ! python3 -m pip --version >/dev/null 2>&1; then
        echo "❌ pip is required but not available."
        echo "💡 Install pip or use: python3 -m ensurepip --default-pip"
        exit 1
    fi
    
    echo "✅ pip available"
    
    # Install Python dependencies
    install_python_deps || {
        echo "❌ Failed to install dependencies"
        exit 1
    }
    
    # Setup AOC session token
    setup_aoc_session
    
    # Create current year structure  
    cd "$PROJECT_ROOT"
    current_year=$(date +%Y)
    if [[ ! -d "events/year_$current_year" ]]; then
        read -p "📁 Create structure for $current_year? (Y/n): " create_year
        if [[ "$create_year" != "n" && "$create_year" != "N" ]]; then
            create_year_structure "$current_year"
        fi
    else
        echo "✅ Year $current_year structure already exists"
    fi
    
    # Generate completion scripts
    echo "⚡ Setting up shell completion..."
    if python3 "$SCRIPT_DIR/setup_completion.py"; then
        echo "✅ Completion scripts generated"
    else
        echo "⚠️  Completion generation failed"
    fi
    
    echo ""
    echo "🎉 Setup Complete!"
    echo "=================="
    echo ""
    echo "🚀 Quick start:"
    echo "   source setup.sh                 # Load environment (run this each time)"
    echo "   aocp 2024 1                     # Run Python solution"
    echo "   aocr 2024 1                     # Run Rust solution"
    echo ""
    echo "💡 For permanent setup, add to your shell config:"
    echo "   echo 'source $PROJECT_ROOT/scripts/enable_completion.sh' >> ~/.bashrc"
    echo "   # or ~/.zshrc for zsh"
    echo ""
    echo "📚 Documentation available in docs/ directory"
}

# Run main function
main "$@"