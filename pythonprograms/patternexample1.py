import re
# dd/mm/yyyy

def validatepassword(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$])(?=.*\d)([A-Za-z\d@#$]){5,10}$"
    isvalid=False
    if re.match(pattern,password):
        isvalid=True
    return isvalid


def validateDate(date):
    pattern = r"\d{2}/\d{2}/\d{4}"
    isvalid = False
    if re.match(pattern, date):
        isvalid = True
    return isvalid


def validatePhone(phone):
    pattern = r"[6-9]\d{9}"
    isvalid = False
    if re.match(pattern, phone):
        isvalid = True
    return isvalid


def validateEmail(email):
    pattern = r"^[\w\.]+@wipro\.com$"
    isvalid = False
    if re.fullmatch(pattern, email):
        isvalid = True
    return isvalid


def check():
    pattern = r"^A.*A$"
    strings = ["A", "AA", "ABA", "APPLE", "AP123", "AB"]

    for text in strings:
        if re.match(pattern, text):
            print("Pattern is valid")
        else:
            print("Invalid pattern")

if __name__ == "__main__":
   # check()
   """
    email = input("Enter a an email id")
    if validateEmail(email):
        print("Email is valid ")
    else:
        print("Email is not valid")
    phone = input("Enter a phone number")
    if validatePhone(phone):
       print("Phone number is valid")
    else:
       print("Phone number is not valid")

    date = input("Enter the date (DD/MM/YYYY)")
    if validateDate(date):
        print("Date is valid")
    else:
        print("Date is not valid")
    """

   password = input("enter a password")
   if validatepassword(password):
       print("Password is valid")
   else:
       print("Password is not valid")
