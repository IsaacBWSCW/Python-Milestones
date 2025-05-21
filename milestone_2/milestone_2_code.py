import re

def checkAndExplainPasswordStrength(password: str):
    lengthError = len(password) < 8
    lowercaseError = re.search(r"[a-z]", password) is None
    uppercaseError = re.search(r"[A-Z]", password) is None
    digitError = re.search(r"\d", password) is None
    symbolError = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Too short (minimum 8 characters)": lengthError,
        "Missing lowercase letter": lowercaseError,
        "Missing uppercase letter": uppercaseError,
        "Missing digit": digitError,
        "Missing special character": symbolError
    }

    if any(errors.values()):
        print("This password is weak for the following reasons:")
        for error, occurred in errors.items():
            if occurred:
                print(f"- {error}")
    else:
        print("This password is strong.")
        print("It is atleast 8 characters long.")
        print("It has atleast one lowercase letter.")
        print("It has atleast one uppercase letter.")
        print("It has atleast one digit.")
        print("It has atleast one special character.")

def main():
    print("Inputted information will not be saved, transmitted, or used outside of this program.")
    
    password = ""

    while len(password) == 0:
        password = input("Input a password: ")
        if len(password) == 0:
            print("Invalid password, please try again.")
    
    checkAndExplainPasswordStrength(password)

if __name__ == "__main__":
    main()