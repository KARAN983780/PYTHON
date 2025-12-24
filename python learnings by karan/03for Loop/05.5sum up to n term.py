# #sum up to n term
# n = int(input("enter a number here ="))
# b = 0
# for i in range(n,0,-1):
#     b = b+i
#     print(f"the sum is {b}")

    # now this is very commen and big mistake in line 6 , 
    #     print is inside the loop thats why its printing 
    #     again and again
    
#sum up to n term
n = int(input("enter a number here ="))
b = 0
for i in range(n,0,-1):
    b = b+i
print(f"the sum is {b}")