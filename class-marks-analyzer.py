"""Task 2: Class Marks Analyzer (lists)."""

PASS_MARK = 50


def get_valid_number(prompt, low, high):
    """Ask for a whole number between low and high; re-ask on bad input."""
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if low <= value <= high:
            return value
        print(f"  Value must be between {low} and {high}.")


def get_valid_name(position):
    """Ask for a non-empty student name and clean it."""
    while True:
        name = input(f"Name of student {position}: ").strip().title()
        if name != "":
            return name
        print("  Name cannot be empty.")


def collect_class_data(count):
    """Read names and marks into two lists using append()."""
    names = []
    marks = []
    for i in range(1, count + 1):
        names.append(get_valid_name(i))
        marks.append(get_valid_number(f"  Marks for {names[-1]} (0-100): ", 0, 100))
    return names, marks


def find_who_scored(names, marks, target):
    """Return the list of students whose marks equal target (handles ties)."""
    result = []
    for i in range(len(marks)):
        if marks[i] == target:
            result.append(names[i])
    return result


def count_pass_fail(marks):
    """Return (passed, failed) counts using the pass mark of 50."""
    passed = 0
    for m in marks:
        if m >= PASS_MARK:
            passed += 1
    return passed, len(marks) - passed


def students_above_average(names, marks, average):
    """Return a list of (name, mark) for students above the class average."""
    above = []
    for i in range(len(marks)):
        if marks[i] > average:
            above.append((names[i], marks[i]))
    return above


def print_sorted_marks(names, marks):
    """Print marks from highest to lowest along with student names."""
    pairs = sorted(zip(marks, names), reverse=True)
    print("\nMarks sorted (highest to lowest):")
    for position, (mark, name) in enumerate(pairs, start=1):
        print(f"  {position}. {name:<15}{mark:>4}")


def main():
    """Run the program: collect data, then print the full analysis."""
    print("--- Class Marks Analyzer ---")
    count = get_valid_number("How many students are in the class? ", 1, 200)
    names, marks = collect_class_data(count)

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    passed, failed = count_pass_fail(marks)

    print("\n=========== CLASS REPORT ===========")
    print(f"Students       : {len(marks)}")
    print(f"Class average  : {average:.2f}")
    print(f"Highest marks  : {highest} ({', '.join(find_who_scored(names, marks, highest))})")
    print(f"Lowest marks   : {lowest} ({', '.join(find_who_scored(names, marks, lowest))})")
    print(f"Passed (>= {PASS_MARK}) : {passed}")
    print(f"Failed (< {PASS_MARK})  : {failed}")

    above = students_above_average(names, marks, average)
    print("\nStudents above class average:")
    if above:
        for name, mark in above:
            print(f"  - {name} ({mark})")
    else:
        print("  None (everyone scored the same).")

    print_sorted_marks(names, marks)


if __name__ == "__main__":
    main()
