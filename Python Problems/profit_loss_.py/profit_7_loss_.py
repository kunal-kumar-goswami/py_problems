cp = float(input("Enter your cost price: "))
sp = float(input("Enter your selling price: "))

if cp > sp :
    amount = cp - sp
    print(f"loss = {amount}")
else:
    amount = sp - cp 
    print(f"profit = {amount}")   
