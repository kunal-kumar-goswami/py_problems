p = int(input("Enter the principal : "))
r = int(input("Enter the rate of intrest :"))
t = int(input("Enter time period in years :"))
 
si = (p * r * t) /100

print(f"Your Simple Intrest is : {si}")

a = p + si
print(f"Your Amount is : {a}")