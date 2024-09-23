def print_report(incomes):
    cumulative_total = 0
    for month, income in enumerate(incomes, start=1):
        cumulative_total += income
        print(f"Month {month} - Income: ${income:>8.2f}         Total: ${cumulative_total:>8.2f}")
