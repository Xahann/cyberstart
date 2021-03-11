import itertools
import base64
with open("encrypted.txt") as f:
    lines = f.read().strip().split("\n")
    possible = filter(lambda x:x[-1] == "=", list("".join(x) for x in itertools.permutations(lines)))
    for x in possible:
        print(base64.b64decode(x).decode('utf-8',errors='ignore'))
