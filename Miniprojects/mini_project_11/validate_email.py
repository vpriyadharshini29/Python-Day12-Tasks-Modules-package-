import re

email = input("Enter email: ")
pattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")
