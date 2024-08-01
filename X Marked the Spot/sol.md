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

# Solution code 
```py
from itertools import cycle

with open("ct", "rb") as ct_file:
    ct = ct_file.read()

# to solve this challenge, calculate the key (8 bytes in size)
# To calculate for the key we know:
# 1. the known plaintext up to the first 7 bytes
# 2. the ciphertext

# As such, we can calculate the the first 7 bytes of the key (incomplete) by xor-ing the plaintext and ciphertext
# To obtain the complete key, just brute force and try 256 different characters, 
# for each of the 256 chars, 
# concat the last byte to the imcomplete key, 
# xor the key with the ciphertext to get back the full plaintext

# Known partial plaintext 
plaintext_known = b"uiuctf{"

# 
ct_incomplete = ct[:7]

key_incomplete = bytes(x ^ y for x, y in zip(plaintext_known, ct_incomplete))

# Brute-force the 8th byte of the key
for i in range(256):
    # Concat the last byte
    key = key_incomplete + bytes([i])
    
    # Decrypt (XOR)
    flag = bytes(x ^ y for x, y in zip(ct, cycle(key)))

    # Check for flag correctness
    if flag.startswith(b"uiuctf{") and flag.endswith(b"}"):
        print(f"Found key: {key}")
        print(f"Flag: {flag.decode()}")
        break
```

# Flag
uiuctf{n0t_ju5t_th3_st4rt_but_4l50_th3_3nd!!!!!}