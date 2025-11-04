#!/usr/bin/env bash
# Auto-install completion for aocp and aocr

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMPLETIONS_DIR="$SCRIPT_DIR/completions"

echo "🔧 Installing shell completions for aocp and aocr..."

# Detect shell
if [[ -n "$ZSH_VERSION" ]]; then
    SHELL_TYPE="zsh"
elif [[ -n "$BASH_VERSION" ]]; then
    SHELL_TYPE="bash"  
else
    echo "⚠️  Unsupported shell. Defaulting to bash completion."
    SHELL_TYPE="bash"
fi

# Create completion files if they don't exist
if [[ ! -d "$COMPLETIONS_DIR" ]]; then
    echo "📂 Creating completion files..."
    python3 "$SCRIPT_DIR/setup_completion.py"
fi

case "$SHELL_TYPE" in
    "zsh")
        echo "🐚 Setting up zsh completion..."
        
        # Add to fpath if not already there
        if [[ ":$fpath:" != *":$COMPLETIONS_DIR:"* ]]; then
            fpath=("$COMPLETIONS_DIR" $fpath)
        fi
        
        # Reload completions
        autoload -U compinit && compinit -u
        
        echo "✅ Zsh completion installed!"
        echo "💡 Add this to your ~/.zshrc for persistence:"
        echo "   fpath=($COMPLETIONS_DIR \$fpath)"
        echo "   autoload -U compinit && compinit"
        ;;
        
    "bash")
        echo "🐚 Setting up bash completion..."
        
        # Source the completion script
        source "$COMPLETIONS_DIR/aocp-completion.bash"
        
        echo "✅ Bash completion installed!"
        echo "💡 Add this to your ~/.bashrc for persistence:"
        echo "   source $COMPLETIONS_DIR/aocp-completion.bash"
        ;;
esac

echo ""
echo "🚀 Test completions:"
echo "   aocp <TAB>      # Should show years: 2015 2016 ..."
echo "   aocp 2024 <TAB> # Should show days: 1 2 3 ..."
echo "   aocp --<TAB>    # Should show flags: --help --examples ..."
echo ""
echo "   aocr <TAB>      # Should show years: 2015 2016 ..."
echo "   aocr 2024 <TAB> # Should show days: 1 2 3 ..."
echo "   aocr --<TAB>    # Should show flags: --help --check ..."