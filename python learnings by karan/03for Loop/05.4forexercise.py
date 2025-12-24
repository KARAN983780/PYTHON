#take a number as a input and print its table 
a = int(input("enter a number = "))
b = 1
for i in range(a,a*10+1,a):
    print(f"{a}x{b}={i}")
    b = b+1