<div align="center">

# Python Functions, Strings & Lists Assessment

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Type](https://img.shields.io/badge/Type-Console%20App-success?style=for-the-badge&logo=gnubash&logoColor=white)
![Tasks](https://img.shields.io/badge/Tasks-2-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

**Two console programs that practise functions, strings and lists in Python.**

[Overview](#-overview) · [Programs](#-description-of-the-programs) · [Concepts](#-python-concepts-used) · [Run](#️-how-to-run) · [Samples](#-sample-input-and-output)

</div>

---

## 📋 Overview
| # | Program | Topic |
|---|---------|-------|
| 1 | **Student Result Card Generator** | Functions + Strings |
| 2 | **Class Marks Analyzer** | Lists |

## 📁 Project Structure
```text
python-functions-lists-assessment/
├── result_card_generator.py
├── class_marks_analyzer.py
└── README.md
```

## 📝 Description of the Programs

### `result_card_generator.py`
- Asks for student name, roll number and marks in 5 subjects (English, Maths, Science, Urdu, Computer).
- Name is cleaned with `.strip()` and `.title()` (extra spaces removed too).
- Roll number must pass `.isdigit()`; marks must be whole numbers from 0 to 100. Wrong input is re-asked.
- Grades: **90+ A+ · 80-89 A · 70-79 B · 60-69 C · 50-59 D · below 50 Fail**
- If any subject is below 40, the result is **Fail** whatever the percentage.
- Prints a neat card with f-strings: name, roll number, subjects, total, percentage (2 decimals), grade, Pass/Fail.

**Functions:** `format_name`, `get_valid_name`, `get_valid_roll_number`, `get_valid_marks`, `calculate_percentage`, `get_grade`, `get_result`, `print_result_card`, `main`

### `class_marks_analyzer.py`
- Asks how many students are in the class, then each name and mark (stored in two lists with `append()`).
- Re-asks on invalid marks (must be 0-100).
- Shows class average, highest and lowest marks (with names, ties included).
- Counts passed (50+) and failed students.
- Lists students above the class average.
- Prints marks sorted from highest to lowest.

**Functions:** `get_valid_number`, `get_valid_name`, `collect_class_data`, `find_who_scored`, `count_pass_fail`, `students_above_average`, `print_sorted_marks`, `main`

## 💡 Python Concepts Used
| Area | Concepts |
|------|----------|
| Functions | `def`, parameters, `return`, docstring comments |
| Strings | `.strip()`, `.title()`, `.split()`, `.join()`, `.isdigit()`, `.isalpha()`, f-strings, format specs (`:.2f`, `:<15`, `:^36`) |
| Lists | create, `append()`, loop, `len()`, `sum()`, `max()`, `min()`, `sorted()`, `zip()` |
| Control flow | `while` validation loops, `for`, `if / elif / else` |
| Error handling | `try / except ValueError` |

## ▶️ How to Run
> Requires **Python 3.8+**

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/python-functions-lists-assessment.git
cd python-functions-lists-assessment

# 2. Run program 1
python result_card_generator.py

# 3. Run program 2
python class_marks_analyzer.py
```
(Use `python3` on Linux / macOS.)

## 🖥️ Sample Input and Output

<details open>
<summary><b>Result Card Generator</b> (click to collapse)</summary>

```text
Enter student name:    ali   raza
Enter roll number: 12x
  Invalid roll number. Digits only, please.
Enter roll number: 1042
Enter marks for English (0-100): 88
Enter marks for Maths (0-100): abc
  Please enter a whole number.
Enter marks for Maths (0-100): 92
Enter marks for Science (0-100): 75
Enter marks for Urdu (0-100): 101
  Marks must be between 0 and 100.
Enter marks for Urdu (0-100): 67
Enter marks for Computer (0-100): 81

====================================
        STUDENT RESULT CARD
====================================
Name        : Ali Raza
Roll Number : 1042
------------------------------------
English           88 / 100
Maths             92 / 100
Science           75 / 100
Urdu              67 / 100
Computer          81 / 100
------------------------------------
Total            403 / 500
Percentage  : 80.60%
Grade       : A
Result      : Pass
====================================
```
Another test: marks 95, 90, **39**, 98, 97 give 83.80% (grade A) but the result is **Fail** because one subject is below 40.

</details>

<details open>
<summary><b>Class Marks Analyzer</b> (click to collapse)</summary>

```text
How many students are in the class? 0
  Value must be between 1 and 200.
How many students are in the class? 4
Name of student 1: ahmed
  Marks for Ahmed (0-100): 72
Name of student 2: bilal
  Marks for Bilal (0-100): -5
  Value must be between 0 and 100.
  Marks for Bilal (0-100): abc
  Please enter a whole number.
  Marks for Bilal (0-100): 45
Name of student 3: fatima
  Marks for Fatima (0-100): 91
Name of student 4: zain
  Marks for Zain (0-100): 45

=========== CLASS REPORT ===========
Students       : 4
Class average  : 63.25
Highest marks  : 91 (Fatima)
Lowest marks   : 45 (Bilal, Zain)
Passed (>= 50) : 2
Failed (< 50)  : 2

Students above class average:
  - Ahmed (72)
  - Fatima (91)

Marks sorted (highest to lowest):
  1. Fatima           91
  2. Ahmed            72
  3. Zain             45
  4. Bilal            45
```

</details>