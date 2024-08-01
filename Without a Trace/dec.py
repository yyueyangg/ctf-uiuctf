"""
u1 = uiuct
u2 =f{tr4
u3 = c1ng_
u4 = &&_mu
u5 = lt5!}

flag = uiuctf{tr4c1ng_&&_mult5!}

----------------------------------------------------------------
"""

import numpy as np
from Crypto.Util.number import bytes_to_long, long_to_bytes


def fun(M):
    f = [bytes_to_long(bytes("uiuct f{man  what ever} asder"[5*i:5*(i+1)], 'utf-8')) for i in range(5)]
    F = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    for i in range(5):
        F[i][i] = f[i]

    R = np.matmul(F, M)
    print(f)
    return np.trace(R)


def main():
    print("[WAT] Welcome")
    M = [
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
    ]

    res = fun(M)
    print(f"[WAT] Have fun: {res}")

if __name__ == "__main__":
    main()