""" 
This is some conditions to validate the email

a-z
0-9
. _ occure ones
@ occure one
. 2nd or 3rd from last
"""


# First approach
"""
email = input("Enter your email\n")  # Example: g@g.in

valid_chars = ["_", ".", "@"]
errors = []

if len(email) < 6:
    errors.append("Email length must be at least 6 characters.")
elif not email[0].isalpha():
    errors.append("Email must start with an alphabetic character.")
elif email.count("@") != 1:
    errors.append("Email must contain exactly one '@' symbol.")
elif not (email[-4] == ".") ^ (email[-3] == "."):
    errors.append("Invalid domain format.")
else:
    for char in email:
        if char.isspace():
            errors.append("Email cannot contain whitespace characters.")
            break
        elif char.isalpha() and char.isupper():
            errors.append("Email cannot contain uppercase letters.")
            break
        elif char not in valid_chars and not char.isdigit():
            errors.append("Email contains invalid characters.")
            break

if errors:
    print("Invalid email address. Errors:")
    for error in errors:
        print("-", error)
else:
    print("Email is correct!!")


"""

# Or it can be done using the regex

import re
email_condition = r"^[a-z]+[\\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email = input("Please enter your email address\n")

if re.search(email_condition, user_email):
    print("Valid email address")
else:
    print("Invalid email address")