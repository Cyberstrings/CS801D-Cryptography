# Columnar Transposition Cipher:
#1. Message written out in column, and then read in rows, in a specified order. Number of columns depends on length of key.
#2. The order is specified by the key's letters' relative position and their position on the alphabet.
#3. Say message: Attack at dawn, key: hack. Then:
#4. A...T...T...A
#4. C...K..._...A
#4. T..._...D...A
#4. W...N..._..._
#5. Key: hack, alphabetically, a comes first, then c, h, k. In key, a comes 2nd, c comes 3rd, h comes 1st, k comes 4th.
#6. So order of reading columns: 2nd, 3rd, 1st, 4th. Cipher: TK NT D ACTWAAA
#7. If key: pork, Then alphabetically, k < o < p < r, and key position wise, k = 4, o = 2, r = 3, p = 1.
#8. So order of reading columns would have beem 4th, 2nd, 3rd, 1st. Cipher: AAA TK NT D ACTW
#9. If key would have been 5 letters, then the matrix would be ax5. (5 columns)
#10. Decryption: To decipher it, the recipient has to work out the column lengths by dividing the message length by the key length.
#11. Then, write the message out in columns again, then re-order the columns by reforming the key word.

import math

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

def orderin(key): #This function studies the key and returns the list of orders in which the columns must be read (See steps 5, 6).
	keylist = []
	k = list(key)
	for i in k:
		if i not in keylist:
			keylist.append(i) #Adds the key, letter by letter, into the list, and removes duplicates. Better than list(key).
	rorder = []
	a = list(alpha)
	for i in alpha:
		if i in keylist:
			rorder.append(keylist.index(i))
	return rorder

def encrypt(key):  #Encryption
	print("Enter plaintext: ")
	plaintext = input()
	#plaintext = 'Attack at daw'
	plaintext = prune(plaintext)
	cipher = ''
	msg_len = len(plaintext)
	msg_lst = list(plaintext)
	col = len(key)
	row = int(math.ceil(msg_len / col)) #Calculate maximum row of the matrix
	fill_null = int((row * col) - msg_len) #Calculate number of empty spaces
	msg_lst.extend('-' * fill_null) #Add the padding character '-' in empty
	matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)] #Create Matrix and insert message, padding chars row-wise 
	for i in matrix:
		print(i)
	readorder = orderin(key)
	print(readorder)
	for i in readorder:
		for j in range(row):
			print(matrix[j][i], end=' ')
	print()

def decrypt(key):  #decryption
	print("Enter ciphertext: ")
	ciphertext = input()
	#ciphertext = 'TKATAWACDAT'
	ciphertext = prune(ciphertext)
	msg_len = len(ciphertext)
	msg_lst = list(ciphertext)
	col = len(key)
	row = int(math.ceil(msg_len / col)) #Calculate maximum row of the matrix
	fill_null = int((row * col) - msg_len) #Calculate number of empty spaces
	msg_lst.extend('-' * fill_null) #Add the padding character '-' in empty
	#matrix = [for i in range(0, len(msg_lst), col)] #Create Matrix and insert message, padding chars row-wise 
	matrix = [[0 for x in range(col)] for y in range(row)] 
	readorder = orderin(key)
	msg_lst.reverse()
	for i in readorder: 
		for j in range(row):
			matrix[j][i] = msg_lst.pop()
	for i in matrix:
		print(i)

while(1):
	print("Welcome to Columnar Tranposition Cipher! \n 1. Encrypt \n 2. Decrypt \n 0. Exit: ")
	choice = int(input("Choose: "))
	if choice==1:
		print("Enter key: ")
		k = input()
		k = prune(k)
		encrypt(k)
	elif choice==2:
		print("Enter key: ")
		k = input()
		k = prune(k)
		decrypt(k)
	elif choice==0:
		exit()
	else:
		print("Incorrect choice")

