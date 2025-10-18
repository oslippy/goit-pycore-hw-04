from utils import get_file_content


def total_salary(path: str) -> tuple[int, float] | None:
    try:
        content = get_file_content(path)
    except Exception as e:
        print(e)
        return None
    salaries = []
    for line in content:
        if "," not in line:
            print(f"'{line.strip()}' format is incorrect.")
            continue
        developer, salary = line.strip().split(",")
        if not salary.isdigit():
            print(
                f"Salary must be a numeric type. Salary for developer {developer} has incorrect format."
            )
            continue
        salaries.append(float(salary))

    total = sum(salaries)
    return total, total / len(salaries)
