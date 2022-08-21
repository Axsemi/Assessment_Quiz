#assessment for iterative processes

#------------------------------------------------------------------

#the actual quiz function

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

#------------------------------------------------------------------

#to check if the users guesses were correct

def answer_checker(answer, guess):

        if answer == guess:
            print("CORRECT")
            return 1
        else:
            print("INCORRECT")
            return 0

#------------------------------------------------------------------

#to display users results

def display_results(correct_guesses, guesses):

    print("-------------------------")
    print("RESULTS FROM YOUR QUIZ :)")
    print("-------------------------")
    print("Answers: ", end="")

    score = (correct_guesses)
    print("You scored "+str(score)+"/6")

#------------------------------------------------------------------

#to ask users if they would like to play again

def play_again():

    response = input("Do you want to try again? " )
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

#------------------------------------------------------------------

#dictionary for all of my questions

questions = {
    "What is the equator?" : "A",
    "What is the prime meridian?" : "C",
    "What are the vertical lines on a map called?" : "A",
    "What are the horizontal lines on a map called?" : "B",
    "When did H.K make landfall?" : "B",
    "Where did H.K make landfall?" : "B",
    }

#------------------------------------------------------------------

#options for the questions

options = [
    ["A. An imaginary line around the earth (horizontal)","B. An imaginary line across the earth (vertical)","C. I do not know"],
    ["A. I do not know", "B. An imaginary line around the earth (horizontal)","C. An imaginary line across the earth (vertical)"],
    ["A. Eastings","B. Westings","C. Northings"],
    ["A. Southings","B. Northings","C. Eastings"],
    ["A. 5:40 am","B. 6:10 am","C. 7:30 am"],
    ["A. California","B. New Orleans","C. New Zealand"]
    ]

#------------------------------------------------------------------

#instructions component - to tell people what to do etc.

def instructions_component():

    intruction_question = input("Before taking part in this quiz, do you want some instruction?: ")
    intruction_question = intruction_question.upper()

    if intruction_question == "YES":
        print("-------------------------")
        print("A question will pop up on the screen and you have 3 choices (a, b or c) to choose from")
        print("you then must decipher which answer is the correct one.")
        print("Good luck!")
        print("-------------------------")
        quiz_component()
    elif intruction_question == "NO":
        quiz_component()
    else:
        print("Please enter (yes) or (no)")
        instructions_component()

#------------------------------------------------------------------

#main program

instructions_component()

while play_again():
    quiz_component()

print("-------------------------")
print("I hope you had fun!")
print("-------------------------")

#------------------------------------------------------------------
