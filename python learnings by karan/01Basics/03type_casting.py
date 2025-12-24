# TYPE CASTING IN PYTHON
# Changing one data type into another

# -----------------------------
# String to Integer
# -----------------------------
a = "10"
b = int(a)          # convert string to int
print(b)
print(type(b))

# -----------------------------
# String to Float
# -----------------------------
c = "10.5"
d = float(c)        # convert string to float
print(d)
print(type(d))

# -----------------------------
# Integer to String
# -----------------------------
e = 25
f = str(e)          # convert int to string
print(f)
print(type(f))

# -----------------------------
# Float to Integer
# -----------------------------
g = 10.9
h = int(g)          # decimal part removed
print(h)
print(type(h))

# -----------------------------
# Integer to Float
# -----------------------------
i = 5
j = float(i)        # convert int to float
print(j)
print(type(j))

# -----------------------------
# Input always gives string
# -----------------------------
age = input("Enter your age: ")
print(age)
print(type(age))    # string

# -----------------------------
# Input with type casting
# -----------------------------
age2 = int(input("Enter your age again: "))
print(age2)
print(type(age2))   # int

# -----------------------------
# Adding numbers from input
# -----------------------------
x = int(input("Enter x: "))
y = int(input("Enter y: "))
print(x + y)

# -----------------------------
# Wrong type casting (will cause error)
# -----------------------------
# name = "karan"
# num = int(name)   # ❌ ValueError

# Implicit done by automaticly by python 

# Explicit