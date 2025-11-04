# AOC CLI tools with completion
# Use relative paths to make it portable
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
alias aocp="python3 $SCRIPT_DIR/aocp"
alias aocr="python3 $SCRIPT_DIR/aocr"
source "$SCRIPT_DIR/completions/aocp-completion.bash"
