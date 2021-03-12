from Crypto.Cipher import AES
import base64
import os

BLOCK_SIZE = 32

PADDING = b"{"

# Encrypted text to decrypt
# xpd4OA7GZYDfn4lTMJW/EEqgp26BlgjxsTonc1Elcgo=
encrypted = b"xpd4OA7GZYDfn4lTMJW/EEqgp26BlgjxsTonc1Elcgo="

DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

secret = b"password"

x = open("original_v2.txt", "wb")


def solve(secret):
    if secret[-1:] == "\n":
        print(
            "Error, new line character at the end of the string. This will not match!"
        )
    elif len(secret) >= 32:
        print("Error, string too long. Must be less than 32 characters.")
    else:
        # create a cipher object using the secret
        cipher = AES.new(secret + (BLOCK_SIZE - len(secret) % BLOCK_SIZE) * PADDING)

        # decode the encoded string
        decoded = DecodeAES(cipher, encrypted)
        # print(decoded.decode("utf-8", errors="ignore") + "\n")
        x.write(decoded + b"\n")


with open("words.txt") as f:
    lines = f.read().strip().split("\n")
    for line in lines:
        byte_stripped = line.strip().encode("utf-8")
        solve(byte_stripped)