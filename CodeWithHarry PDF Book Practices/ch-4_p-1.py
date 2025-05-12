# Write a program to store seven fruits in a list entered by the user.

fruits = []
for i in range(1, 8):
    fruits.append(input(f"Enter fruit name {i}: "))
print(fruits)   