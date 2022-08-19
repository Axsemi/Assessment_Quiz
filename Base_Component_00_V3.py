#assessment for iterative processes
#------------------------------------------------------------------
#the quiz generator function
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
        print("-------------------------")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += answer_checker(questions.get(key), guess)
        question_num += 1
    display_results(correct_guesses, guesses)

def answer_checker(answer, guess):
        if answer == guess:
            print("CORRECT")
            return 1
        else:
            print("INCORRECT")
            return 0
def display_results(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS FROM YOUR QUIZ :)")
    print("-------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()
    print("Your guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("You scored "+str(score)+"%")

    #dictionary for all of my questions
questions = {
    "Questions" : "A",
    "Question" : "B",
    "Quest" : "C"
    }

    #options for the questions
options = [
    ["A.blah","B.blah","C.blah"],
    ["A.bleh","B.bleh","C.bleh"],
    ["A.blih","B.blih","C.blih"]
    ]
quiz_component()
#------------------------------------------------------------------
