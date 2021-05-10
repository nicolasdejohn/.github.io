# Nicolas DeJohn | Chapter 10-9 Lab | April 3 2021

'''The purpose of this program is to ask two players a series of questions and compare their scores at the end of the round.'''

#import collections
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 10")

# Import needed modules
import Question
import GenerateQuestions

# Main function
def main():
    # Initialize an instance of the question object
    questionList = GenerateQuestions.generateQuestion()

    # Initialize the player score constants
    player1 = 0
    player2 = 0

    # Loop 0 through 5 for Player 1's questions
    print("Player 1")
    for i in range(0,5):
        question = questionList[i]
        print(question)
        try:
            res = int(input("\nEnter your choice: "))
            print()
            if res == int(question.getCorrectAnswer()):
                player1 += 1 # Add to player1
        except ValueError:
            print("Invalid answer. No points are awarded.")

    # Loop 5 through 10 for Player 2's questions
    print("Player 2")
    for i in range(5,10):
        question = questionList[i]
        print(question)
        try:
            res = int(input("\nEnter your choice: "))
            print()
            if res == int(question.getCorrectAnswer()):
                player2 += 1 # Add to player2
        except ValueError:
            print("Invalid answer. No points are awarded.")

    # Compare scores
    if player1 > player2:
        print("Player 1 wins!")
    elif player1 < player2:
        print("Plater 2 wins!")
    else:
        print("Both players have tied!")
    print("Player 1: " + str(player1) + " point(s).")
    print("Player 2: " + str(player2) + " point(s).")

# Call the main function
main()