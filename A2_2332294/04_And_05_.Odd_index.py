listOne = [3,6,12,15,18,21]
listTwo = [4,8,12,16,20,24,28]

thirdList = []

for odd in listOne:
    if(odd %2 == 1):
        thirdList.append(odd)
for even in listTwo:
    if(even %2 == 0):
        thirdList.append(even)

print(thirdList)

"""

Exercice 05


"""

listEx = [54, 44, 27, 79, 91, 41]


remove = listEx.pop(4)

listEx.insert(1, remove)
listEx.append(remove)

print(listEx)
