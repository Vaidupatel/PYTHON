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