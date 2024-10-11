
word = input("Enter the first word: ")

lower = []
upper = []

for char in word:
    if (char.islower()):
        lower.append(char)
    elif (char.isupper()):
        upper.append(char)

lower.sort()
upper.sort()

finalWord = "".join(lower)+"".join(upper)

print(finalWord)



        
