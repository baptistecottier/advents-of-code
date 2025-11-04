# 🔧 AOC Shell Completion Troubleshooting

If autocompletion isn't working, try these steps:

## Quick Fix (Current Session)
```bash
# Run this in your terminal:
cd /path/to/advents-of-code
source setup_completion_interactive.sh
```

## Common Issues & Solutions

### 1. "Command not found: aocp"
**Problem**: The command aliases aren't set up.
**Solution**: 
```bash
# Set up aliases manually:
alias aocp="python3 /path/to/advents-of-code/aocp"
alias aocr="python3 /path/to/advents-of-code/aocr"
```

### 2. "Completion not working"
**Problem**: Bash completion not loaded.
**Solution**:
```bash
# Load completion manually:
source /path/to/advents-of-code/completions/aocp-completion.bash

# Verify it's loaded:
complete -p aocp
# Should show: complete -F _aocp_completion aocp
```

### 3. "Permission denied"
**Problem**: Scripts aren't executable.
**Solution**:
```bash
# Don't need executable permissions - use python3 directly:
python3 aocp --help  # This should work
```

### 4. "Completion shows wrong suggestions"
**Problem**: Completion cache or old completions.
**Solution**:
```bash
# Clear and reload:
complete -r aocp aocr  # Remove old completions
source completions/aocp-completion.bash  # Reload
```

## Test Completion
After setup, these should work:
```bash
aocp <TAB>        # Shows: 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025
aocp 2024 <TAB>   # Shows: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25  
aocp --<TAB>      # Shows: --help --days --examples --extract-examples --refresh-examples etc.
```

## Permanent Setup

### For Bash (~/.bashrc):
```bash
# Add to ~/.bashrc:
source /path/to/advents-of-code/enable_completion.sh
```

### For Zsh (~/.zshrc):
```bash
# Add to ~/.zshrc:
autoload -U +X bashcompinit && bashcompinit
source /path/to/advents-of-code/enable_completion.sh
```

## Manual Verification
Check if everything is set up correctly:
```bash
# 1. Check commands exist
type aocp          # Should show alias or function
type aocr          # Should show alias or function

# 2. Check completion is registered  
complete -p aocp   # Should show: complete -F _aocp_completion aocp
complete -p aocr   # Should show: complete -F _aocr_completion aocr

# 3. Test completion functions exist
type _aocp_completion  # Should show: _aocp_completion is a shell function
type _aocr_completion  # Should show: _aocr_completion is a shell function

# 4. Test commands work
aocp --help        # Should show usage
aocr --help        # Should show usage
```

## Still Not Working?
If completion still doesn't work:
1. Make sure you're using bash (not zsh/fish) 
2. Try in a fresh terminal session
3. Check bash version: `bash --version` (needs 4.0+)
4. Use the commands without completion:
   ```bash
   python3 aocp 2024 1
   python3 aocr 2024 1
   ```