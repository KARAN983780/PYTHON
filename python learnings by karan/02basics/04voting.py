name = input("enter ur name = ")
age = int(input("enter ur age = "))
if age >= 18:
    print(f"{name} yoy are eligible for voting ")
else:
    print(f"{name } u can vote after {18-age} years")