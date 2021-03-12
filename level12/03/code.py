from Crypto.Cipher import AES
import base64
import os

BLOCK_SIZE = 32

PADDING = b"{"

# Encrypted text to decrypt
encrypted = b"xpd4OA7GZYDfn4lTMJW/EEqgp26BlgjxsTonc1Elcgo="

DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

with open("words.txt") as f:
    lines = f.read().strip().split("\n")
    for secret in lines:

        secrets = [
            secret.encode("utf-8"),
            secret.lower().encode("utf-8"),
            secret.upper().encode("utf-8"),
        ]
        for asecret in secrets:
            if asecret[-1:] == "\n":
                print(
                    "Error, new line character at the end of the string. This will not match!"
                )
            elif len(asecret) >= 32:
                pass
                # print("Error, string too long. Must be less than 32 characters.")
            else:
                # create a cipher object using the asecret
                cipher = AES.new(
                    asecret + (BLOCK_SIZE - len(asecret) % BLOCK_SIZE) * PADDING
                )

                # decode the encoded string
                decoded = DecodeAES(cipher, encrypted)
                print(decoded.decode("utf-8", errors="ignore"))
