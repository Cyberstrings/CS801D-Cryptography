# Caesar Cipher/Generic Shift Cipher Algorithm:
#1. Each letter is replaced with the letter located n places down the alphabets. The n is the key length.
#2. If n=3, then it is called Caesar Cipher. But it is not really a cipher as its key length is fixed.
#3. Example: APPLE -> (key=3) -> DSSOH; ATTACKATONCE -> (key=4) -> EXXEGOEXSRGI

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def prune(text): #To cut off all punctuations and transform to uppercase
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    nums = '1234567890'
    for letter in text:
        if letter in punc or letter in nums:
            text = text.replace(letter, "")
    text=text.replace(" ", "")
    text=text.upper()
    return text

def encrypt(key):  #Encryption
    print("Enter plaintext: ")
    plaintext = input()
    plaintext = prune(plaintext)
    cipher = ''
    for i in plaintext:
        indx = alpha.index(i)
        cipher = cipher + alpha[(indx+key)%26]
    print("Cipher Text is: "+cipher)

def decrypt(key):  #decryption
    print("Enter ciphertext: ")
    ciphertext = input()
    ciphertext = prune(ciphertext)
    plain = ''
    for i in ciphertext:
        indx = alpha.index(i)
        plain = plain + alpha[(indx-key)%26]
    print("Plain Text is: "+plain)

while(1):
    print("Welcome to Shift Cipher! \n 1. Encrypt \n 2. Decrypt \n 0. Exit: ")
    choice = int(input("Choose: "))
    if choice==1:
        print("Enter key length: ")
        k = int(input())
        encrypt(k)
    elif choice==2:
        print("Enter key length: ")
        k = int(input())
        decrypt(k)
    elif choice==0:
        exit()
    else:
        print("Incorrect choice")
