# Nicolas DeJohn | Chapter 10-9 Lab | April 3 2021

''' '''

import collections
import os 
os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 10")

import Question
import GenerateQuestion

questionList = []
generateQuestion()

player1 = 0

for i in range(0,5):
    ques = questionList[i]
    print(ques)
    try:
        res = int(input("\n Enter your choice: "))
        if res == int(ques.getCorrectAnswer()):
            player1 += 1
    except ValueError:
        print("Enter the option number")

print(player1)