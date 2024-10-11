"""
Question 7: Find all occurrences of “USA” in given string (uppercase and
lowercase).
Welcome to USA. usa awesome, isn't it?
"""

message = "Welcome to USA. usa awesome, isn't it?"
messagePrep = message.lower()
worldList = list(messagePrep.strip().split(" "))
indexOfUsa = []

for i in range(len(worldList)):
    if worldList[i].find("usa") != -1: ## o find se achar retorna 0 e se nao achar retorna -1
        indexOfUsa.append(i)
        

print(indexOfUsa)
