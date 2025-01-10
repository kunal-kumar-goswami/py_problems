num = int(input("Enter a number: "))

sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    cube = digit **3
    sum = sum + cube
    temp //= 10

if num == sum:
    print(num,"is an Aemstrong number")    
else:
    print(num, "is not an Armstrong number")    
