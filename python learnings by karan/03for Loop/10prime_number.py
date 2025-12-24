# # check the number is prime or not
# n = int(input("enter the number you want to check = "))
# for i in range(2,n,1):
#     if n%i==0:
#         print(f"this {n} not a prime number")
#         break
# else:
#     print(f"this {n} a prime number ")

    #2nd method
n = int(input("enter ur n = "))
count=0
for i in range(1,n+1,1):
    if n%i==0:
        count=count+1
if count==2:
    print("its a prime number")
else :
    print("its not a prime number")
        
