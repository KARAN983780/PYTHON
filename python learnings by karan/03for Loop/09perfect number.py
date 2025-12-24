#check if its a perfect number or not 
# (sum of all factors equals to the user input number)
# check if it is a perfect number or not

#facter
n = int(input("enter the number = "))
s=0
for i in range(1,n,1):
    if n%i==0:
      s=s+i
print(s)
if s == n:
    print("this is a perfect number ")
else:
    print("this is not a perfect number")
