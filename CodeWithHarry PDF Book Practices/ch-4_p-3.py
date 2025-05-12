# Check that a tuple type cannot be changed in python.
tpl = (1, 2, 3, 4)
print("There will be an error after printing the line")
tpl.append(4)
print(tpl)