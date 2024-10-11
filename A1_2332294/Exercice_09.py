"""
Question 9: Given an input list removes the element at index 4 and add it to the 2nd
position and also, at the end of the list
List = [54, 44, 27, 79, 91, 41]
"""

listOfNum = [54, 44, 27, 79, 91, 41]

removeFromList = listOfNum.pop(4)

listOfNum.insert(2, removeFromList)

listOfNum.append(removeFromList)

print(listOfNum)
