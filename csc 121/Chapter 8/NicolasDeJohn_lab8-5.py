# Nicolas DeJohn | Chapter 7-2 Lab | January 24th 2021


import os 
os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 8")
def main():
    userPhoneNumber = str(input("Enter the number in the format of XXX-XXX-XXXX: "))
    userPhoneNumberSplit = userPhoneNumber.split("-")

    weird_character = False

    count = 0

    numericPhoneNumber = ''

    while weird_character == False and count < 3:
        for ch in userPhoneNumberSplit:
            if ch.isdigit():
                userPhoneNumberSplit += ch
            elif ch.upper() in 'ABC':
                userPhoneNumberSplit += '2'
            elif ch.upper() in 'DEF':
                userPhoneNumberSplit += '3'
            elif ch.upper() in 'GHI':
                userPhoneNumberSplit += '4'
            elif ch.upper() in 'JKL':
                userPhoneNumberSplit += '5'
            elif ch.upper() in 'MNO':
                userPhoneNumberSplit += '6'
            elif ch.upper() in 'PQRS':
                userPhoneNumberSplit += '7'
            elif ch.upper() in 'TUV':
                userPhoneNumberSplit += '8'
            elif ch.upper() in 'WXYZ':
                userPhoneNumberSplit += '9'
            else: weird_character = True
        if count != 2:
            numericPhoneNumber += "-"
        count += 1
    if weird_character:
        print("weird character")
    else:
        print(numericPhoneNumber)

main()



    
    
    

