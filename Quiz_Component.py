def quiz_component():
    question_num = 1
    guesses = []
    correct_guesses = 0

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter A, B or C: ")
        guess = guess.upper()
        guesses.append(guess)

        #correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    #display_results()

questions = {
    "Questions" : "A",
    "Question" : "B",
    "Quest" : "C"
    }

options = [
    ["A.blah","B.blah","C.blah"],
    ["A.bleh","B.bleh","C.bleh"],
    ["A.blih","B.blih","C.blih"]
    ]
quiz_component()
