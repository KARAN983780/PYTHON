n = int(input("enter a number -"))
b = 0
if n>=0:
    for i in range(n,-1,-1):
        b = b+i
    print(b)
elif n<0:
    for i in range(-1,n-1,-1):
        b = b+i
    print(b)
else:
    print("nothing")