#!/bin/bash
# AOC Shell Completion - User-friendly setup

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🎄 AOC Shell Completion Setup"
echo "=============================="
echo ""

# Step 1: Create aliases
echo "📝 Step 1: Setting up command aliases..."
alias aocp="python3 $SCRIPT_DIR/aocp"
alias aocr="python3 $SCRIPT_DIR/aocr" 

# Step 2: Load completion
echo "🚀 Step 2: Loading shell completion..."
if [[ -f "$SCRIPT_DIR/completions/aocp-completion.bash" ]]; then
    source "$SCRIPT_DIR/completions/aocp-completion.bash"
    echo "✅ Completion loaded successfully!"
else
    echo "❌ Completion file not found. Run: python3 setup_completion.py"
    exit 1
fi

# Step 3: Test
echo ""
echo "🧪 Step 3: Testing setup..."
if command -v aocp >/dev/null 2>&1; then
    echo "✅ aocp command available"
else
    echo "❌ aocp command not found"
fi

if complete -p aocp >/dev/null 2>&1; then
    echo "✅ aocp completion registered"
else
    echo "❌ aocp completion not registered"
fi

echo ""
echo "🎉 Setup complete! Try these commands:"
echo ""
echo "  aocp --help             # Show help"
echo "  aocp <TAB>              # Complete years (2015, 2016...)"
echo "  aocp 2024 <TAB>         # Complete days (1, 2, 3...)"  
echo "  aocp --<TAB>            # Complete flags (--help, --examples...)"
echo ""
echo "💡 To make permanent, add this line to your ~/.bashrc or ~/.zshrc:"
echo "   source $SCRIPT_DIR/enable_completion.sh"
echo ""

# Create a permanent setup file
cat > "$SCRIPT_DIR/enable_completion.sh" << EOF
# AOC CLI tools with completion
alias aocp="python3 $SCRIPT_DIR/aocp"
alias aocr="python3 $SCRIPT_DIR/aocr"
source "$SCRIPT_DIR/completions/aocp-completion.bash"
EOF

echo "📄 Created enable_completion.sh for permanent setup"