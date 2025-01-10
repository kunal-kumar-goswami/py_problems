num1 = (int(input("Enter a number 1 ")))
num2 = (int(input("Enter a number 2 ")))
num3 = (int(input("Enter a number 3 ")))

if num1>num2 and num1 >num3:
    print(num1 ,"greater than both num2 amd num3 ")
elif num2>num1 and num2>num3:
    print(num2, "geater than  both num1 and num3 ")
else:
    print(num3, "greater than both num1 and num2")