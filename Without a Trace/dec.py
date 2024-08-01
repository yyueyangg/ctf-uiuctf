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