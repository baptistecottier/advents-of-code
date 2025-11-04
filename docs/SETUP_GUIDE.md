# 🛠️ Setup Guide

This guide covers setting up the Advent of Code development environment from scratch.

## 🚀 Quick Setup (Recommended)

For a fresh clone, run the automated setup:

```bash
git clone <your-repo-url>
cd advents-of-code
./scripts/initial_setup.sh
```

This script will:
- ✅ Check Python 3 installation
- 📦 Install required packages (`aocd`, `requests`)  
- 🔑 Help configure your AOC session token
- 📁 Create year structure for current year
- ⚡ Generate shell completion scripts
- 📚 Provide usage instructions

## 📋 Requirements

### System Requirements
- **Python 3.8+** - Download from [python.org](https://www.python.org/downloads/)
- **pip** - Usually comes with Python
- **Internet connection** - For downloading puzzles and submitting answers

### Python Packages
The project requires these packages (auto-installed by setup):

**Core Dependencies:**
- `advent-of-code-data` - AOC puzzle fetching and submission
- `requests` - HTTP requests (used by some solutions)

**Solution Dependencies (found across all years):**
- `numpy` - Mathematical computations and array operations
- `networkx` - Graph algorithms and network analysis  
- `z3-solver` - Constraint solving and theorem proving
- `parse` - Text parsing with format strings
- `regex` - Enhanced regular expressions
- `argcomplete` - Shell autocompletion (optional)
- `numexpr` - Fast numerical expression evaluation (optional)

**📊 Auto-detection:** Run `python3 scripts/scan_requirements.py` to automatically detect and update dependencies based on your actual solution files.

## 🔑 AOC Session Token

To automatically fetch puzzles and submit answers, you need your Advent of Code session token:

### Getting Your Token
1. Go to [adventofcode.com](https://adventofcode.com)
2. Log in to your account
3. Open browser developer tools (F12)
4. Navigate to **Application/Storage** → **Cookies** → `https://adventofcode.com`
5. Find the `session` cookie and copy its **Value**

### Setting Your Token
The setup script will prompt for this, or set it manually:

```bash
mkdir -p ~/.config/aocd
echo "YOUR_SESSION_TOKEN_HERE" > ~/.config/aocd/token
```

**⚠️ Keep your session token private!** Add `~/.config/aocd/token` to your `.gitignore`.

## 🐍 Virtual Environment (Optional but Recommended)

For isolated dependencies:

```bash
# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# Install dependencies  
pip install -r requirements.txt

# Now run setup
source setup.sh
```

## 📁 Project Structure After Setup

```
advents-of-code/
├── requirements.txt         # Python dependencies
├── setup.sh                # Daily environment loader
├── scripts/initial_setup.sh # One-time setup script
├── aocp / aocr             # CLI tools
├── events/year_YYYY/       # Solutions organized by year
│   └── day_DD/
│       ├── day_DD.py       # Python solution template
│       ├── day_DD.input    # Puzzle input (auto-downloaded)
│       └── day_DD.examples # Extracted examples (optional)
└── completions/            # Shell completion scripts
```

## 🔧 Manual Setup Steps

If you prefer to set up manually:

### 1. Install Dependencies
```bash
python3 -m pip install -r requirements.txt
```

### 2. Configure AOC Session
```bash
mkdir -p ~/.config/aocd
echo "YOUR_SESSION_TOKEN" > ~/.config/aocd/token
```

### 3. Generate Completions
```bash
python3 scripts/setup_completion.py
```

### 4. Load Environment
```bash
source setup.sh
```

## 🎯 Usage After Setup

### Daily Workflow
```bash
# Load environment (each terminal session)
source setup.sh

# Run solutions
aocp 2024 1                 # Python
aocr 2024 1                 # Rust (if available)

# Get help
aocp --help
```

### Features Available
- **Auto-input download**: Puzzle inputs saved automatically
- **Answer submission**: `--verify` flag to check answers
- **Example extraction**: `--examples` to test with examples
- **Shell completion**: Tab completion for years, days, flags

## 🔄 Permanent Shell Integration

To avoid running `source setup.sh` every time:

```bash
# Add to your shell config (.bashrc, .zshrc, etc.)
echo 'source /path/to/advents-of-code/scripts/enable_completion.sh' >> ~/.bashrc
```

## 🐛 Troubleshooting

### Common Issues

**"Python 3 not found"**
- Install Python 3.8+ from [python.org](https://www.python.org/downloads/)
- On macOS: `brew install python3`
- On Ubuntu: `sudo apt install python3 python3-pip`

**"aocd authentication failed"**  
- Check your session token is correct
- Token file should be: `~/.config/aocd/token`
- Make sure you're logged into AOC in your browser

**"Module not found"**
- Run: `python3 -m pip install -r requirements.txt`  
- Consider using a virtual environment

**"Completion not working"**
- Run: `source setup.sh` in your current terminal
- For permanent setup: `source scripts/enable_completion.sh`

### Getting Help

- Check [COMPLETION_TROUBLESHOOTING.md](COMPLETION_TROUBLESHOOTING.md)
- Review [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)  
- Run setup again: `./scripts/initial_setup.sh`

## 🎉 You're Ready!

After successful setup:
- ✅ Python environment configured
- ✅ AOC session token set
- ✅ Dependencies installed
- ✅ Shell completion active
- ✅ CLI tools ready to use

Happy coding! 🎄⭐