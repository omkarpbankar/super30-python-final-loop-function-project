"""
Task 04: Python Quiz Application
Objective:
    Interactive Python knowledge quiz system.
    - Displays one question at a time.
    - Accepts and validates user answers.
    - Checks correctness and provides immediate feedback.
    - Maintains the score.
    - Displays detailed final score, percentage, and rating.
"""

from typing import List, Dict, Any


def get_quiz_questions() -> List[Dict[str, Any]]:
    """
    Returns a curated list of at least 6 Python conceptual questions with options and explanations.

    Returns:
        List[Dict[str, Any]]: List of question dictionaries.
    """
    return [
        {
            "id": 1,
            "question": "Which keyword is used to define a function in Python?",
            "options": {
                "A": "func",
                "B": "def",
                "C": "function",
                "D": "lambda"
            },
            "correct": "B",
            "explanation": "'def' is the keyword used to define standard functions in Python."
        },
        {
            "id": 2,
            "question": "What is the output of `len([1, 2, 3, [4, 5]])` in Python?",
            "options": {
                "A": "5",
                "B": "4",
                "C": "3",
                "D": "TypeError"
            },
            "correct": "B",
            "explanation": "The outer list contains 4 elements: 1, 2, 3, and the nested list [4, 5]."
        },
        {
            "id": 3,
            "question": "Which loop is generally best suited when the exact number of iterations is known beforehand?",
            "options": {
                "A": "while loop",
                "B": "for loop",
                "C": "do-while loop",
                "D": "infinite loop"
            },
            "correct": "B",
            "explanation": "'for' loops in Python are designed for iterating over known sequences or ranges."
        },
        {
            "id": 4,
            "question": "Which of the following statements immediately terminates a loop in Python?",
            "options": {
                "A": "continue",
                "B": "pass",
                "C": "break",
                "D": "return"
            },
            "correct": "C",
            "explanation": "'break' terminates the innermost executing loop immediately."
        },
        {
            "id": 5,
            "question": "What data type is the result of `type((1,))`?",
            "options": {
                "A": "int",
                "B": "tuple",
                "C": "set",
                "D": "list"
            },
            "correct": "B",
            "explanation": "A single element followed by a comma enclosed in parentheses defines a tuple."
        },
        {
            "id": 6,
            "question": "Which built-in function returns an immutable sequence of numbers from start to stop by step?",
            "options": {
                "A": "sequence()",
                "B": "range()",
                "C": "enumerate()",
                "D": "xrange()"
            },
            "correct": "B",
            "explanation": "'range()' generates an immutable arithmetic progression in Python 3."
        }
    ]


def display_question(q_data: Dict[str, Any], q_index: int, total_questions: int) -> None:
    """
    Displays a single quiz question and its formatted options.

    Args:
        q_data (Dict[str, Any]): Question dictionary.
        q_index (int): 1-based question number.
        total_questions (int): Total number of questions.
    """
    print("\n" + "=" * 65)
    print(f"QUESTION {q_index} OF {total_questions}")
    print("=" * 65)
    print(f"{q_data['question']}\n")
    for opt_key, opt_text in q_data["options"].items():
        print(f"  [{opt_key}] {opt_text}")
    print("-" * 65)


def accept_user_answer() -> str:
    """
    Prompts user for answer and validates that choice is one of A, B, C, or D.

    Returns:
        str: Validated uppercase answer choice.
    """
    valid_choices = {"A", "B", "C", "D"}
    while True:
        choice = input("Your answer (A, B, C, or D): ").strip().upper()
        if choice in valid_choices:
            return choice
        print("  [!] Invalid input. Please enter A, B, C, or D.")


def check_answer(user_ans: str, q_data: Dict[str, Any]) -> bool:
    """
    Checks user answer against correct answer and displays immediate feedback.

    Args:
        user_ans (str): User choice ('A', 'B', 'C', 'D').
        q_data (Dict[str, Any]): Question dictionary.

    Returns:
        bool: True if answer is correct, False otherwise.
    """
    correct_ans = q_data["correct"]
    if user_ans == correct_ans:
        print(f"  [+] CORRECT! Great job.")
        print(f"      Explanation: {q_data['explanation']}")
        return True
    else:
        correct_text = q_data["options"][correct_ans]
        print(f"  [-] INCORRECT! The correct answer was [{correct_ans}]: {correct_text}")
        print(f"      Explanation: {q_data['explanation']}")
        return False


def calculate_percentage(score: int, total: int) -> float:
    """
    Calculates percentage score.

    Args:
        score (int): Number of correct answers.
        total (int): Total questions.

    Returns:
        float: Percentage rounded to 2 decimal places.
    """
    if total <= 0:
        return 0.0
    return round((score / total) * 100.0, 2)


def display_final_results(score: int, total: int, user_summary: List[Dict[str, Any]]) -> None:
    """
    Displays comprehensive final scorecard and performance analysis.

    Args:
        score (int): Number of correct answers.
        total (int): Total questions.
        user_summary (List[Dict[str, Any]]): Log of user answers.
    """
    pct = calculate_percentage(score, total)

    if pct >= 90:
        badge = "Python Master (Outstanding)"
    elif pct >= 70:
        badge = "Proficient Pythonista (Good Job)"
    elif pct >= 50:
        badge = "Apprentice (Needs Revision)"
    else:
        badge = "Novice (Keep Practicing)"

    print("\n" + "#" * 65)
    print(f"{'QUIZ SUMMARY & PERFORMANCE REPORT':^65}")
    print("#" * 65)
    print(f"Total Questions  : {total}")
    print(f"Correct Answers  : {score}")
    print(f"Incorrect Answers: {total - score}")
    print(f"Final Score      : {score}/{total}")
    print(f"Percentage       : {pct:.2f}%")
    print(f"Achievement Rank : {badge}")
    print("-" * 65)
    print("Detailed Review:")
    for idx, item in enumerate(user_summary, start=1):
        status = "[CORRECT]" if item["is_correct"] else "[WRONG]  "
        print(f"  Q{idx}: {status} | Your Answer: {item['user_ans']} | Correct: {item['correct_ans']}")
    print("#" * 65 + "\n")


def run_quiz(questions: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Executes the entire quiz application flow.

    Args:
        questions (List[Dict[str, Any]], optional): Question set. Defaults to standard questions.

    Returns:
        Dict[str, Any]: Final quiz performance dictionary.
    """
    if questions is None:
        questions = get_quiz_questions()

    score = 0
    total = len(questions)
    user_summary: List[Dict[str, Any]] = []

    print("\nWelcome to the Super30 Python Quiz Application!")
    print(f"You will be asked {total} questions. Let's test your Python skills!\n")

    # Loop through each question sequentially
    for index, q_data in enumerate(questions, start=1):
        display_question(q_data, index, total)
        ans = accept_user_answer()
        is_corr = check_answer(ans, q_data)
        if is_corr:
            score += 1
        user_summary.append({
            "question_id": q_data["id"],
            "user_ans": ans,
            "correct_ans": q_data["correct"],
            "is_correct": is_corr
        })

    display_final_results(score, total, user_summary)
    return {
        "score": score,
        "total": total,
        "percentage": calculate_percentage(score, total),
        "summary": user_summary
    }


def main():
    """Interactive quiz starter with replay loop."""
    while True:
        run_quiz()
        replay = input("Would you like to retry the quiz? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thanks for playing! Happy Coding!")
            break


if __name__ == "__main__":
    main()
