name = "karan bisht"
       #^^^^^^^^^^^
       #0123456789......
print(name[0:5:1]) # this is string slicing
print(name[0:]) 

print(name.upper())     # KARAN BISHT
print(name.lower())     # karan bisht
print(name.find("bisht"))  # 6

print(name.replace("karan", "shibu") ) # shibu bisht

print(name.split())   # ['karan', 'bisht']
print(len(name))  # 11
print(name.title() ) # Karan Bisht

# Formatting (very important)
print(f"my name is {name}")

