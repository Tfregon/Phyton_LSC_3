
print("Please enter 5 different numbers to se their average: ")

sum = 0
count = 0
num = []

for i in range(5):

    userNum = float(input("Enter the number: "))
    num.append(userNum)
    sum += userNum
    count += 1

resultAvg = sum/count

print(f"The average is: {resultAvg}")

access = int(input(" Enter a number to access an indice 0-4: "))

print(num[access])
