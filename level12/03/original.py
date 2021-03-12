from Crypto.Cipher import AES
import base64
import os

BLOCK_SIZE = 32

PADDING = "{"

# Encrypted text to decrypt
# xpd4OA7GZYDfn4lTMJW/EEqgp26BlgjxsTonc1Elcgo=
encrypted = "xpd4OA7GZYDfn4lTMJW/EEqgp26BlgjxsTonc1Elcgo="

DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

secret = "password"

if secret[-1:] == "\n":
    print "Error, new line character at the end of the string. This will not match!"
elif len(secret) >= 32:
    print "Error, string too long. Must be less than 32 characters."
else:
    # create a cipher object using the secret
    cipher = AES.new(secret + (BLOCK_SIZE - len(secret) % BLOCK_SIZE) * PADDING)

    # decode the encoded string
    decoded = DecodeAES(cipher, encrypted)
    print decoded + "\n"
