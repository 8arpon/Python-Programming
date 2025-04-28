import time

myTime = time.strftime('%H:%M:%S')
print(f"The time right now is: {myTime}")
myTime = int(time.strftime('%H'))

if myTime <= 11 and myTime > 6:
    print("Good Morning, Sir")
elif myTime < 16 and myTime > 12:
    print("Good Noon, Sir")
elif myTime <= 18 and myTime > 16:
    print("Good Evening, Sir")
else:
    print("Good Night, Sir")
