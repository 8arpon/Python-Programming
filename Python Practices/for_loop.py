yourLoop = input("Write what do you want to print: ")
n = int(input("Write how may times you wanna get: "))

# to print the yourLoop several times you want to get
for i in range(1, n + 1):
    print(f"{i}: {n}")

# to find the odd values
for i in range(0, n + 1, 2):
    print(i + 1)
    
# to find the even values
for i in range(2, n + 1, 2):
    print(i)


