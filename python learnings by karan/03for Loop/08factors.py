# factors and sum of al factors

n = int(input("enter the number ="))
s= 0

for i in range (1,n+1,1):
    
    if n%i==0:
        print(f"{i} is a  factor of {n}")
        
        s= s+i
 
print(f"sum of all the factors are {s}")