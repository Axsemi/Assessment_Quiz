def instructions_component():
    intruction_question = input("Before taking part in this quiz, do you want some instruction?: ")
    if intruction_question == "yes" or intruction_question == "YES" or intruction_question == "Y":
        print("INSTRUCTIONS")
        while True:
            send_from_instructions = input("Enter 'yes' when you are ready to take the quiz: ")
            if send_from_instructions == "yes" or send_from_instructions == "YES" or send_from_instructions == "Y":
                print("SEND USER TO QUIZ")
            else:
                print("Please enter yes")

    elif intruction_question == "no" or intruction_question == "NO" or intruction_question == "N":
        print("SEND USER TO QUIZ COMPONENT")
    else:
        print("Please enter yes or no.")
instructions_component()
