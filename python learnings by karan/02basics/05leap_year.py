year = (int(input("enter the year = ")))
if year %400==0 and year %100== 0:
    print(f"{year} its a leap year ")

elif  year %100!= 0 and year%4==0:
    print(f"{year} its a leap year")
else :
    print(f"{year} its a normal year")