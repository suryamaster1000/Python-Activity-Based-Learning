# Project 02: Password Policy Validation Engine
# Uses beginner-level Python concepts: strings, variables, conditions, loops, and lists.

MIN_LENGTH = 8

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
prohibited_substrings = ["password", "123456", "qwerty"]

number_of_passwords = int(input("How many passwords do you want to check? "))
while number_of_passwords <= 0:
    print("Please enter a number greater than zero.")
    number_of_passwords = int(input("How many passwords do you want to check? "))

for password_number in range(1, number_of_passwords + 1):
    print("\nPassword", password_number)
    password = input("Enter password: ")
    normalized_password = password.lower()

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    has_space = False

    for character in password:
        if character in uppercase_letters:
            has_uppercase = True
        elif character in lowercase_letters:
            has_lowercase = True
        elif character in digits:
            has_digit = True
        elif character == " ":
            has_space = True
        else:
            has_special = True

    has_three_repeated_characters = False
    previous_character = ""
    repeat_count = 0

    for character in password:
        if character == previous_character:
            repeat_count = repeat_count + 1
        else:
            previous_character = character
            repeat_count = 1

        if repeat_count >= 3:
            has_three_repeated_characters = True

    has_prohibited_substring = False
    for prohibited_text in prohibited_substrings:
        if prohibited_text in normalized_password:
            has_prohibited_substring = True

    password_is_valid = True
    print("Checks:")

    if len(password) < MIN_LENGTH:
        print("FAIL: Password must contain at least", MIN_LENGTH, "characters.")
        password_is_valid = False
    else:
        print("PASS: Minimum length")

    if has_uppercase == False:
        print("FAIL: Add at least one uppercase letter (A-Z).")
        password_is_valid = False
    else:
        print("PASS: Uppercase letter")

    if has_lowercase == False:
        print("FAIL: Add at least one lowercase letter (a-z).")
        password_is_valid = False
    else:
        print("PASS: Lowercase letter")

    if has_digit == False:
        print("FAIL: Add at least one digit (0-9).")
        password_is_valid = False
    else:
        print("PASS: Digit")

    if has_special == False:
        print("FAIL: Add at least one special character, such as ! or #.")
        password_is_valid = False
    else:
        print("PASS: Special character")

    if has_space:
        print("FAIL: Spaces are not allowed.")
        password_is_valid = False
    else:
        print("PASS: No spaces")

    if has_three_repeated_characters:
        print("FAIL: Do not use the same character three times in a row.")
        password_is_valid = False
    else:
        print("PASS: No character repeated three times in a row")

    if has_prohibited_substring:
        print("FAIL: Do not include 'password', '123456', or 'qwerty'.")
        password_is_valid = False
    else:
        print("PASS: No prohibited substring")

    if password_is_valid:
        print("RESULT: Password meets this project's policy.")
    else:
        print("RESULT: Password does not meet this project's policy.")

print("\nPassword checking completed.")
