# Nicolas DeJohn | Chapter 8-5 Lab | March 1st 2021
'''The purpose of this program is to format a phone number that contains letters into one that contains only numbers while mainting the '###-###-####' format.'''

#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 8")


def main(): # Defines the main function

    userPhoneNumber = str(input("Enter the number in the format of XXX-XXX-XXXX: ")) # Asks the user for a phone number in the correct format and converts to a string.
    userPhoneNumberSplit = userPhoneNumber.replace("-", "") # Formats the users input by removing the hyphens.
    numericPhoneNumber = '' # This variable serves as a blank canvas to store the new converted number.
    convertedNumber = phoneNumberConversion(userPhoneNumberSplit, numericPhoneNumber) # This variable holds the returned value of the function.
    print(convertedNumber) # Prints the converted phone number.

def phoneNumberConversion(userPhoneNumberSplit, numericPhoneNumber): # Defines the function that converts the users input.
    count = 0 # The next two variables will be used to track when to add the hyphens back in...
    sectionCount = 0 # ..this is use to track the sections of the number groupings..
    for ch in userPhoneNumberSplit: # For character in the string..
        # I won't write a comment on every line but this conditional set tests each letter in ch and adds the properly assigned number to the new string.
        if ch.isdigit():  
            numericPhoneNumber += ch
        elif ch.upper() in 'ABC':
            numericPhoneNumber += '2'
        elif ch.upper() in 'DEF':
            numericPhoneNumber += '3'
        elif ch.upper() in 'GHI':
            numericPhoneNumber += '4'
        elif ch.upper() in 'JKL':
            numericPhoneNumber += '5'
        elif ch.upper() in 'MNO':
            numericPhoneNumber += '6'
        elif ch.upper() in 'PQRS':
            numericPhoneNumber += '7'
        elif ch.upper() in 'TUV':
            numericPhoneNumber+= '8'
        elif ch.upper() in 'WXYZ':
            numericPhoneNumber += '9'
        count += 1 # Adding to the count until it reaches 3. Then...
        if count == 3 and sectionCount != 2: # I'm using count to keep track of every 3 numbers and then inserting a hyphen.
            numericPhoneNumber += '-' # Adds the hyphen to the string.
            count = 0 # Resets the count for the next number grouping.
            sectionCount += 1 # Because the last set of numbers are 4 digits, I'm using this to stop after the seconding grouping of numbers.
    return numericPhoneNumber # Show me the money. 

main() # Ta-daaa



    
    
    

