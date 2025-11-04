# 📁 Project Structure

```
advents-of-code/
├── README.md                    # Main project documentation
├── requirements.txt             # 📦 Python dependencies  
├── setup.sh                     # 🚀 Daily environment loader (source this!)
│
├── aocp                         # 🐍 Python runner (main CLI tool)
├── aocr                         # 🦀 Rust runner (main CLI tool)
│
├── docs/                        # 📚 Documentation
│   ├── COMPLETION_TROUBLESHOOTING.md
│   └── SETUP_SCRIPTS.md
│
├── scripts/                     # 🛠️ Utility scripts
│   ├── initial_setup.sh         # 🚀 One-time setup for fresh clone
│   ├── enable_completion.sh     # For permanent shell configuration
│   ├── setup_completion.py      # Generates completion scripts
│   ├── scan_requirements.py     # Auto-detect Python dependencies
│   ├── setup_aoc_environment.sh # Environment setup utilities
│   ├── setup_completion_interactive.sh
│   └── install_completion.sh    # Completion installer
│
├── completions/                 # ⚡ Shell completion
│   ├── aocp-completion.bash     # Bash completion
│   └── _aocp_aocr               # Zsh completion
│

├── events/                      # 🎄 AOC Solutions
│   ├── year_2015/
│   ├── year_2016/
│   ├── ...
│   └── year_2025/
│
├── pythonfw/                   # 🐍 Python framework
│   └── __pycache__/
│
├── rustfw/                     # 🦀 Rust framework  
│   ├── src/
│   └── target/
│
└── build/                      # 🏗️ Build artifacts
```

## 🚀 Quick Start

```bash
# One-time setup (fresh clone)
./scripts/initial_setup.sh

# Daily usage - load environment
source setup.sh

# Use the tools
aocp 2024 1                     # Run Python solution
aocr 2024 1                     # Run Rust solution
aocp --help                     # Show help
```

## 🔧 Key Files

- **`scripts/initial_setup.sh`** - One-time setup for fresh clone (install deps, configure AOC)
- **`setup.sh`** - Daily environment loader, source this each session  
- **`requirements.txt`** - Python dependencies (aocd, requests)
- **`aocp`** - Python runner with full AOC integration
- **`aocr`** - Rust runner with Cargo integration  
- **`scripts/enable_completion.sh`** - Add to shell config for permanent setup