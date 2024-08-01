from itertools import cycle

# Read the ciphertext from the file
with open("ct", "rb") as ct_file:
    ct = ct_file.read()

# Known partial plaintext (first 7 bytes of the flag)
known_plaintext = b"uiuctf{"

# Extract the part of the ciphertext that corresponds to the known plaintext
partial_ct = ct[:len(known_plaintext)]

# Derive the first 7 bytes of the key by XORing the known plaintext with the corresponding part of the ciphertext
partial_key = bytes(x ^ y for x, y in zip(known_plaintext, partial_ct))

# Brute-force the 8th byte of the key
for i in range(256):
    # Try the 8th byte
    key = partial_key + bytes([i])
    
    # Decrypt the full flag using the candidate key
    flag = bytes(x ^ y for x, y in zip(ct, cycle(key)))

    # Check if the decrypted flag looks correct (starts with "uiuctf{" and ends with "}")
    if flag.startswith(b"uiuctf{") and flag.endswith(b"}"):
        print(f"Found key: {key}")
        print(f"Flag: {flag.decode()}")
        break
