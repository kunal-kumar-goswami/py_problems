import random
import string

def generate_custom_strong_password(length=12):
    
    custom_symbols = "!@#$%^&*()_-+=<>?{}[]|"
    characters = string.ascii_letters + string.digits + custom_symbols

    
    while True:
        password = ''.join(random.choices(characters, k=length))
        
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in custom_symbols for c in password)):
            return password


password = generate_custom_strong_password()
print("Your strong password is:", password)
