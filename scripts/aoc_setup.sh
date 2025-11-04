#!/bin/bash
# Enhanced completion setup with aliases

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🔧 Setting up AOC CLI tools with completion..."

# Create aliases for aocp and aocr
echo "📝 Creating shell aliases..."

cat << 'EOF' > "$SCRIPT_DIR/aoc_aliases.sh"
# AOC CLI aliases
alias aocp='python3 "$SCRIPT_DIR/aocp"'
alias aocr='python3 "$SCRIPT_DIR/aocr"'

# Add current directory to PATH for direct execution
export PATH="$SCRIPT_DIR:$PATH"
EOF

# Source the aliases
source "$SCRIPT_DIR/aoc_aliases.sh"

# Create and source completion
if [[ -f "$SCRIPT_DIR/completions/aocp-completion.bash" ]]; then
    echo "🚀 Loading bash completion..."
    source "$SCRIPT_DIR/completions/aocp-completion.bash"
    echo "✅ Completion loaded!"
else
    echo "📂 Creating completion files..."
    python3 "$SCRIPT_DIR/setup_completion.py"
    if [[ -f "$SCRIPT_DIR/completions/aocp-completion.bash" ]]; then
        source "$SCRIPT_DIR/completions/aocp-completion.bash"
        echo "✅ Completion loaded!"
    fi
fi

echo ""
echo "🎉 AOC CLI ready!"
echo ""
echo "Test with:"
echo "  aocp <TAB>      # Should show years"  
echo "  aocp 2024 <TAB> # Should show days"
echo "  aocp --<TAB>    # Should show flags"
echo ""
echo "💡 To make permanent, add this to your shell config:"
echo "   source $SCRIPT_DIR/aoc_setup.sh"