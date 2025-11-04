#!/usr/bin/env python3
"""
Setup shell completion for aocp and aocr commands.
"""

import os
from pathlib import Path

def create_bash_completion():
    """Create bash completion script."""
    completion_script = '''#!/bin/bash
# Bash completion for aocp and aocr

_aocp_completion() {
    local cur prev opts cmd
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    cmd="${COMP_WORDS[0]}"
    
    # Available options
    opts="--help -h --days -e --examples -ev --examples-verbose --no-local --force --save-input --extract-examples --refresh-examples"
    
    # Check position in command line
    case "${COMP_CWORD}" in
        1)
            # First argument: year (2015-2025) or flags
            if [[ ${cur} == -* ]]; then
                COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
            else
                COMPREPLY=( $(compgen -W "2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025" -- ${cur}) )
            fi
            return 0
            ;;
        2)
            # Second argument: day (1-25) or flags (if prev is year)
            case "${prev}" in
                2015|2016|2017|2018|2019|2020|2021|2022|2023|2024|2025)
                    if [[ ${cur} == -* ]]; then
                        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
                    else
                        COMPREPLY=( $(compgen -W "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25" -- ${cur}) )
                    fi
                    return 0
                    ;;
                --days)
                    # Days format: 1-25, 1,2,3, or 1-5
                    COMPREPLY=( $(compgen -W "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 1-25 1,2,3 1-5" -- ${cur}) )
                    return 0
                    ;;
            esac
            ;;
    esac
    
    # Default: offer options if current word starts with -
    if [[ ${cur} == -* ]]; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    fi
}

_aocr_completion() {
    local cur prev opts cmd
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    cmd="${COMP_WORDS[0]}"
    
    # Available options  
    opts="--help -h --days -c --check -r --release --build-only -v --verbose --time --save-input --extract-examples --refresh-examples"
    
    # Check position in command line
    case "${COMP_CWORD}" in
        1)
            # First argument: year (2015-2025) or flags
            if [[ ${cur} == -* ]]; then
                COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
            else
                COMPREPLY=( $(compgen -W "2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025" -- ${cur}) )
            fi
            return 0
            ;;
        2)
            # Second argument: day (1-25) or flags (if prev is year)
            case "${prev}" in
                2015|2016|2017|2018|2019|2020|2021|2022|2023|2024|2025)
                    if [[ ${cur} == -* ]]; then
                        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
                    else
                        COMPREPLY=( $(compgen -W "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25" -- ${cur}) )
                    fi
                    return 0
                    ;;
                --days)
                    # Days format: 1-25, 1,2,3, or 1-5
                    COMPREPLY=( $(compgen -W "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 1-25 1,2,3 1-5" -- ${cur}) )
                    return 0
                    ;;
            esac
            ;;
    esac
    
    # Default: offer options if current word starts with -
    if [[ ${cur} == -* ]]; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    fi
}
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    
    # Available options  
    opts="--help -h --days -c --check -r --release --build-only -v --verbose --time --save-input --extract-examples --refresh-examples"
    
    case "${prev}" in
        aocr)
            # First argument: year (2015-2025)
            COMPREPLY=( $(compgen -W "2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025" -- ${cur}) )
            return 0
            ;;
        --days)
            # Days format: 1-25, 1,2,3, or 1-5
            COMPREPLY=( $(compgen -W "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 1-25 1,2,3 1-5" -- ${cur}) )
            return 0
            ;;
        2015|2016|2017|2018|2019|2020|2021|2022|2023|2024|2025)
            # Second argument: day (1-25)
            if [[ ${cur} == -* ]]; then
                COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
            else
                COMPREPLY=( $(compgen -W "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25" -- ${cur}) )
            fi
            return 0
            ;;
        *)
            ;;
    esac
    
    # Default: offer options if current word starts with -
    if [[ ${cur} == -* ]]; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    fi
}

# Register completions
complete -F _aocp_completion aocp
complete -F _aocr_completion aocr
'''
    return completion_script

