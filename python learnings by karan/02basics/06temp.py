temp = int(input("enter the temperature = "))
if temp<0:
    print("temperature is very cold")
elif temp>=0 and temp<=10:
    print("temperature is cold")
elif temp>=11 and temp<=20:
    print("temperature is pleasant ")
elif temp>=21 and temp<=30:
    print("temperature is humid")
else:
    print("temp is very hot ")
