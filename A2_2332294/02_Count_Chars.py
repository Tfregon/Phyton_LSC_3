
word = input("Enter the word to see how many chars number or symbols: ")

lower = []
upper = []
digit = []
symbol = []
countLow = 0
countUpp = 0
countNum = 0
countSym = 0
for char in word:
    if (char.islower()):
        lower.append(char)
        countLow += 1
    elif (char.isupper()):
        upper.append(char)
        countUpp += 1
    elif (char.isdigit()):
        countNum += 1
    else:
        symbol.append(char)
        countSym += 1

lower.sort()
upper.sort()
digit.sort()
symbol.sort()

finalWord = "".join(lower)+"".join(upper)+"".join(digit)+"".join(symbol)
print(f"The final word sorted is: {finalWord} and the number of lower case is {countLow}, upper is: {countUpp}, digit is: {countNum}, Especial symbols: {countSym}")


