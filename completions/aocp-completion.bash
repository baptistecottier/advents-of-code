#!/bin/bash
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

# Register completions
complete -F _aocp_completion aocp
complete -F _aocr_completion aocr
