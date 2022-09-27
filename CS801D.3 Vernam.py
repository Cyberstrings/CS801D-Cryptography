# Vernam Cipher (One Time Pad) Algorithm:
#0. Asymmetric algorithm, so needs separate encryption/public key and decryption/private key.
#0. Only available algorithm which is unbreakable but requires the use of a single-use pre-shared key that is of same length as the message being sent.
#1. Say our message = M, with each bit being M[i] i.e. M[0], M[1], M[2], M[3]... so on
#2. Generate a key K of same length as M, with each bit being denoted as K[i] i.e. K[0], K[1], K[2], K[3]... so on.
#3. Now perform a PRE-DETERMINED operation (Like, bitwise XOR, or addition modulo 26) like:
#3. C[i] = (M[i] + K[i]) mod 26, or,
#3. C[i] = M[i] xor K[i], or,
#3. We can convert each letter -> ASCII or numeric value -> binary, then perform binary XOR, for example:
#3. plaintext = OAK and key = SON. So, OAK xor SON = (O, A, K) xor (S, O, N) = (14, 00, 10) xor (18, 14, 13) = (01110, 00000, 01010) xor (10010, 01110, 01101) = (11100, 01110, 00111)
#3. (11100, 01110, 00111) = (28, 14, 7) = (28 % 26, 14, 7) = (2, 14, 7) = (C, O, H) = COH is our cipher.
#4. Transport both C and K to the user.
#5. To decrypt, perform XOR again with the key: (11100, 01110, 00111) xor (10010, 01110, 01101) = (01110, 00000, 01010) = OAK which is our plaintext.
#5. Or if we have done the modulo operator, subtract this time to obtain back ciphertext.

'''
Program approach:
#1. Assign each alphabet with corresponding integer e.g. A = 0, B = 1, C = 2, ... Z = 25.
#2. Convert message (say, "Hello") to integer value (7, 5, 11, 11, 14); M[0] = 7, M[1] = 5, ... M[4] = 14.
#3. Generate a random key which is the same size as the message. Say, wivfa (22, 8, 21, 5, 0); K[0] = 22, K[1] = 8, ... K[4] = 0.
#4. Now perform a PRE-DETERMINED operation (Like, bitwise XOR, or addition modulo 26).
#4. For now, we will do addition modulo 26 for each corresponding alphabet: C[i] = (M[i] + K[i]) mod 26
#5. So, C[0] = (M[0] + K[0]) mod 26 = 29 mod 26 = 3; C[1] = (M[1] + K[1] mod 26) = 12 mod 26 = 12, and so on.
#6. At end, we obtain: C = (3, 12, 6, 16, 14) = construct back into alphabet = "dmgqo" which is our encrypted text.
#7. Similarly, we take our encrypted text and subtract the key value, to obtain plaintext.
'''

import random
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def texttonum(plain_text):
    plain_num = []
    for i in plain_text:
        indx = alpha.index(i)
        plain_num.append(indx)
    return plain_num

def keygen(plain_text):
    key = []
    for i in range(1, len(plain_text)+1):
        j = random.randrange(0, 25) #To keep it alphabetical we choose between 0 to 25
        key.append(j)
    print("Random key:", key)
    return key

def encrypt(plain_text, key):
    cipher_num = []
    cipher_text = []
    plain_text = plain_text.upper()
    plain_num = texttonum(plain_text)
    for i in range(0, len(plain_text)):
        cipher_num.append((plain_num[i] + key[i]) % 26)
        cipher_text.append(alpha[cipher_num[i]])
    cipher = ''.join(cipher_text)
    print("Cipher:", cipher)
    return cipher_num

def decrypt(cipher_num, key):
    decrypted_text = []
    decrypted_num = []
    for i in range(0, len(cipher_num)):
        decrypted_num.append((cipher_num[i] - key[i]) % 26)
        decrypted_text.append(alpha[decrypted_num[i]])
    plain = ''.join(decrypted_text)
    return plain


if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    print("Vernam Cipher/One Time Pad Encryptor-Decryptor")
    print(" ")
    string1 = input("Step 1) Enter plain text: ")

    print("Step 2) Generating your public / private key-pairs now . . .")
    key = keygen(string1)

    print("Step 3) Encrypting the text: ")
    cnum = encrypt(string1, key)

    print("Step 4) Decrypting message. . .")
    print("Step 5) Your message is:", decrypt(cnum, key))

    print(" ")
    print("Thank you for using Vernam Cipher!")
