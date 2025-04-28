import time
lst = [i*i for i in range(1, 10) if(i*i % 2 == 0)]
print(lst)

for i in lst:
    print(i)
lst.sort(reverse=True)
print(lst)
lst.sort(reverse=False)
print(lst)
lst.remove(16)
print(lst)
lst.pop()
print(lst)
lst.append(64)
print(lst)
j = 0
lst2 = [1, 3, 4, 1, 4, 1, 9, 5, "Arpon Sarker", True, 234]
print(lst2)


#If user wants to make a list and remove values from the list whatever he wants
userList = []
def createList():
    n = int(input("Enter a number how many elements you want to add into the list: "))
    for i in range(0, n):
        num = input("Write whatever you want: ")
        userList.append(num)
    print("List according to your input: ", userList)
    
# If user wants to remvove any value from this list
def removeList():
    n = input("Enter a and element that you want to remove from the list: (Write 0 to stop removing) ")
    if n == 0:
        return 
    for i in userList:
        if i == n:
            userList.remove(n)
    print("The Final List: ", userList)

# Users are able to add unlimited numbers at a specific time (for 10 seconds)
def createListTime():
    startingTime = int(time.strftime('%S'))
    i = 0
    while i < 10:
        input("Enter elements to add")
        currentTime = int(time.strftime('%S'))
        totalTime = (currentTime - startingTime) % 60
        print(totalTime)
        print(startingTime)
        print(currentTime)
        i += 1
        
createListTime()
userList.insert(0, 18)
createList()
removeList()


