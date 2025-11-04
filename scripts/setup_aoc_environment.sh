#!/bin/bash
# Complete AOC setup with working completion

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BIN_DIR="$SCRIPT_DIR/bin"

echo "🔧 Setting up AOC development environment..."

# Create bin directory if it doesn't exist
mkdir -p "$BIN_DIR"

# Create executable wrapper scripts
cat > "$BIN_DIR/aocp" << 'EOF'
#!/bin/bash
cd "$(dirname "$0")/.."
exec python3 aocp "$@"
EOF

cat > "$BIN_DIR/aocr" << 'EOF'
#!/bin/bash
cd "$(dirname "$0")/.."
exec python3 aocr "$@"
EOF

# Make them executable
chmod +x "$BIN_DIR/aocp" "$BIN_DIR/aocr"

echo "✅ Created executable wrappers in bin/"

# Add bin directory to PATH for this session
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    export PATH="$BIN_DIR:$PATH"
    echo "✅ Added $BIN_DIR to PATH"
fi

# Test the commands work
echo "🧪 Testing commands..."
if "$BIN_DIR/aocp" --help >/dev/null 2>&1; then
    echo "✅ aocp command works"
else
    echo "❌ aocp command failed"
fi

if "$BIN_DIR/aocr" --help >/dev/null 2>&1; then
    echo "✅ aocr command works"  
else
    echo "❌ aocr command failed"
fi

# Generate completion if it doesn't exist
if [[ ! -f "$SCRIPT_DIR/completions/aocp-completion.bash" ]]; then
    echo "📂 Generating completion scripts..."
    python3 "$SCRIPT_DIR/setup_completion.py"
fi

# Source completion
if [[ -f "$SCRIPT_DIR/completions/aocp-completion.bash" ]]; then
    echo "🚀 Loading shell completion..."
    source "$SCRIPT_DIR/completions/aocp-completion.bash"
    echo "✅ Completion loaded!"
fi

echo ""
echo "🎉 AOC development environment ready!"
echo ""
echo "Commands available:"
echo "  aocp 2024 1          # Run Python solution"
echo "  aocr 2024 1          # Run Rust solution"
echo "  aocp --help          # Show help"
echo ""
echo "Test completion:"
echo "  aocp <TAB>           # Should complete years"
echo "  aocp 2024 <TAB>      # Should complete days"  
echo "  aocp --<TAB>         # Should complete options"
echo ""
echo "💡 To make permanent, add to your shell config:"
echo "   export PATH=\"$BIN_DIR:\$PATH\""
echo "   source \"$SCRIPT_DIR/completions/aocp-completion.bash\""