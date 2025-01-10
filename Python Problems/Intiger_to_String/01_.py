def convert(number):
    digits = '0123456789'
    result =''

    while number !=0:
        current_num = number % 10
        result = digits[current_num] + result
        number = number // 10 

    return result 
print(type(convert(23)))
     