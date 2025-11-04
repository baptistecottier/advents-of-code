#!/bin/bash
# AOC Development Environment Setup
# Run: source setup.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🎄 Setting up Advent of Code development environment..."

# Check Python 3 installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed. Please install Python 3.8+ first."
    return 1 2>/dev/null || exit 1
fi

echo "🐍 Python version: $(python3 --version)"

# Check if pip is available
if ! python3 -m pip --version &> /dev/null; then
    echo "❌ pip is required but not available. Please install pip first."
    return 1 2>/dev/null || exit 1
fi

# Install Python dependencies
if [[ -f "$SCRIPT_DIR/requirements.txt" ]]; then
    echo "📦 Installing Python dependencies..."
    
    # Try to install in user space first, fallback to system if needed
    if python3 -m pip install --user -r "$SCRIPT_DIR/requirements.txt" --quiet; then
        echo "✅ Dependencies installed successfully (user space)"
    elif python3 -m pip install -r "$SCRIPT_DIR/requirements.txt" --quiet; then
        echo "✅ Dependencies installed successfully (system)"
    else
        echo "⚠️  Failed to install dependencies. You may need to install manually:"
        echo "   python3 -m pip install -r requirements.txt"
    fi
else
    echo "⚠️  requirements.txt not found. Some features may not work."
fi

# Set up command aliases
echo "📝 Creating command aliases..."
alias aocp="python3 $SCRIPT_DIR/aocp"
alias aocr="python3 $SCRIPT_DIR/aocr"

# Generate completion if needed
if [[ ! -f "$SCRIPT_DIR/completions/aocp-completion.bash" ]]; then
    echo "📂 Generating completion scripts..."
    python3 "$SCRIPT_DIR/scripts/setup_completion.py" 2>/dev/null || echo "⚠️  Completion generation failed"
fi

# Load completion
if [[ -f "$SCRIPT_DIR/completions/aocp-completion.bash" ]]; then
    echo "🚀 Loading shell completion..."
    source "$SCRIPT_DIR/completions/aocp-completion.bash"
    echo "✅ AOC environment ready!"
else
    echo "⚠️  Completion not available"
    echo "✅ AOC commands ready (without completion)"
fi

echo ""
echo "Available commands:"
echo "  aocp 2024 1              # Run Python solution"
echo "  aocr 2024 1              # Run Rust solution"  
echo "  aocp --extract-examples  # Extract puzzle examples"
echo ""
echo "💡 To make permanent, add to your shell config:"
echo "   source $SCRIPT_DIR/scripts/enable_completion.sh"