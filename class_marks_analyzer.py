"""
Task 2 - Class Marks Analyzer
Topics: lists (create, append, len, sum, max, min, sorted) and loops.

Collects names and marks for a whole class, then reports statistics.
"""

PASS_MARK = 50   # 50 or above passes, below 50 fails


def get_valid_student_count():
    """Ask for the class size until a whole number of 1 or more is entered."""
    while True:
        raw = input("How many students are in the class? ").strip()
        if raw.isdigit() and int(raw) >= 1:
            return int(raw)
        print("  Invalid input. Enter a whole number of 1 or more.")


def get_valid_mark(prompt):
    """Ask repeatedly until a number between 0 and 100 is entered."""
    while True:
        raw = input(prompt).strip()
        try:
            mark = float(raw)
        except ValueError:
            print("  Invalid input. Please enter a number.")
            continue
        if 0 <= mark <= 100:   # also rejects 'nan'
            return mark
        print("  Marks must be between 0 and 100.")


def get_valid_student_name(position):
    """Ask for a non-empty student name (cleaned with strip and title)."""
    while True:
        name = input(f"Student {position} name: ").strip().title()
        if name:
            return name
        print("  Name cannot be empty.")


def find_students_with_mark(student_names, student_marks, target):
    """Return the names of every student whose mark equals target."""
    matches = []
    for index in range(len(student_marks)):
        if student_marks[index] == target:
            matches.append(student_names[index])
    return matches


def print_section(title):
    """Print a section heading."""
    print(f"\n--- {title} ---")


def main():
    """Collect class data and display every required statistic."""
    print("=== Class Marks Analyzer ===\n")
    student_names = []
    student_marks = []

    count = get_valid_student_count()
    for number in range(1, count + 1):
        student_names.append(get_valid_student_name(number))
        student_marks.append(get_valid_mark(f"  Marks of {student_names[-1]} (0-100): "))

    # Class average
    average = sum(student_marks) / len(student_marks)
    print_section("Class Summary")
    print(f"Total students : {len(student_marks)}")
    print(f"Class average  : {average:.2f}")

    # Highest and lowest (ties are all listed)
    highest, lowest = max(student_marks), min(student_marks)
    top = find_students_with_mark(student_names, student_marks, highest)
    bottom = find_students_with_mark(student_names, student_marks, lowest)
    print(f"Highest marks  : {highest:g} -> {', '.join(top)}")
    print(f"Lowest marks   : {lowest:g} -> {', '.join(bottom)}")

    # Pass / fail count
    passed = 0
    for mark in student_marks:
        if mark >= PASS_MARK:
            passed += 1
    failed = len(student_marks) - passed
    print_section("Pass / Fail")
    print(f"Passing (>= {PASS_MARK}) : {passed}")
    print(f"Failing (<  {PASS_MARK}) : {failed}")

    # Students above the class average
    print_section("Above Class Average")
    above_found = False
    for name, mark in zip(student_names, student_marks):
        if mark > average:
            print(f"  {name:<20}{mark:>6g}")
            above_found = True
    if not above_found:
        print("  No student scored above the class average.")

    # Sorted high to low (highest mark first, then name A-Z for ties)
    ranking = sorted(zip(student_names, student_marks), key=lambda pair: (-pair[1], pair[0]))
    print_section("Marks (Highest to Lowest)")
    for rank, (name, mark) in enumerate(ranking, start=1):
        print(f"  {rank:>2}. {name:<20}{mark:>6g}")
    print("\nSorted marks only:", [f"{m:g}" for m in sorted(student_marks, reverse=True)])


if __name__ == "__main__":
    main()
