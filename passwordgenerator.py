import random
import time

def again(): # This function is to ask the user if they want to generate another password
    answer = input("Would you like to generate another password? (y/n): ")
    if answer in ("y", "Y", "yes", "Yes", "YES"):
        generator()
    else:
        time.sleep(1)
        print("Goodbye!")
        time.sleep(1)


def generator():
    length = int(input("Enter a password length: "))
    special = int(input("Enter the number of special characters: "))
    numbers = int(input("Enter the number of numbers: "))

    password = ""

    for i in range(length - special - numbers):
        password += chr(random.randint(97, 122)) # Lowercase letters

    for i in range(special):
        password += chr(random.randint(33, 47)) # Special characters
        while password[i + (length - special - numbers)] in (")", "(", '"', "'"): # It checks if a character is a parenthesis or a quotation mark and removes it
            password = password[:-1]
            password += chr(random.randint(33, 47))
        else:
            continue
                
                

    for i in range(numbers):
        password += chr(random.randint(48, 57)) # Numbers

    random_password = list(password) 
    random.shuffle(random_password) # Shuffles the password
    print("".join(random_password))

    again()

generator()
