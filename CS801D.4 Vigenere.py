# Vigenere Cipher
#1. Dynamic shift. Let key = ACE, message = ATTACKED.
#2. Get numeric value of key in the order A=0, B=1, C=2, D=3... Z=25. So for ACE, the value would be A=0, C=2, E=4. This will be required later.
#3. Get length of message (ATTACKED = 8 letters) and key (ACE = 3 letters). Compare key length with message length.
#5. If key is shorter, concatenate key, letter by letter, until key length becomes equal to plaintext length.
#6. If key is longer, truncate key, letter by letter, until key length becomes equal to the plaintext length.
#7. Our key (length 3) < plaintext (length 8), so concatenated key of length 8 is ACEACEAC.
#8. Make a keyshift[] which will store the numeric value of key[]. Our key[] = [A,C,E,A,C,E,A,C], so keyshift[] = [0,2,4,0,2,4,0,2].
#9. Now shift plaintext[i] by the number of places equal to keyshift[i].
#10. ATTACKED = [A,T,T,A,C,K,E,D] => shift => [A+0, T+2, T+4, A+0, C+2, K+4, E+0, D+2] => [A,V,X,A,E,O,E,F]. So ciphertext = AVXAEOEF
#11. To decrypt, follow same process. Subtract the positions from ciphertext and you will obtain plaintext.

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generateKey(string, key): #To concatenate or truncate key
    key = list(key)
    l = len(string)
    k = len(key)
    if l == key:
        return(key)
    elif l < k:
        keys = "".join(key) #Convert from list to string
        return keys[0:l] #Return truncated key upto length l
    else:
        for i in range(len(string)-len(key)):
            key.append(key[i % len(key)])
        return("" . join(key))

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
    l = len(plaintext)
    conckey = generateKey(plaintext, key)
    conckey = prune(conckey)
    print("Modified key is: "+conckey)
    cipher_text = []
    for i in range(len(plaintext)):
        print("conckey[i] is: "+conckey[i])
        shiftval = alpha.index(conckey[i]) #Get index of key's letter
        currentval = alpha.index(plaintext[i])
        cipher_text.append(alpha[(currentval+shiftval)%26]) #Shift
    cipher = "".join(cipher_text)
    print("Cipher Text is: "+cipher)

def decrypt(key): #A different approach to decryption
    print("Enter ciphertext: ")
    ciphertext = input()
    ciphertext = prune(ciphertext)
    key = generateKey(ciphertext, key)
    key = prune(key)
    plain = []
    for i in range(len(ciphertext)):
        x = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        plain.append(chr(x))
    plaintext = "".join(plain)
    print("Plain Text is: "+plaintext)

while(1):
    print("Welcome to Vigenere Cipher! \n 1. Encrypt \n 2. Decrypt \n 0. Exit: ")
    choice = int(input("Choose: "))
    if choice==1:
        print("Enter key: ")
        k = input()
        encrypt(k)
    elif choice==2:
        print("Enter key: ")
        k = input()
        decrypt(k)
    elif choice==0:
        exit()
    else:
        print("Incorrect choice")
