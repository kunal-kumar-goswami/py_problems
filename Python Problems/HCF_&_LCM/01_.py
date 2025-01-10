#HCf of two numbers 
a = int(input("Enter your 1st number : "))
b = int(input("Enter your 2nd number : "))

while a % b != 0 :
    rem = a % b           
    a = b 
    b = rem

print(f"Your HCF is = {b}")