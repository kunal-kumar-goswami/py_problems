import random
import string

def generate_strong_password():
    while True:
        password = input("Enter a password: ")
        
        if len(password) < 8:
            print("Password should be at least 8 characters long.")
            continue
        if not any(c.islower() for c in password):
            print("Password should include at least one lowercase letter.")
            continue
        if not any(c.isupper() for c in password):
            print("Password should include at least one uppercase letter.")
            continue
        if not any(c.isdigit() for c in password):
            print("Password should include at least one digit.")
            continue
        if not any(c in string.punctuation for c in password):
            print("Password should include at least one special character.")
            continue
        
        print("Your password is strong!")
        break

generate_strong_password()
