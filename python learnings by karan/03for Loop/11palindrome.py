n = input("enter a number = ")

rev = ""

for i in range(len(n) - 1, -1, -1):
    rev = rev + n[i]

if n == rev:
    print("its a palindrome")
else:
    print("its not a palindrome")
