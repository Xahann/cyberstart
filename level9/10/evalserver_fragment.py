print("Welcome to Maths_Server 1.0\n")
flag = "supersecretmessage"

try:
    print("Enter the first number, so I can EVALuate it:\n")
    firstNum = eval(input())
    firstNum = firstNum + firstNum + ord(flag[4]) + ord(flag[8]) + ord(flag[5])
    print(firstNum)
    print("Enter the second number, so I can EVALuate it:\n")
    secondNum = eval(input())
    print(secondNum)
    if secondNum == firstNum:
        print("The flag is: " + flag + "\n")
        firstNum = 0
        secondNum = 0
except:
    pass

clientsock.close()
