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
    # Try the 8th byte
    key = key_incomplete + bytes([i])
    
    # Decrypt the full flag using the candidate key
    flag = bytes(x ^ y for x, y in zip(ct, cycle(key)))

    # Check if the decrypted flag looks correct (starts with "uiuctf{" and ends with "}")
    if flag.startswith(b"uiuctf{") and flag.endswith(b"}"):
        print(f"Found key: {key}")
        print(f"Flag: {flag.decode()}")
        break
