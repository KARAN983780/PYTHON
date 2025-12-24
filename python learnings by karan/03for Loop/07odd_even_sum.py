# even and odd sum
# even and odd sum
n = int(input("Enter the number = "))
b = 0

if n % 2 == 0:
    for i in range(n, 0, -2):
        b += i
    print(f"The sum of even numbers is {b}")
else:
    for i in range(n, 0, -2):
        b += i
    print(f"The sum of odd numbers is {b}")
