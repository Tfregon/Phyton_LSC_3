s1 = input("Enter the first word: ").lower()
s2 = input("Enter the chars to check if is balanced in the word: ").lower()

tot = len(s2)
count = 0;
ans = False;

for char in s2:
    for charInWord in s1:
        if(char == charInWord):
            count += 1
if(count == tot):
    ans = True

        
print(f"{s1} and {s2} are balanced {ans}")

