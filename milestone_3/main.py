def ask_question(question: str, answers: list[str]) -> bool:
    print(question)

    answer: str = input("Answer: ")

    if answer.lower() in answers:
        return True
    return False

def main() -> None:
    correct_answers: int = 0
    incorrect_answers: int = 0

    questions: list[tuple[str, list[str], str, str]] = [
        ("What function do you use to print a string?", ["print", "print()"], "Yes, that is correct.", "Sorry, that's incorrect. The answer is print."),
        ("What function do you use to get user input?", ["input", "input()"], "Yes, that is correct.", "Sorry, that's incorrect. The answer is input."),
        ("What function is used to format a string?", ["format", ".format", "format()", ".format()"], "Yes, that is correct.", "Sorry, that's incorrect. The answer is format.")
    ]

    for question in questions:
        if ask_question(question[0], question[1]):
            print(question[2])
            correct_answers += 1
        else:
            print(question[3])
            incorrect_answers += 1

    print(f"Correct answers: {correct_answers}.")
    print(f"Incorrect answers: {incorrect_answers}.")
    print(f"Your score is {float(correct_answers) / float(len(questions)) * 100}%.")

if __name__ == "__main__":
    main()