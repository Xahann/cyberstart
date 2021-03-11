from Crypto.Cipher import AES
import base64
import os

BLOCK_SIZE = 32

PADDING = b"{"

# Encrypted text to decrypt
encrypted = b"uqX82PBZ8pi1fvt4GLHYgLs50ht8OQlrR1KHL2teppQ="

DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

with open("words.txt") as f:
    data = f.read().strip().split("\n")
    for secretstr in data:
        secret = secretstr.encode("utf-8")

        if secret[-1:] == "\n":
            print(
                "Error, new line character at the end of the string. This will not match!"
            )
        elif len(secret) >= 32:
            pass
            # print("Error, string too long. Must be less than 32 characters.")
        else:
            # create a cipher object using the secret
            cipher = AES.new(secret + (BLOCK_SIZE - len(secret) % BLOCK_SIZE) * PADDING)

            # decode the encoded string
            decoded = DecodeAES(cipher, encrypted)

            if decoded.startswith(b"FLAG:"):
                print(b"\n")
                print(b"Success: " + secret + b"\n")
                print(decoded + b"\n")
            else:
                pass
                # print("Wrong password")
