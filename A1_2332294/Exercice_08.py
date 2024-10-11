"""
Question 8: Given a two list. Create a third list by picking an odd-index element from the
first list and even index elements from second.
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
"""

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

newListB = []
listThree = []


for i in range(len(listOne)):
    if i%2 == 1:
        listThree.append(listOne[i])
for i in range(len(listTwo)):
    if i%2 == 0:
        newListB.append(listTwo[i])

listThree.extend(newListB) ## com o append eu colocaria a segunda lista dentro de um so elemento

print(listThree)
