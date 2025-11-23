# **************************************************
# Coder: Raman Raj Shrivastava
# Roll no.:- 2501010021
# Title: Gradebook Analyzer Assignmnet
#SOET B.TECH CSE CORE Section "B"
# **************************************************

import csv
import statistics


# Task 3: Statistical Functions


def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict) if marks_dict else 0

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values()) if marks_dict else 0

def find_max_score(marks_dict):
    if not marks_dict:
        return None, 0
    name = max(marks_dict, key=marks_dict.get)
    return name, marks_dict[name]

def find_min_score(marks_dict):
    if not marks_dict:
        return None, 0
    name = min(marks_dict, key=marks_dict.get)
    return name, marks_dict[name]



# Task 4: Grade Assignment


def assign_grades(marks_dict):
    grades = {}
    for name, score in marks_dict.items():
        if score >= 90:
            grades[name] = "A"
        elif score >= 80:
            grades[name] = "B"
        elif score >= 70:
            grades[name] = "C"
        elif score >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades



# Task 1 + Task 6: Main Program Loop


def display_menu():
    print("\n=== Gradebook Analyzer ===")
    print("1. Manual Entry")
    print("2. Load from CSV")
    print("3. Exit")
    print("--------------------------")


def print_table(marks, grades):
    print("\n-------------------- RESULTS --------------------")
    print(f"{'Name':<15}{'Marks':<10}{'Grade'}")
    print("-------------------------------------------------")
    for name in marks:
        print(f"{name:<15}{marks[name]:<10}{grades[name]}")
    print("-------------------------------------------------")



# Task 2: Manual Input with Error Handling


def manual_entry():
    marks = {}

    # number of students validation
    while True:
        try:
            n = int(input("How many students? "))
            if n <= 0:
                print("Enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid number! Please enter an integer.")

    for _ in range(n):
        name = input("Enter student name: ").strip()
        while not name:
            print("Name cannot be blank!")
            name = input("Enter student name: ").strip()

        # marks validation
        while True:
            try:
                score = int(input(f"Enter marks for {name}: "))
                if score < 0 or score > 100:
                    print("Marks must be between 0 and 100.")
                    continue
                break
            except ValueError:
                print("Invalid input! Marks must be an integer.")

        marks[name] = score

    return marks



# Task 2: CSV Input with Robust Handling


def load_from_csv():
    marks = {}
    file = input("Enter CSV file name (with .csv): ").strip()

    try:
        with open(file, "r") as f:
            reader = csv.reader(f)

            header = next(reader, None)  # skip header
            if header is None:
                print("Empty file or no header found!")
                return {}

            for row in reader:
                # skip empty lines
                if not row or len(row) < 2:
                    continue

                # trim spaces
                row = [col.strip() for col in row]

                name = row[0]
                if not name:
                    print("Skipping row: missing name")
                    continue

                try:
                    score = int(row[1])
                    if score < 0 or score > 100:
                        print(f"Skipping invalid marks for {name}: {row[1]}")
                        continue
                except ValueError:
                    print(f"Skipping invalid marks for {name}: {row[1]}")
                    continue

                marks[name] = score

    except FileNotFoundError:
        print("File not found! Please check the filename.")
    except Exception as e:
        print("Error reading file:", e)

    return marks



# Task 5: Pass/Fail using list comprehension


def pass_fail_lists(marks):
    passed = [name for name, score in marks.items() if score >= 40]
    failed = [name for name, score in marks.items() if score < 40]
    return passed, failed



# Main Execution Loop


def main():
    print("\nWelcome to Gradebook Analyzer!")
    print("This program analyzes student marks.\n")

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            marks = manual_entry()

        elif choice == "2":
            marks = load_from_csv()

        elif choice == "3":
            print("Exiting program. Thank you!")
            break

        else:
            print("Invalid option! Try again.")
            continue

        if not marks:
            print("No valid data found! Please try again.")
            continue

        # Task 3: Statistical Analysis
        avg = calculate_average(marks)
        median = calculate_median(marks)
        max_name, max_score = find_max_score(marks)
        min_name, min_score = find_min_score(marks)

        # Task 4: Grades
        grades = assign_grades(marks)

        # Grade Distribution
        distribution = {g: list(grades.values()).count(g) for g in "ABCDF"}

        # Task 5: Pass/Fail
        passed, failed = pass_fail_lists(marks)

        # Task 6: Results Table
        print_table(marks, grades)

        # Summary
        print("\n----- Analysis Summary -----")
        print(f"Average Score: {avg:.2f}")
        print(f"Median Score: {median}")
        print(f"Highest Score: {max_name} ({max_score})")
        print(f"Lowest Score: {min_name} ({min_score})")

        print("\nGrade Distribution:")
        for g, cnt in distribution.items():
            print(f"{g}: {cnt}")

        print("\nPassed Students:", passed)
        print("Failed Students:", failed)
        print("-------------------------------------------")


if __name__ == "__main__":
    main()
