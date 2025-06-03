def ask_question(i: int, question: str, answers: list[str]) -> bool:
    print(f"Question {i+1}:")
    print(question)

    answer: str = input("Answer: ")

    if answer.lower() in answers:
        return True
    return False

def main() -> None:
    print("Hello!, This quiz will test your beginner knowledge in python.")
    print("REMINDER: Any information you input into this program will not be saved, stored or transmitted anywhere!")

    name = input("Please input your name: ")
    print(f"Hello {name}! We'll begin now.\n")

    correct_answers: int = 0
    incorrect_answers: int = 0

    questions: list[tuple[str, list[str], str, str]] = [
        ("What function do you use to print a string?", ["print", "print()"], "Yes, that is correct.", "Sorry, that's incorrect. The answer is print."),
        ("What function do you use to get user input?", ["input", "input()"], "Yes, that is correct.", "Sorry, that's incorrect. The answer is input."),
        ("What function is used to format a string?", ["format", ".format", "format()", ".format()"], "Yes, that is correct.", "Sorry, that's incorrect. The answer is format.")
    ]

    for i in range(len(questions)):
        question = questions[i]
        if ask_question(i, question[0], question[1]):
            print(question[2])
            correct_answers += 1
        else:
            print(question[3])
            incorrect_answers += 1

    print(f"Alright {name}, we've finished the questions.")
    print(f"You got {correct_answers} correct and {incorrect_answers} incorrect.")
    print(f"Your score is {float(correct_answers) / float(len(questions)) * 100}%.")

if __name__ == "__main__":
    main()