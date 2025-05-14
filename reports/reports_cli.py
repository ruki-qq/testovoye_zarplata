def print_department_data(department, name, hours, rate, payout):
    design_header = f"| {department}    | Name            | Hours | Rate | Payout   |"
    design_separator = "|-----------|-----------------|-------|------|----------|"
    design_rows = (
        f"|           | {name}      | {hours}   | {rate}   | ${payout}    |",
    )

    print(design_header)
    print(design_separator)
    print("\n".join(design_rows))
    print()  # Add space between sections


if __name__ == "__main__":
    print_department_data()
