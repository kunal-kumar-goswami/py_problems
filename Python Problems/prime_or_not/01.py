num = int(input("Enter a number "))

if num ==1:
    print("It is prime number ")
if num>1:
    for i in range(2,num):
        if num% i==0:
         print("IT is not prime ")
         break
    else:
         print("prime number")