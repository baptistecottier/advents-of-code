def preprocessing(puzzle_input):
    reports = []
    for report in puzzle_input.splitlines():
        data = [int(item) for item in report.split()]
        reports.append(data)
    return reports

def solver(reports):
    nearly_safe = 0
    very_safe = 0
    for report in reports:
        if is_report_safe(report):
            very_safe += 1
        else :
            nearly_safe += any(is_report_safe(report[:i] + report[i + 1:]) for i in range(len(report)))
    yield very_safe
    yield nearly_safe + very_safe
            
def is_report_safe(report):
    values = [a - b for a, b in zip(report[:-1], report[1:])]
    return all(abs(v) < 4 for v in values) and (all(v > 0 for v in values) or all(v < 0 for v in values))