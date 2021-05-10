# Nicolas DeJohn | Chapter 9-3 Lab | March 26 2021

'''
The purpose of this program is to take an unencrypted text file and encrypt it using a dictionary of codes. Then, it's to use the same
dictionary to decrypt the encrypted file.

'''

import collections
import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 9")
cwd = os.getcwd()

# Initialize the code dictionary
code = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
            'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
            'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
            'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
            'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
            'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
            'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
            'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
            'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
            '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
            '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
            '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
            ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
            "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
            '{':'[','[':'{','}':']',']':'}'}

# Main function
def main():
    # Encrypts the unencrypted file
    encrypt()
    # Decrypts the encrypted file
    decrypt()
    # Shows where both files have been created
    print("\nThe files 'encryptedText.txt' and 'decryptedText.txt' have been created in '" + cwd + "'\n")

# Encrypts the file
def encrypt():
    # Opens the unencrypted file and reads it
    unencryptedFile = open('unencryptedText.txt', 'r')
    fileRead = unencryptedFile.read()
    unencryptedFile.close()
    # Opens a new file to write the encryption
    encryptFile = open('encryptedText.txt' , 'w')

    # Loop through each character in the unencrypted file
    for ch in fileRead:
        # If the character is a key in the code dictionary..
        if ch in code:
            encryptFile.write(code[ch]) # Write the value of that key to the file
        else:
            encryptFile.write(ch) # Write the character to that value. Covers spaces and new lines.
    encryptFile.close()

# Decrypts the encrypted file
def decrypt():
    # Opens the encrypted file and reads it
    encryptFile = open('encryptedText.txt', 'r')
    readFile = encryptFile.read()
    encryptFile.close()
    # Opens a new file to write the decrypted message
    decryptFile = open('decryptedText.txt', 'w')

    # Loop through each character in the file
    for ch in readFile:
        # Checks if ch is a space or newline and writes it
        if ch == " " or ch == "\n":
            decryptFile.write(ch)
        else:
            # If ch is a key in code
            if code[ch]:
                # Write the value of the key
                decryptFile.write(code[ch])
# Call the main function
main()
