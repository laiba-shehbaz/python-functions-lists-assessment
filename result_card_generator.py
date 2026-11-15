"""
Task 1 - Student Result Card Generator
Topics: functions (def, parameters, return) and string manipulation.

Asks for one student's details, validates every input, calculates the
result and prints a formatted result card.
"""

SUBJECTS = ["English", "Mathematics", "Physics", "Chemistry", "Computer Science"]
MAX_PER_SUBJECT = 100      # every subject is marked out of 100
SUBJECT_PASS_MARK = 40     # any subject below this forces an overall Fail


def format_name(name):
    """Clean a name: strip outer spaces, collapse inner spaces, Title Case."""
    cleaned = name.strip().title()
    return " ".join(cleaned.split())


def get_valid_name():
    """Keep asking until the name contains only letters and . - ' characters."""
    while True:
        name = format_name(input("Enter student name: "))
        # Remove allowed punctuation/spaces; what is left must be letters only
        letters_only = name
        for allowed in (" ", ".", "-", "'"):
            letters_only = letters_only.replace(allowed, "")
        if letters_only.isalpha():
            return name
        print("  Invalid name. Use letters only (spaces, '.', '-' and ' allowed).")


def get_valid_roll_number():
    """Keep asking until the roll number contains digits only."""
    while True:
        roll = input("Enter roll number (digits only): ").strip()
        if roll.isdigit():  # rejects empty text, letters, spaces, '-', '.'
            return roll
        print("  Invalid roll number. Digits only, e.g. 1024.")


def get_valid_marks(subject):
    """Ask for marks in one subject until a number from 0 to 100 is entered."""
    while True:
        raw = input(f"Enter marks in {subject} (0-100): ").strip()
        try:
            marks = float(raw)
        except ValueError:
            print("  Invalid input. Please enter a number.")
            continue
        # Chained comparison is also False for 'nan', so nan is rejected too
        if 0 <= marks <= MAX_PER_SUBJECT:
            return marks
        print("  Marks must be between 0 and 100.")


def calculate_percentage(total, max_total):
    """Return total as a percentage of max_total (0 if max_total is 0)."""
    if max_total == 0:
        return 0.0
    return total / max_total * 100


def get_grade(percentage):
    """Return the letter grade for an overall percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    return "Fail"


def get_final_status(marks_list, grade):
    """Return 'Fail' if the grade is Fail or ANY subject is below 40."""
    # The subject rule overrides the overall percentage
    if grade == "Fail" or min(marks_list) < SUBJECT_PASS_MARK:
        return "Fail"
    return "Pass"


def build_result_card(name, roll, marks_list, total, max_total, percentage, grade, status):
    """Build the formatted result card text using f-strings."""
    line = "=" * 46
    thin = "-" * 46
    rows = ""
    for subject, mark in zip(SUBJECTS, marks_list):
        flag = "  <- below 40" if mark < SUBJECT_PASS_MARK else ""
        rows += f"  {subject:<20}{mark:>8g} / {MAX_PER_SUBJECT}{flag}\n"
    return (
        f"\n{line}\n"
        f"{'STUDENT RESULT CARD':^46}\n"
        f"{line}\n"
        f"  Name         : {name}\n"
        f"  Roll Number  : {roll}\n"
        f"{thin}\n"
        f"  {'Subject':<20}{'Marks':>8}\n"
        f"{thin}\n"
        f"{rows}"
        f"{thin}\n"
        f"  Total Marks  : {total:g} / {max_total}\n"
        f"  Percentage   : {percentage:.2f}%\n"
        f"  Grade        : {grade}\n"
        f"  Final Status : {status}\n"
        f"{line}"
    )


def main():
    """Collect input, process it and print the result card."""
    print("=== Student Result Card Generator ===\n")
    name = get_valid_name()
    roll = get_valid_roll_number()

    marks_list = []                       # marks of the five subjects
    for subject in SUBJECTS:
        marks_list.append(get_valid_marks(subject))

    total = sum(marks_list)
    max_total = MAX_PER_SUBJECT * len(SUBJECTS)
    percentage = calculate_percentage(total, max_total)
    grade = get_grade(percentage)
    status = get_final_status(marks_list, grade)

    print(build_result_card(name, roll, marks_list, total, max_total,
                            percentage, grade, status))
    if status == "Fail" and grade != "Fail":
        print("Note: Failed because at least one subject is below 40.")


if __name__ == "__main__":
    main()
