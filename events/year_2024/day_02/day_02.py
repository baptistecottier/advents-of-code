"""
Advent of Code - Year 2024 - Day 2
https://adventofcode.com/2024/day/2
"""


def preprocessing(puzzle_input: str) -> list[list[int]]:
    """
    Parses the puzzle input string into a list of lists of integers, where each inner list
    represents a report.
    """
    reports = []
    for report in puzzle_input.splitlines():
        data = list(map(int, report.split()))
        reports.append(data)
    return reports


def solver(reports: list[list[int]]) -> tuple[int, int]:
    """
    Analyzes a list of reports to count how many are very safe and how many are nearly safe by
    checking safety criteria.
    """
    nearly_safe = 0
    very_safe = 0
    for report in reports:
        if is_report_safe(report):
            very_safe += 1
        else:
            if any(is_report_safe(report[:i] + report[i + 1:])
                   for i in range(len(report))):
                nearly_safe += 1
    return very_safe, nearly_safe + very_safe


def is_report_safe(report: list[int]) -> bool:
    """
    Determines if a report is safe by checking if consecutive differences are less than 4 in
    absolute value and all differences have the same sign.
    """
    differences = [a - b for a, b in zip(report[:-1], report[1:])]
    return (all(abs(diff) < 4 for diff in differences)
            and (all(diff > 0 for diff in differences)
                 or all(diff < 0 for diff in differences)))
