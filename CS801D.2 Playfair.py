#Playfair Cipher:
#1. Make 5x5 Matrix.
#2. Set a Key (say, MONARCHY). Write it in the matrix such that, a[0][0]=M, a[0][1]=O, a[0][2]=N, a[0][3]=A etc (populate row-wise).
# [M, O, N, A, R]
# [C, H, Y, B, D]
# [E, F, G, I, K]
# [L, P, Q, S, T]
# [U, V, W, X, Z]
#3. MONARCHY appears at the top of the matrix, then the other alphabets in alphabetical order, such that:
#3a. 1) Each alphabet appears only once in the matrix.
#3b. 2) I/J treated as same letter I.
#4. Now, set a plaintext (say, BALLOONS). Replace all J with I in the text.
#5. Split it into groups of 2: BA, LX(Repeating letters like LL, AA, MM not allowed, so X is used as filler), LO, ON, SX.
#6. Encrypt each group (BA, LX, LO, ON, SX) following some rules:
#6a. For BA & SX, B and A both are in same column, column 4, replace them both by the letter below them in the matrix. BA => IB. SX => XA.
#6b. For LX & LO, L => Element at L's row X's column, X => Element at X's row L's column => LX => SU. For LO => Same rules => PM.
#6d. For ON, O and N both are in same row, row 1, replace them both by the letter on the right to them in the matrix. ON => NA.

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

def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]

def makematrix(key):
    result = list()
    key = prune(key)
    for c in key: #storing key
        if c not in result:
            if c=='J':
                result.append('I')
            else:
                result.append(c)
    flag=0

    for i in alpha: #storing other character
        if i not in result:
            if i=="I" and "J" not in result:
                result.append("I")
                flag=1
            elif flag==0 and i=="I" or i=="J":
                pass
            else:
                result.append(i)

    k=0
    my_matrix=matrix(5,5,0) #initialize matrix
    for i in range(0,5): #making matrix
        for j in range(0,5):
            my_matrix[i][j]=result[k]
            k+=1
    return my_matrix

def locindex(c, my_matrix): #get location of each character
    loc=list()
    row = 0
    if c=='J':
        c='I'
    for i,j in enumerate(my_matrix):  #Pick up each row and enumerate
        #print(j)
        for k,l in enumerate(j): #Pick up each element in row
            if c == l:
                loc.append(i)
                loc.append(k)
    return loc

def encrypt(key):  #Encryption
    msg=str(input("Enter message/plain text: "))
    #msg="instruments"
    msg=prune(msg)
    print("Key used is: ",key)
    my_matrix = makematrix(key)
    for row in my_matrix:
        print(row)
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        if msg[len(msg)-1] == 'X':
            msg=msg[:]+'Z' #If length is odd and ends with X, add Z at the end
        else:
            msg=msg[:]+'X' #If length is odd, add X at the end
    print("Cipher Text: ")
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i], my_matrix) #Group plaintext into two letters, i and i+1
        loc1=list()
        loc1=locindex(msg[i+1], my_matrix)
        if loc[1]==loc1[1]: #Same column
            x = my_matrix[(loc[0]+1)%5][loc[1]]
            y = my_matrix[(loc1[0]+1)%5][loc1[1]]
            print(x+" "+y+" ")
        elif loc[0]==loc1[0]: #Same row
            x = my_matrix[loc[0]][(loc[1]+1)%5]
            y = my_matrix[loc1[0]][(loc1[1]+1)%5]
            print(x+" "+y+" ")
        else:
            x = my_matrix[loc[0]][loc1[1]]
            y = my_matrix[loc1[0]][loc[1]]
            print(x+" "+y+" ")
        i=i+2

def decrypt(key):  #decryption
    msg=str(input("Enter cipher text: "))
    #msg="gatlmzclrqxa"
    msg=prune(msg)
    print("Key used is: ",key)
    my_matrix = makematrix(key)
    for row in my_matrix:
        print(row)
    print("Plain text: ")
    i = 0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i], my_matrix)
        loc1=list()
        loc1=locindex(msg[i+1], my_matrix)
        if loc[1]==loc1[1]:
            x = my_matrix[(loc[0]-1)%5][loc[1]]
            y = my_matrix[(loc1[0]-1)%5][loc1[1]]
            print(x+" "+y+" ")
        elif loc[0]==loc1[0]:
            x = my_matrix[loc[0]][(loc[1]-1)%5]
            y = my_matrix[loc1[0]][(loc1[1]-1)%5]
            print(x+" "+y+" ")
        else:
            x = my_matrix[loc[0]][loc1[1]]
            y = my_matrix[loc1[0]][loc[1]]
            print(x+" "+y+" ")
        i=i+2


while(1):
    print("Welcome to Playfair Cipher! \n 1. Encryption \n 2. Decryption \n 0. Exit")
    choice=int(input("Choose: "))
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
