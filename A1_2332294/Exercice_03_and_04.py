"""
Given a string of odd length greater 7, return a string made of the middle three
chars of a given String
Question 4: Given a string and an int n, remove characters from string starting from zero
upto n and return a new string
"""
##message = input(print("Input the word: "))
##
##sizeOfMessage = len(message)
##
##if(sizeOfMessage > 7 and sizeOfMessage%2 == 1):
##
##    startingPoint = int(sizeOfMessage/2 - 1)
##    lastPoint = int(startingPoint + 3)
##    
##    newString = message[startingPoint:lastPoint]
##    print(newString)

"""
-------------------------------------------------------------------------------------------
"""


newMessage = input(print("Say something: "))
lastIndex = int(input(print("Please insert the last letter that you want to slice: ")))

newString_2 = newMessage[:lastIndex]

print(newString_2)
