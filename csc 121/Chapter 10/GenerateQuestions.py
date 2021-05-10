# Nicolas DeJohn | Chapter 10-9 Lab | April 3 2021

'''The purpose of this program is to create a series of questions and answers and append them to a list'''

#import collections
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 10")

import Question

# Initialize an empty list
questionList = []

# Creates 10 questions and appends each one to questionList
def generateQuestion():
    question = Question.Question('How many legs does a spider have?','4','8','6','2',2);
    questionList.append(question)

    question = Question.Question('What is the color of an emerald?','Green','Blue','Orange','Red',1);
    questionList.append(question)

    question = Question.Question('What is the name of the fairy in Peter Pan?','Woody','Flora','Tank','Tinkerbell',4);
    questionList.append(question)

    question = Question.Question('If you freeze water, what do you get?','Orange Juice','Ice','Milk','Money',2);
    questionList.append(question)

    question = Question.Question('What colors are the stars on the American flag?','Red','Blue','White','Green',3);
    questionList.append(question)

    question = Question.Question('Where does the President of the United States live while in office?','New York','Home','White House','Outside',3);
    questionList.append(question)

    question = Question.Question('Which ocean is off the California coast?','Pacific','Indian','Atlantic','Arctic',1);
    questionList.append(question)

    question = Question.Question('What fruit do kids traditionally give to teachers?','Watermelon','Apple','Peach','Grapes',2);
    questionList.append(question)

    question = Question.Question('Who is Mickey Mouse’s girlfriend?','Betty Boop','Chucky Cheese','Minnie Mouse','Wonder Woman',3);
    questionList.append(question)

    question = Question.Question('Which state is famous for Hollywood?','Utah','North Carolina','New York','California',4);
    questionList.append(question)

    # Returns the list
    return questionList

