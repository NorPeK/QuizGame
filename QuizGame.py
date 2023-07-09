def newGame():
    guesses = []
    correctGuesses = 0
    questionNumber = 1
    for key in questions:
        print("--------------------")
        print(key)
        for i in options[questionNumber-1]:
            print(i)
        guess =  input("Enter (A,B,C, or D):")
        guess = guess.upper()
        guesses.append(guess)
        correctGuesses += checkAnswer(questions.get(key), guess) #this will pick up the answer along with its guess ; .get(key) is A,B,C,D
        questionNumber += 1
    displayScore(correctGuesses, guesses)
    playAgain()


def checkAnswer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
    

def displayScore(correct_guesses, guesses):
    print("--------------------")
    print("RESULTS")
    print("--------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print("")
    print("Answers: ", end="")
    for i in guesses:
        print(i, end=" ")
    print("")
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+" out of 100!")

def playAgain():
    response = input("Do you want to play again? (yes/no): ")
    response = response.upper()
    if response == "YES":
        newGame()
    #if response == "YES":
    #    return True
    #else:
    #    return False

#main program
questions = {
    "Who created python? " : "A",
    "What year was python created?" : "B",
    "Python is tributed to which comedy group?" : "C",
    "Is the Earth round?" : "A"
}
options = [["A. Duido van Rossum" , "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989" , "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island" , "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. Yes" , "B. No", "C. Sometimes", "D. huh?"]]

newGame()
#while playAgain():
#    newGame()
print("Thanks for playing!")


