n = int(input("Enter a number = "))
b = 0

if n > 0:
    for i in range(1, n+1):
        b += i
elif n < 0:
    for i in range(-1, n-1, -1):
        b += i
else:
    b = 0

print("The sum is", b)
