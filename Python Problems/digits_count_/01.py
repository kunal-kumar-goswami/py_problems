a= int(input("Enter your number : "))
count = 0
while(a > 0):
    a = a // 10
    count = count +1
print(f"Number of digits is : {count}")


