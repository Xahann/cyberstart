message = "GANG MAY KNOW YOUR IDENTITY ABORT ABORT MEET AT SAFE HOUSE B"

mapping = {
    "A": "F",
    "B": "G",
    "C": "H",
    "D": "I",
    "E": "J",
    "F": "K",
    "G": "L",
    "H": "M",
    "I": "N",
    "J": "O",
    "K": "P",
    "L": "Q",
    "M": "R",
    "N": "S",
    "O": "T",
    "P": "U",
    "Q": "V",
    "R": "W",
    "S": "X",
    "T": "Y",
    "U": "Z",
    "V": "A",
    "W": "B",
    "X": "C",
    "Y": "D",
    "Z": "E",
    " ": " ",
}
final = ""
for letter in message:
    final += mapping[letter]
print(final)