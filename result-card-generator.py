"""Task 1: Student Result Card Generator (functions + strings)."""

SUBJECTS = ["English", "Maths", "Science", "Urdu", "Computer"]
MAX_PER_SUBJECT = 100
SUBJECT_PASS_MARK = 40


def format_name(name):
    """Clean a name: remove extra spaces and capitalise each word."""
    return " ".join(name.strip().split()).title()


def get_valid_name():
    """Keep asking until the name contains only letters and spaces."""
    while True:
        name = format_name(input("Enter student name: "))
        if name != "" and name.replace(" ", "").isalpha():
            return name
        print("  Invalid name. Use letters and spaces only.")


def get_valid_roll_number():
    """Keep asking until the roll number is made of digits only."""
    while True:
        roll = input("Enter roll number: ").strip()
        if roll.isdigit():
            return roll
        print("  Invalid roll number. Digits only, please.")


def get_valid_marks(subject):
    """Ask for marks in one subject and re-ask until they are 0-100."""
    while True:
        text = input(f"Enter marks for {subject} (0-100): ").strip()
        try:
            marks = int(text)
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if 0 <= marks <= MAX_PER_SUBJECT:
            return marks
        print("  Marks must be between 0 and 100.")


def calculate_percentage(total, max_total):
    """Return the percentage of total out of max_total."""
    return total / max_total * 100


def get_grade(percentage):
    """Return the grade letter for a given percentage."""
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


def get_result(marks_list, grade):
    """Return Pass/Fail: Fail if any subject is below 40 or grade is Fail."""
    if min(marks_list) < SUBJECT_PASS_MARK or grade == "Fail":
        return "Fail"
    return "Pass"


def print_result_card(name, roll, marks_list, total, max_total, percentage, grade, result):
    """Print the final result card using f-strings."""
    line = "=" * 36
    print("\n" + line)
    print(f"{'STUDENT RESULT CARD':^36}")
    print(line)
    print(f"Name        : {name}")
    print(f"Roll Number : {roll}")
    print("-" * 36)
    for subject, marks in zip(SUBJECTS, marks_list):
        print(f"{subject:<15}{marks:>5} / {MAX_PER_SUBJECT}")
    print("-" * 36)
    print(f"{'Total':<15}{total:>5} / {max_total}")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Grade       : {grade}")
    print(f"Result      : {result}")
    print(line)


def main():
    """Run the program: collect input, calculate, print the card."""
    print("--- Student Result Card Generator ---")
    name = get_valid_name()
    roll = get_valid_roll_number()

    marks_list = []
    for subject in SUBJECTS:
        marks_list.append(get_valid_marks(subject))

    total = sum(marks_list)
    max_total = MAX_PER_SUBJECT * len(SUBJECTS)
    percentage = calculate_percentage(total, max_total)
    grade = get_grade(percentage)
    result = get_result(marks_list, grade)

    print_result_card(name, roll, marks_list, total, max_total, percentage, grade, result)


if __name__ == "__main__":
    main()
