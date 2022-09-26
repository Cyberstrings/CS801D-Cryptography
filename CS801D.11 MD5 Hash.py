# MD5 (Message Digest 5) Hashing Cipher Algorithm:
#1. Original message = M.
#2. Pad (append) bits to M and make M1 such that M1 = 448 modulo 512; or, M1 + 64 is a multiple of 512.
#3. Append a 64 bit value (indicating length of M1) after M1 to make P. The length of P is now divisible by 512.
#4. Initialize four buffer words, say, A, B, C, D such that:
#4. A = 01234567, B = 89abcdef, C = fedcab98, D = 76543210 (Processing hexadecimal values, so 0 to F are valid).
#5. Break P into chunks of 512 bits (1 bit = 0 or 1); lets call the chunks P[0], P[1]... P[N-1]. Total length is say L = 512*N.
#6. Define 4 functions, each taking 3 arguments: F(X,Y,Z), G(X,Y,Z), H(X,Y,Z), I(X,Y,Z), X/Y/Z being 32 bits, such that:
#6. F(X,Y,Z) = (X and Y) or (~X and Z)
#6. G(X,Y,Z) = (X and Y) or (Y and ~Z)
#6. H(X,Y,Z) = X xor Y xor Z
#6. I(X,Y,Z) = Y xor (X or ~Z)
#7. Then do the following in loop:
'''
# L is length = 512*N and LL be the number of 32 bit words in the final message P.
T[i] = set of 64 unique constants, T[0], T[1] ... T[63].

For i = 0 to (LL/16)-1 do:

	# Copy block i into X => For round 1, X[0] = P[0], X[1] = P[1] etc, for round 2, X[0] = P[16], X[1] = P[17] etc.
	For j = 0 to 15 do
		X[j] := P[i*16+j].
	End of j loop.

	# Save A as AA, B as BB, C as CC, and D as DD.
	AA = A
	BB = B
	CC = C
	DD = D

	# Round 1:
	# Let [PQRS k s i] denote the operation: P = Q + ((P + F(Q,R,S) + X[k] + T[i]) <<< s).
	# <<< s: meaning left shift s bits
	# Do the following 16 operations rowwise:
	[ABCD  0  7  1]  [DABC  1 12  2]  [CDAB  2 17  3]  [BCDA  3 22  4]
	[ABCD  4  7  5]  [DABC  5 12  6]  [CDAB  6 17  7]  [BCDA  7 22  8]
	[ABCD  8  7  9]  [DABC  9 12 10]  [CDAB 10 17 11]  [BCDA 11 22 12]
	[ABCD 12  7 13]  [DABC 13 12 14]  [CDAB 14 17 15]  [BCDA 15 22 16]

    	# Round 2:
	# Let [PQRS k s i] denote the operation: P = Q + ((P + G(Q,R,S) + X[k] + T[i]) <<< s).
	# <<< s: meaning left shift s bits
	# Do the following 16 operations rowwise:
    	[ABCD  1  5 17]  [DABC  6  9 18]  [CDAB 11 14 19]  [BCDA  0 20 20]
    	[ABCD  5  5 21]  [DABC 10  9 22]  [CDAB 15 14 23]  [BCDA  4 20 24]
    	[ABCD  9  5 25]  [DABC 14  9 26]  [CDAB  3 14 27]  [BCDA  8 20 28]
    	[ABCD 13  5 29]  [DABC  2  9 30]  [CDAB  7 14 31]  [BCDA 12 20 32]

    	# Round 3:
	# Let [PQRS k s i] denote the operation: P = Q + ((P + H(Q,R,S) + X[k] + T[i]) <<< s).
	# <<< s: meaning left shift s bits
	# Do the following 16 operations rowwise:
    	[ABCD  5  4 33]  [DABC  8 11 34]  [CDAB 11 16 35]  [BCDA 14 23 36]
    	[ABCD  1  4 37]  [DABC  4 11 38]  [CDAB  7 16 39]  [BCDA 10 23 40]
    	[ABCD 13  4 41]  [DABC  0 11 42]  [CDAB  3 16 43]  [BCDA  6 23 44]
    	[ABCD  9  4 45]  [DABC 12 11 46]  [CDAB 15 16 47]  [BCDA  2 23 48]

    	# Round 4:
	# Let [PQRS k s i] denote the operation: P = Q + ((P + I(Q,R,S) + X[k] + T[i]) <<< s).
	# <<< s: meaning left shift s bits
	# Do the following 16 operations rowwise:
    	[ABCD  0  6 49]  [DABC  7 10 50]  [CDAB 14 15 51]  [BCDA  5 21 52]
    	[ABCD 12  6 53]  [DABC  3 10 54]  [CDAB 10 15 55]  [BCDA  1 21 56]
    	[ABCD  8  6 57]  [DABC 15 10 58]  [CDAB  6 15 59]  [BCDA 13 21 60]
    	[ABCD  4  6 61]  [DABC 11 10 62]  [CDAB  2 15 63]  [BCDA  9 21 64]

	# Then perform the following additions.
	# Increment each of the four registers by the value it had before this block was started.
	A = A + AA
	B = B + BB
	C = C + CC
	D = D + DD

End of i loop.
'''
#8. End of all loops. Append ABCD to form the output.
#9. ABCD = 32 digit hexadecimal number.


import hashlib
  
str2hash = "This is an article about the cryptography algorithm"  
result = hashlib.md5(str2hash.encode())
  
print("The hexadecimal equivalent of hash is: ", end ="")
print(result.hexdigest())