def create_zsh_completion():
    """Create zsh completion script."""
    completion_script = '''#compdef aocp aocr

# Zsh completion for aocp and aocr

_aocp() {
    local context state line
    typeset -A opt_args
    
    _arguments -C \\
        '1: :_years' \\
        '2: :_days' \\
        '--help[Show help message]' \\
        '-h[Show help message]' \\
        '--days[Specify days to run]:days:' \\
        '-e[Test examples before running]' \\
        '--examples[Test examples before running]' \\
        '-ev[Test examples with verbose output]' \\
        '--examples-verbose[Test examples with verbose output]' \\
        '--no-local[Force use of remote input (bypass local files)]' \\
        '--force[Force run even if examples fail]' \\
        '--save-input[Save puzzle input to local .input file and exit]' \\
        '--extract-examples[Extract and display examples from puzzle description]' \\
        '--refresh-examples[Force refresh examples (ignore cached .examples files)]'
}

_aocr() {
    local context state line
    typeset -A opt_args
    
    _arguments -C \\
        '1: :_years' \\
        '2: :_days' \\
        '--help[Show help message]' \\
        '-h[Show help message]' \\
        '--days[Specify days to run]:days:' \\
        '-c[Check compilation only (cargo check)]' \\
        '--check[Check compilation only (cargo check)]' \\
        '-r[Build in release mode (optimized)]' \\
        '--release[Build in release mode (optimized)]' \\
        '--build-only[Build only, do not run]' \\
        '-v[Verbose cargo output]' \\
        '--verbose[Verbose cargo output]' \\
        '--time[Measure execution time]' \\
        '--save-input[Save puzzle input to local .input file]' \\
        '--extract-examples[Extract and display examples from puzzle description]' \\
        '--refresh-examples[Force refresh examples (ignore cached .examples files)]'
}

_years() {
    local years
    years=(2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025)
    _describe 'year' years
}

_days() {
    local days
    days=(1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25)
    _describe 'day' days
}

case "$service" in
    aocp)
        _aocp "$@"
        ;;
    aocr) 
        _aocr "$@"
        ;;
esac
'''
    return completion_script

def setup_completions():
    """Set up shell completions."""
    print("🔧 Setting up shell completions for aocp and aocr...")
    
    # Create completions directory (go up one level from scripts/)
    completions_dir = Path("../completions")
    completions_dir.mkdir(exist_ok=True)
    
    # Create bash completion
    bash_completion_path = completions_dir / "aocp-completion.bash"
    with open(bash_completion_path, 'w', encoding='utf-8') as f:
        f.write(create_bash_completion())
    print(f"✅ Created bash completion: {bash_completion_path}")
    
    # Create zsh completion  
    zsh_completion_path = completions_dir / "_aocp_aocr"
    with open(zsh_completion_path, 'w', encoding='utf-8') as f:
        f.write(create_zsh_completion())
    print(f"✅ Created zsh completion: {zsh_completion_path}")
    
    # Make scripts executable
    os.chmod(bash_completion_path, 0o755)
    os.chmod(zsh_completion_path, 0o755)
    
    print("\\n📋 To enable completions:")
    print("\\nFor Bash:")
    print(f"  source {bash_completion_path.absolute()}")
    print("  # Or add this line to your ~/.bashrc")
    
    print("\\nFor Zsh:")
    print(f"  # Add {completions_dir.absolute()} to your fpath in ~/.zshrc:")
    print(f"  fpath=({completions_dir.absolute()} $fpath)")
    print("  autoload -U compinit && compinit")
    
    print("\\n🚀 Quick setup for current session:")
    shell = os.environ.get('SHELL', '')
    if 'zsh' in shell:
        print(f"  source {bash_completion_path.absolute()}")
    elif 'bash' in shell:
        print(f"  source {bash_completion_path.absolute()}")
    
    print("\\n💡 Test with: aocp <TAB> or aocr <TAB>")

if __name__ == "__main__":
    setup_completions()