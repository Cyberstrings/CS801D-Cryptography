# Rail Fence Cipher:
#1. Written diagonally zigzag way and then read horizontally.
#2. Length of diagonal is the key. Say key = 3, msg=ATTACK AT DAWN. Then:
#3. A......C.......D.........												
#3. .T...A...K...T...A...N...												
#3. ...T.......A.......W..... Cipher (read rowwise): ACDTAKTANTAW. Now, if the key = 4, then:
#4. A........A..........
#4. .T.....K...T.....N..
#4. ..T..C......D..W....
#4. ...A.........A...... Cipher (read rowwise): AATKTNTCDWAA. And so on.
#5. Algorithm: Represent each rail (row/line)  as a list. Use a loop variable, and add space or letters in the list to populate.
#6. Like, when we append A in list 1, append space in lists 2 and 3. When append T in list 2, append space in lists 1 and 3, etc.
#7. When you print the lists, it will give a zigzag feeling.

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

def print_rail(fence):
	for i in fence:
		print(i)

def encrypt(key):  #Encryption
	#print("Enter plaintext: ")
	#plaintext = input()
	plaintext = 'GeeksforGeeks '
	plaintext = prune(plaintext)
	fence = [[] for i in range(key)]  #Creating lists for the rows
	rail = 0
	var = 1
	for char in plaintext: 
		fence[rail].append(char) #Append the character at the proper row
		sp = ' '
		for i in range(key):
			m = (rail+i)%key
			if m != rail: #If its the row where the letter has just been added, skip.
				fence[(rail+i)%key].append(sp) #Append space to the OTHER two rows to give it a zigzag feel
		rail += var 
		if rail == key-1 or rail == 0:
			var = -var
	res = ''
	print_rail(fence)
	for i in fence:
		for j in i:
			res = res + j
	print("Cipher is: ")
	res = prune(res) #Remove the spaces from res
	print(res)


def decrypt(n):  #decryption
	print("Enter ciphertext: ")
	ciphertext = input()
	cipher = prune(ciphertext)
	plain = ''
	fence = [[] for i in range(n)]
	rail = 0
	var = 1
	for char in cipher:
		fence[rail].append(char)
		rail += var
		if rail == n-1 or rail == 0:
			var = -var
	rFence = [[] for i in range(n)]
	i = 0
	l = len(cipher)
	s = list(cipher)
	for r in fence:
		for j in range(len(r)):
			rFence[i].append(s[0])
			s.remove(s[0])
		i += 1
	rail = 0
	var  = 1
	r = ''
	for i in range(l):
		r += rFence[rail][0]
		rFence[rail].remove(rFence[rail][0])
		rail += var
		if rail == n-1 or rail == 0:
			var = -var
	print("The plaintext is: ")
	print(r)

while(1):
	print("Welcome to Rail Fence Cipher! \n 1. Encrypt \n 2. Decrypt \n 0. Exit: ")
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
		
