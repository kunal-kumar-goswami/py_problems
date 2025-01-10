#LCM of two numbers
a = int(input("Enter the 1st number :"))
num1 = a
b = int(input("Enter the 2nd number :"))
num2 = b

while num1 % num2 !=0:
    rem = num1 % num2
    num1 = num2
    num2 = rem

hcf = num2
lcm = (a * b) /hcf    
print(f"Your LCM is : {lcm}")
