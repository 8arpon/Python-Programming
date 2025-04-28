# Write a program to count the number of zeros in the following tuple:
a = [7, 0, 8, 0, 0, 9]
j = 0
for i in a:
    if(i == 0):
        j = j + 1
print(j)
a.remove(8)
print(a)