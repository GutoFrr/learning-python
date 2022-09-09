quiz = {
    "question1": {
        "statement": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "statement": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "statement": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "statement": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5": {
        "statement": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question6": {
        "statement": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question7": {
        "statement": "What is the capital of England?",
        "answer": "London"
    },
}

score = 0

for key, value in quiz.items():
    print(value['statement'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct!')
        score = score + 1
        print("Your score is: " + str(score) + "\n")

    else:
        print("Wrong!")
        print("The answer is: " + value['answer'])
        print("Your score is: " + str(score) + "\n")

print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is " + str(int(score / 7 * 100)) + "%")
