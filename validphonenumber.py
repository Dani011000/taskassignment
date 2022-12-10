import re


def isvalid(number):
    pattern = re.compile("[+]?[0-9]?[(]?[ ]?[-]?[0-9]{3}[)]?[-]?[.]?[ ]?[0-9]{3}[-]?[.]?[ ]?[0-9]{4}")
    return pattern.match(number)


print("Enter the Phone number:")
number = input()
if isvalid(number):
    print("Valid Number")
else:
    print("Invalid Number")
