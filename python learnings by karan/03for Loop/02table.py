n = int(input("Enter the number whose table you want = "))
a = 1
for i in range (n,(n*10)+1,n):
    print(f"{n}x{a}={i}")
    a = a+1
