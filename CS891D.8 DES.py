# Fiestel Algorithm:
#1. Message = ABCDEF. Divide into two: L = ABC, R = DEF.
#2. Say, Ln is output's left half after round n and Rn is output's right half after round n.
#3. L1 = R. R1 = L xor F(R,K1) [F is any function, K1 is key for round 1].
#3. L2 = R1. R2 = L1 xor F(R1,K2)
#3. L3 = R2. R3 = L2 xor F(R2,K3)
#4. Ln = Rm, Rn = Lm xor F(Rm,Kn) [m = n-1].
#5. After n rounds, say Ln = UVW, Rn = XYZ.
#6. Cipher: RnLn = XYZUVW (Ln and Rn are swapped and joined).
#7. For decryption, feed cipher XYZUVW, follow exact same algorithm, except, use keys K1, K2... in REVERSE order.

# DES Algorithm (Data Encryption Standard):
#0. Block cipher.
#1. Uses the Fiestel structure, with n = 16 (16 rounds) & a different key (size 56 bits) each round.
#2. Can encrypt 64 bits at once. So, the plaintext is broken into blocks of 64 bits.
#3. Key generation (Round key generation):
#3. (1) The original key is 64 bits; say key = 0000000 00000001 00000010... 00001000.
#3. (2) Parity Drop: 8th or rightmost bit of each bytes (0000000 is 1st byte, 00000001 is 2nd byte) is discarded to make the key. So key = 64 - (8*1) = 56 bits.
#3. (3) Divide the 56bit key into two 28bit keys; say KL and KR.
#3. (4) For round 1, left shift KL and KR by 1, to generate KL1 and KR1, and concatenate KL1KR1 as key.
#3. (4) For round 2, left shift KL1 and KR1 by 1 again, to generate KL2 and KR2, and concatenate KL2KR2 as key and so on.
#3. (4) For round 1, 2, 9 and 16, shift by 1 place. For other rounds, shift by 2 place.
#3. (4) Example: In round 2, left shift KL2 & KR2 by 2 bits to generate KL3 & KR3, concatenate KL3KR3 to form key for round 3. Jumble the key again.
#3. (5) Pass this 56bit key into a compression permutation box or Pbox which will discard random 8 bits and jumble it to make a different 48bit subkey for each round.
#4. Now we move on to plaintext. First, 64bit plaintext is jumbled according to some permutation table, called Initial Permutation.
#5. Divide the jumbled plaintext into L and R, like Fiestel. Jumble the 56bit key.
#6. Follow Fiestel cipher's steps now:
#6. We obtained L and R in Step 5. We got K1 = KL1KR1, K2 = KL2KR2 etc in Step 3.
#7. We feed them to our function F(R,K) as in Fiestel algorithm. Inside this F(), we have one expansion permutation, one substitution S box, and one straight permutation P box.
#8. (1) Our plaintext L, R = 32 bits long but K1, K2 etc are 48 bits long. So first we do expansion permutation. The 32 bit block is broken into 8 4bit blocks and changed to 8 6bit blocks
#8. (1) So each 4bit block is fed with 2 extra bits like: {1 2 3 4} => {32 1 2 3 4 5}, 32nd bit of L and R is pushed in first block first position and 5th bit is pushed to first block last position.
#8. (1) [{32 1 2 3 4 5} {4 5 6 7 8 9} {8 9 10 11 12 13} {12 13 14 15 16 17} {16 17 18 19 20 21} {20 21 22 23 24 25} {24 25 26 27 28 29} {28 29 30 31 32 1}]
#8. (2) Then follows our S-box. We get a final 48 bit from step 8 (1), but we need a 32 bit value. The S-box takes the 48 bit value and makes it 32 bit.
#8. (2) In the Sbox, we have a 4 row 16 column table, each containing a 4bit value. The 48bit input is divided into 8 6bit inputs.
#8. (3) The first bit and last bit of the 6bit input gives us the row number (00, 01, 10 or 11 i.e. 4 values) and the middle 4 bits gives us column number (0000, 0001... 1111 i.e. 16 values)
#8. (4) Then, Sbox[row][column] value which is 4bit is substituted in place of the 6bit value, giving us 8 such 4bit values i.e. 32 bits.
#9. Then it passes through a final plain Permutation P box where the values are jumbled and it gives us the output of F(R,K).
#10. After 16 rounds, we perform a final permutation. Like initial permutation this is also based on some predetermined permutation table.


#Source: https://pypi.org/project/des/

from des import DesKey
key0 = DesKey(b"some key")                  #for DES
key1 = DesKey(b"a key for TRIPLE")          #for 3DES, same as "a key for TRIPLEa key fo"
key2 = DesKey(b"a 24-byte key for TRIPLE")  #for 3DES
key3 = DesKey(b"1234567812345678REAL_KEY")  #for DES, same as "REAL_KEY"

key0.encrypt(b"any long message")  # -> b"\x14\xfa\xc2 '\x00{\xa9\xdc;\x9dq\xcbr\x87Q"

key0.encrypt(b"abc", padding=True)  # -> b"%\xd1KU\x8b_A\xa6"
key0.decrypt(b"%\xd1KU\x8b_A\xa6", padding=True)  # -> b"abc"
