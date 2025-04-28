import time

now = int(time.strftime('%S'))
print(now)

def game():
    pass
while True:
    now1 = int(time.strftime('%S'))
    n = input("Write any random number: ")
    theTime = (now1 - now + 1) % 60
    print(theTime)
    if(theTime > 4):
        print(f"Your time is over! You used the time in total: {theTime} seconds")
        exit()
    
    