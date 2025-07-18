import time

sec = int(input("Enter time in seconds: "))
for i in range(sec, 0, -1):
    print(i, end="\r")
    time.sleep(1)
print("Time's up!")
