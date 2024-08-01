# Challenge Details 

Category: Crypto
Title: Without a Trace
Points: 246
Solves: 298

# Challenge Summary
The challenge is asking us to input 5 non-zero numbers into a 5x5 M matrix, where the inputs will occupy the matrix diagonally.

To hide the flag, the challenge split the flag into 5 parts and converted the flag to its long representation, then putting them in a matrix 5x5 matrix where the flag parts will occupy the matrix diagonally. This is the F matrix.

Then, the challenge multiplies M matrix and F matrix, which will eventually give us a number (res = m1*f1 + m2*f2.... + m5*f5)


# Solution 
To capture the flag, the player can input 5 1(s) when prompted by the server. This would give a res1 of (f1+f2+..+f5) which would give us the sum of the flag parts (represented in long numbers)

To get each individual flag part, for example, to get f1, input 2 for u1, then 1(s) for the 4 other inputs. 

u1 = 2
u2 = 1
u3 = 1
u4 = 1
u5 = 1

This would give a res2 of (2*f1 + f2 + f3 + f4 + f5)

Then taking res2 - res1, the player has successfully calculated f1.

Repeat this to get f2, f3, f4 and f5. 

Convert each flag part from their long representation back to bytes, concat them together, and you have successfully captured the flag.

# Solution code 
```py
from Crypto.Util.number import long_to_bytes

input_one_for_all = 2000128101369
input_two_for_u1 = 2504408575853
input_two_for_u2 = 2440285994541
input_two_for_u3 = 2426159182680
input_two_for_u4 = 2163980646766
input_two_for_u5 = 2465934208374

f1 = 2504408575853 - 2000128101369
f2 = 2440285994541 - 2000128101369
f3 = 2426159182680 - 2000128101369
f4 = 2163980646766 - 2000128101369
f5 = 2465934208374 - 2000128101369

print(long_to_bytes(f1))
print(long_to_bytes(f2))
print(long_to_bytes(f3))
print(long_to_bytes(f4))
print(long_to_bytes(f5))
```
# Flag 
uiuctf{tr4c1ng_&&_mult5!}