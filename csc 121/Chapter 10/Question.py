# Nicolas DeJohn | Chapter 10-9 Lab | April 3 2021

'''The purpose of this program is to create a class for a trivia question with answers'''

#import collections
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 10")

class Question:

    # Sets the data attributes when the question is initialized
    def __init__(self, question,answer1,answer2,answer3,answer4,correctAnswer):

        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correctAnswer = correctAnswer

    # Mutators        
    def changeAnswer1(self,answer1):
        self.answer1 = answer1

    def changeAnswer2(self,answer2):
        self.answer2 = answer2

    def changeAnswer3(self,answer3):
        self.answer3 = answer3

    def changeAnswer4(self,answer4):
        self.answer4 = answer4

    def changeCorrectAnswer(self,correctAnswer):
        self.correctAnswer = correctAnswer 

    # Returns the question with the answers
    def __str__(self):
        return self.question + '\n 1. ' + str(self.answer1)+'\n 2. ' + str(self.answer2) + '\n 3. '+ str(self.answer3) + '\n 4. '+str(self.answer4)

    # Returns the correct answer
    def getCorrectAnswer(self):
        return self.correctAnswer

    # Returns a list of answers for the question
    def getAnswerChoice(self):
        return [self.answer1,self.answer2,self.answer3,self.answer4]

    # Returns the question         
    def getQuestion(self):
        return self.question