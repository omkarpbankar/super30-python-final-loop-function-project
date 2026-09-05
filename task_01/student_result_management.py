"""
Task 01: Student Result Management System
Objective:
    Accept student marks, calculate total, calculate percentage, assign grade,
    determine pass/fail status, and display a formatted result report.
    Uses loops for data collection, validation, and table rendering.
"""

from typing import Dict, List, Tuple, Union


def accept_student_marks(subjects: List[str] = None) -> Dict[str, float]:
    """
    Interactively accepts marks for given subjects with input validation.

    Args:
        subjects (List[str], optional): List of subject names. Defaults to standard 5 subjects.

    Returns:
        Dict[str, float]: Mapping of subject name to marks obtained (0-100).
    """
    if subjects is None:
        subjects = ["Mathematics", "Physics", "Chemistry", "English", "Computer Science"]

    marks: Dict[str, float] = {}
    print(f"\nEnter marks for {len(subjects)} subjects (Max: 100 per subject):")

    for subject in subjects:
        while True:
            try:
                user_input = input(f"  Enter marks for {subject}: ").strip()
                score = float(user_input)
                if 0.0 <= score <= 100.0:
                    marks[subject] = score
                    break
                else:
                    print("    [!] Error: Marks must be between 0 and 100.")
            except ValueError:
                print("    [!] Error: Please enter a valid numeric value.")
    return marks


def calculate_total(marks: Union[Dict[str, float], List[float]]) -> float:
    """
    Calculates the total marks from a dictionary or list of scores using a loop.

    Args:
        marks (Union[Dict[str, float], List[float]]): Subject scores.

    Returns:
        float: Sum of all marks.
    """
    total = 0.0
    scores = marks.values() if isinstance(marks, dict) else marks
    for score in scores:
        total += score
    return round(total, 2)


def calculate_percentage(total_marks: float, max_marks: float) -> float:
    """
    Calculates percentage based on total marks obtained and maximum possible marks.

    Args:
        total_marks (float): Total marks scored.
        max_marks (float): Maximum possible marks.

    Returns:
        float: Percentage rounded to 2 decimal places.
    """
    if max_marks <= 0:
        return 0.0
    return round((total_marks / max_marks) * 100.0, 2)


def assign_grade(percentage: float) -> str:
    """
    Assigns a letter grade based on percentage score.

    Scale:
        90 - 100 : A+
        80 - 89.99 : A
        70 - 79.99 : B
        60 - 69.99 : C
        50 - 59.99 : D
        < 50 : F (Fail)

    Args:
        percentage (float): Student percentage.

    Returns:
        str: Assigned letter grade.
    """
    if percentage >= 90.0:
        return "A+"
    elif percentage >= 80.0:
        return "A"
    elif percentage >= 70.0:
        return "B"
    elif percentage >= 60.0:
        return "C"
    elif percentage >= 50.0:
        return "D"
    else:
        return "F"


def determine_pass_fail(marks: Union[Dict[str, float], List[float]], passing_mark: float = 40.0) -> Tuple[bool, List[str]]:
    """
    Determines if the student passed all individual subjects.

    Args:
        marks (Union[Dict[str, float], List[float]]): Marks obtained.
        passing_mark (float): Minimum marks required to pass each subject. Defaults to 40.0.

    Returns:
        Tuple[bool, List[str]]: (Overall pass status, List of failed subjects).
    """
    failed_subjects: List[str] = []
    if isinstance(marks, dict):
        for subject, score in marks.items():
            if score < passing_mark:
                failed_subjects.append(subject)
    else:
        for idx, score in enumerate(marks, start=1):
            if score < passing_mark:
                failed_subjects.append(f"Subject {idx}")

    is_passed = len(failed_subjects) == 0
    return is_passed, failed_subjects


def display_result(
    student_name: str,
    marks: Dict[str, float],
    total: float,
    max_marks: float,
    percentage: float,
    grade: str,
    is_passed: bool,
    failed_subjects: List[str]
) -> None:
    """
    Displays a formatted student report card.

    Args:
        student_name (str): Name of the student.
        marks (Dict[str, float]): Individual subject marks.
        total (float): Total marks.
        max_marks (float): Maximum possible marks.
        percentage (float): Percentage.
        grade (str): Letter grade.
        is_passed (bool): Pass/Fail indicator.
        failed_subjects (List[str]): List of failed subjects if any.
    """
    status_str = "PASSED" if is_passed else "FAILED"
    print("\n" + "=" * 55)
    print(f"{'STUDENT RESULT REPORT CARD':^55}")
    print("=" * 55)
    print(f"Student Name : {student_name}")
    print("-" * 55)
    print(f"{'Subject':<30} | {'Marks (Out of 100)':<20}")
    print("-" * 55)
    for subject, score in marks.items():
        status_flag = "PASS" if score >= 40.0 else "FAIL"
        print(f"{subject:<30} | {score:>6.2f}  ({status_flag})")
    print("-" * 55)
    print(f"Total Marks Scored : {total:.2f} / {max_marks:.2f}")
    print(f"Percentage         : {percentage:.2f}%")
    print(f"Assigned Grade     : {grade}")
    print(f"Final Status       : {status_str}")
    if not is_passed:
        print(f"Failed in Subjects : {', '.join(failed_subjects)}")
    print("=" * 55 + "\n")


def process_student_result(student_name: str, marks: Dict[str, float], passing_mark: float = 40.0) -> Dict[str, Union[str, float, bool, List[str]]]:
    """
    Processes all components of student results in a single callable pipeline.

    Returns:
        dict: Complete result dictionary.
    """
    total = calculate_total(marks)
    max_marks = len(marks) * 100.0
    percentage = calculate_percentage(total, max_marks)
    grade = assign_grade(percentage)
    is_passed, failed_subjects = determine_pass_fail(marks, passing_mark)

    return {
        "student_name": student_name,
        "marks": marks,
        "total": total,
        "max_marks": max_marks,
        "percentage": percentage,
        "grade": grade,
        "is_passed": is_passed,
        "failed_subjects": failed_subjects
    }


def main():
    """Interactive CLI runner for Student Result Management."""
    print("=== Super30 Student Result Management System ===")
    while True:
        name = input("\nEnter student name (or type 'exit' to quit): ").strip()
        if not name:
            print("Student name cannot be empty.")
            continue
        if name.lower() == 'exit':
            print("Exiting Student Result Management System. Goodbye!")
            break

        marks = accept_student_marks()
        result = process_student_result(name, marks)
        display_result(
            student_name=result["student_name"],
            marks=result["marks"],
            total=result["total"],
            max_marks=result["max_marks"],
            percentage=result["percentage"],
            grade=result["grade"],
            is_passed=result["is_passed"],
            failed_subjects=result["failed_subjects"]
        )

        again = input("Do you want to evaluate another student? (y/n): ").strip().lower()
        if again != 'y':
            print("Session ended.")
            break


if __name__ == "__main__":
    main()
