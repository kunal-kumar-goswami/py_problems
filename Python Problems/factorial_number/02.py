def fact(a):
    if a ==0:
        return 1
    else:
        return((a)* fact(a-1))
    
num = int(input("Enter a number "))    
result = fact(num)
print("the factorial of given munber",result)