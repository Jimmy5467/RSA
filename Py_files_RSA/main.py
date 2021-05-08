import dec
import enc
import key_generate
import sys

"""def encrypt(e, N, msg):
    cipher = ""

    for c in msg:
        m = ord(c)
        cipher += str(pow(m, e, N)) + " "

    return cipher
"""
"""def decrypt(d, N, cipher):
    msg = ""

    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, N))

    return msg"""


def main():
    keysize = 32

    p, q, e, d, N = key_generate.generateKeys(keysize)
    msg = "%s" % (sys.argv[1])
    en = enc.encrypt(e, N, msg)
    de = dec.decrypt(d, N, en)

    print(f"p: {p}")
    print(f"q: {q}")
    print(f"Message: {msg}")
    print(f"e: {e}")
    print(f"d: {d}")
    print(f"N: {N}")
    print(f"enc: {en}")
    print(f"dec: {de}")


main()
