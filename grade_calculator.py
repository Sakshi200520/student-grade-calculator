# Student Grade Calculator 

from typing import Tuple


# Constants
GRADE_RULES = [
    (90, "A", "Excellent work! Keep shining! 🌟"),
    (80, "B", "Very Good! Keep it up! 👍"),
    (70, "C", "Good effort! You can do even better! 💪"),
    (60, "D", "Don't give up! Keep practicing! 📘"),
    (0,  "F", "Keep trying! You will improve! 🔥")
]


def calculate_grade(marks: float) -> Tuple[str, str]:
    """
    Determines grade and message based on marks.
    """
    for min_marks, grade, message in GRADE_RULES:
        if marks >= min_marks:
            return grade, message


def get_valid_marks() -> float:
    """
    Prompts user until valid marks (0-100) are entered.
    """
    while True:
        user_input = input("Enter marks (0-100): ")

        try:
            marks = float(user_input)

            if 0 <= marks <= 100:
                return marks

            print("❌ Marks must be between 0 and 100.")

        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")


def get_student_name() -> str:
    """
    Gets and validates student name.
    """
    while True:
        name = input("Enter student name: ").strip()

        if name:
            return name

        print("❌ Name cannot be empty.")


def display_result(name: str, marks: float, grade: str, message: str) -> None:
    """
    Displays formatted result.
    """
    print("\n" + "=" * 40)
    print(f"📊 RESULT FOR {name.upper()}")
    print("=" * 40)
    print(f"Marks : {marks}/100")
    print(f"Grade : {grade}")
    print(f"Message: {message}")
    print("=" * 40)


def main() -> None:
    """
    Main program execution.
    """
    print("📊 STUDENT GRADE CALCULATOR 📊\n")

    name = get_student_name()
    marks = get_valid_marks()

    grade, message = calculate_grade(marks)
    display_result(name, marks, grade, message)


# Entry point (best practice)
if __name__ == "__main__":
    main()