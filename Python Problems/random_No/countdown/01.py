import time

your_time = int(input("enter the time in second: "))


for x in range(your_time,-1,-1):
    hours = x // 3600
    minutes = int(x % 3600) // 60
    second = x % 60
    print(f"{hours:02}:{minutes:02}:{second:02}")
    time.sleep(1)

print("TIME'S UP! ")    