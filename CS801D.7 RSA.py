# RSA (Rivest-Shamir-Adleman Encryption) Algorithm:
#0. Asymmetric algorithm, so needs separate encryption/public key and decryption/private key.
#1. Choose two random large prime numbers, P and Q.
#2. Calculate product N = P*Q. N and D(N) = (P-1)*(Q-1).
#3. N is the first part of the public key. Now, pick an integer E such that:
    #3.1. E and D(N) is mutually prime i.e. they have no common factor other than 1. So, HCF(e, D(N)) = 1.
    #3.2. 1 < E < D(N)
#4. <E, N> is our public key. Support plaintext = P, then:
#4. Cipher C = P^E mod N. [Mod means modulus or remainder. So P^E - N would be divisible by C]
#5. We pick a number D so that D != E and D*E = 1 mod D(N). [D(N) - 1 would be divisible by D*E]
#6. <D, N> is our private key. If cipher = C, then:
#6. Plaintext P = C^D mod N. [C^D - N would be divisible by P, i.e. P % N = C^D]

'''
This program takes a string input say 'apple', converts it into an ASCII integer array say [97, 112, 112...].
Then it will perform RSA on each of the elements in the array separately and concatenate them together to generate one number array.
In decryption, each of that resultant array is decrypted back to its ASCII and converted to text.

For the decryption to work, the N (product of P and Q) has to be greater than the ASCII value range (i.e. 65 to 122). So P and Q must be sufficently large.
If we pick P = 3 and Q = 11, they are prime but their product 33 < 65 so it wont work while decryption.
So for RSA to work, 0 <= plaintext < product of p * q, which is why at Step #1, we chose random LARGE prime numbers.
Source: https://en.wikipedia.org/wiki/RSA_%28algorithm%29#Encryption

In RSA, there can be specific scenarios where plaintext = ciphtertext. For example: say, p = 17 and q = 37, n = 629, e = 433, d = 145.
In such case, all conditions satisfy. When we try to encrypt 'apple' = [97, 112, 112, 108, 101], for example, then:
97^433 mod 629 = 97, or 112^433 mod 629 = 112, 108^433 mod 629 = 108 and so on.
This is a specific case in RSA when m mod n = m^e, or, m^e = m mod p and m^e = m mod q.
'''

import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    #As divisibility by 2 already checked before, we start from 3 and check only odd numbers
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

def mod_inverse(a, m):
    #Input: E, D(N). Output: D such that D*E = 1 mod D(N)
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def modular_pow(base, exponent, modulus): #base = encrypted msg, exp = D, modulus = N
    if modulus == 1:
        return 0
    c = 1
    for e_prime in range (0, exponent-1):
        c = (c * base) % modulus
    return c

def multi_inverse_1(e, phi):
    #Input: E, D(N). Output: D such that D*E = 1 mod D(N) using Eucledian algorithm
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    if temp_phi == 1:
        return d + phi

def multi_inverse(a, m) :
    m0 = m
    y = 0
    x = 1
    if (m == 1) :
        return 0
    while (a > 1) :
        # q is quotient
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        # Update x and y
        y = x - q * y
        x = t
    # Make x positive
    if (x < 0) :
        x = x + m0
    return x

def generate_key_pair(p, q):
    if not is_prime(p):
        raise ValueError('First number is not prime.')
    elif not is_prime(q):
        raise ValueError('Second number is not prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    #n = pq
    n = p*q
    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(2, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(2, phi)
        g = gcd(e, phi)
    print("Step 3.1: Random chosen value of e = ", e)

    #Use Extended Euclid's Algorithm to generate the private key
    d = multi_inverse(e, phi)

    #If d and e become equal, it is less secure. In such event, choose d and e again:
    while d == e:
        print("Step 3.2: Value of d = ", d)
        print("Oops! Value of d same as e. Choosing again. . .")
        e = random.randrange(2, phi)
        g = gcd(e, phi)
        while g != 1:
            e = random.randrange(2, phi)
            g = gcd(e, phi)
        print("Step 3.1: Random chosen value of e = ", e)
        d = multi_inverse(e, phi)
    print("Step 3.2: Value of d = ", d)

    #Return public and private key_pair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    e, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m (Pow(a, b, c) = a^b mod c)
    plain = [ord(char) for char in plaintext]
    print("Plain: ", plain)
    cipher = [pow(ord(char), e, n) for char in plaintext]
    print("Cipher: ", cipher)
    #Return the array of bytes
    return cipher

def decrypt(pk, ciphertext):
    try:
        #Unpack the key into its components
        d, n = pk
        #Generate the plaintext based on the ciphertext and key using a^b mod m
        aux = [str(pow(char, d, n)) for char in ciphertext]
        print("Aux: ", aux)
        #Return the array of bytes as a string
        plain = [chr(int(char2)) for char2 in aux]
        print("Plain: ", plain)
        return ''.join(plain)
    except TypeError as err:
        print(err)

if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    print("RSA Encryptor/Decrypter")
    print("====================================== ")

    p = int(input("Step 1: Enter a prime number: "))
    q = int(input("Step 2: Enter another prime number (Must not be similar to the first): "))

    print("Step 3: Generating your public / private key-pairs now . . .")

    public, private = generate_key_pair(p, q)

    print("Step 4: Your public key is ", public, " and your private key is ", private)

    message = input("Step 5: Enter a message to encrypt with your public key: ")
    encrypted_msg = encrypt(public, message)

    print("Step 6: Your encrypted message is: ", ''.join(map(lambda x: str(x), encrypted_msg)))
    print("Step 7: Decrypting message with private key ", private, " . . .")
    print("Step 8: Your message is: ", decrypt(private, encrypted_msg))

    print("====================================== ")
    print("Thank you for using RSA Algorithm!")
