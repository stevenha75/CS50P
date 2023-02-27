from validator_collection import validators

def main():
    # Asking for inputs
    email = input("What's your email address? ")

    # Check email
    try:
        email_address = validators.email(email)
        print("Valid")
    except ValueError:
        print("Invalid")

if __name__ == "__main__":
    main()