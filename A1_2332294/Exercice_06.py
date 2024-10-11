
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")


middle = int(len(s1)/2)

newFirstPart = list(s1[:middle])

newFirstPart.append(s2)

newString = "" .join(newFirstPart)

print(newString)
