# Algorithm and Pseudocode — Password Policy Validation Engine

## Algorithm

1. Start.
2. Set the minimum length to 8 and define uppercase letters, lowercase letters, digits, and the prohibited substring list.
3. Input the number of passwords. If it is not positive, keep asking until it is positive.
4. Repeat for each password:
   - Input the password and create a lowercase copy.
   - Scan every character and record whether uppercase, lowercase, digit, special character, or space appears.
   - Scan every character to detect three or more identical consecutive characters.
   - Search for the prohibited substrings `password`, `123456`, and `qwerty` in the lowercase copy.
   - Start with the result marked valid.
   - Check every rule. Print a PASS message if it passes; otherwise print a specific failure message and mark the password invalid.
   - Print the final result for the password.
5. Display that checking is complete.
6. Stop.

## Pseudocode

```text
BEGIN
    MIN_LENGTH <- 8
    UPPERCASE <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LOWERCASE <- "abcdefghijklmnopqrstuvwxyz"
    DIGITS <- "0123456789"
    PROHIBITED <- ["password", "123456", "qwerty"]

    INPUT number_of_passwords
    WHILE number_of_passwords <= 0
        DISPLAY "Please enter a number greater than zero"
        INPUT number_of_passwords
    END WHILE

    FOR password_number FROM 1 TO number_of_passwords
        INPUT password
        normalized_password <- lowercase(password)
        set has_uppercase, has_lowercase, has_digit, has_special, has_space to FALSE

        FOR each character in password
            IF character is in UPPERCASE: has_uppercase <- TRUE
            ELSE IF character is in LOWERCASE: has_lowercase <- TRUE
            ELSE IF character is in DIGITS: has_digit <- TRUE
            ELSE IF character is a space: has_space <- TRUE
            ELSE: has_special <- TRUE
        END FOR

        detect whether any character occurs 3 times consecutively
        detect whether any PROHIBITED item is in normalized_password
        password_is_valid <- TRUE

        check length and each character-category flag
        check spaces, consecutive repetition, and prohibited substrings
        for every failed rule, display its explanation and set password_is_valid <- FALSE

        IF password_is_valid
            DISPLAY "Password meets this project's policy"
        ELSE
            DISPLAY "Password does not meet this project's policy"
        END IF
    END FOR

    DISPLAY "Password checking completed"
END
```

## Policy assumptions

The source case study does not set exact thresholds. This solution assumes an 8-character minimum, four character categories, no spaces, no three identical consecutive characters, and no case-insensitive occurrence of `password`, `123456`, or `qwerty`.
