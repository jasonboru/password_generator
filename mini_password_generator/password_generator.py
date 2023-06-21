import string
import random


def generate_password(min_length, numbers=True, special_characters=True):
    """using the imported string class methods to get all letters, digits and special characters"""
    letters = string.ascii_letters
    # returns all letters:
    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

    digits = string.digits
    # returns all digits:
    # 0123456789

    special = string.punctuation
    # returns all letters:
    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    characters = letters  # the password options will always have letters

    if numbers:  # if numbers is True
        characters += digits # add all digit options to the characters object

    if special_characters:  # if special_charters is True
        characters += special  # add all special character options to the characters object

    pwd = ""  # password variable set to empty string
    meets_criteria = False  # starts False
    has_number = False  # starts False
    has_special = False  # starts False

    while not meets_criteria or len(pwd) < min_length:
        # while loop runs until meets_criteria is True or the password is no longer less than min length parameter

        new_char = random.choice(characters)  # variable new-char set to a random choice from the characters list
        pwd += new_char  # the password will build on itself each iteration through the while loop.

        if new_char in digits:  # check if this iteration of the new_char is in the digits list
            has_number = True
        elif new_char in special:
            has_special = True

        # This block ensures if nubmers or special_characters is passed as true when calling the method
        # the result will have at least 1 of those values.
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

    print(pwd)

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want your password to have numbers? [y/n]: ").lower() == "y"

has_special = input("Do you want your password to have special characters? [y/n]: ").lower() == "y"


pwd = generate_password(min_length,has_number,has_special)
print("Your minimum " + str(min_length) + " charcter password generated: " + pwd)



