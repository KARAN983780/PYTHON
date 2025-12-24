
# Positional arguments
def info(name, age):
    print(name, age)

info("Karan", 22)

# Keyword arguments
info(age=22, name="Karan")

# Default argument
def country(name="India"):
    print(name)

country()
country("USA")

