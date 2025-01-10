p = int(input("Enter the principal : "))
r = int(input("Enter the rate of intrest : "))
t = int(input("Enter time period in years : "))

a = p *(1 + r / 100)**t
print(f"Your amount is : {a}")

ci = a - p
print(f"Your Compound Intrest is : {ci}")