# Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []
for i in range(1, 7):
    num = int(input("Enter your marks "))
    marks.append(num) 
    
marks.sort()
print(marks)
    