# Let's make a fibonacchi series using Python and recursion

def fibo(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    else:
        return fibo(number - 1) + fibo(number - 2)
    

number = int(input("Enter a number: "))
print(fibo(number))