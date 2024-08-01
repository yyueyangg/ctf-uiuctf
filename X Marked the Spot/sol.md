# Challenge Details 

Category: Crypto

Title: X Marked the Spot

Points: 93

Solves: 531

# Challenge Summary
The challenge hides the flag by:
1. using a key (8 bytes), 
2. xor the key with the plaintext (48 bytes)
3. note that cycle() is used meaning, for each 8 bytes of the plaintext, xor the plaintext with the key, repeat this for all 6 units of the 8 bytes of plaintext

# Solution
to solve this challenge, calculate the key (8 bytes in size)

To calculate for the key we know:
1. the known plaintext up to the first 7 bytes 'uiuctf{'
2. the ciphertext

As such, we can calculate the the first 7 bytes of the key (incomplete) by xor-ing the plaintext and ciphertext

To obtain the complete key, just brute force and try 256 different characters, 
for each of the 256 chars:
1. concat the last byte to the imcomplete key, 
2. xor the key with the ciphertext to get back the full plaintext

