def squared_number(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers    


numbers = [2,4,6,8]
squared_numbers = squared_number(numbers)
print(squared_numbers)
