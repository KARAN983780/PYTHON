age = int(input("enter the age = "))
gender = input("enter the gender (m for male an f for female) = ")
experience = int(input("enter the experience year ="))
if age <18:
    print("not eligible ")
elif age>=18:
    if gender =="f":
        if experience >= 2:
            print("Senior Female Candidate")
        else:
            print("Junior Female Candidate")
    elif gender == "m":
        if experience >= 5:
            print("Senior Male Candidate")
        else:
            print("Junior Male Candidate")
    else:
        print("invalid information")