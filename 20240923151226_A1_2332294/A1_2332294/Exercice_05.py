
sizeOfList = int(input("How many objects inside of list: "))

intList = []

for i in range(sizeOfList):
    num = int(input("Enter a list of numbers: "))
    intList.append(num)
    
if(intList[0] == intList[-1]):
    ans = True
   
else:

    ans = False

print(ans)
