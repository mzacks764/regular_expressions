import validators
import sys

def main():
    email = input("What's your email address? ")
    if validate(email):
        print("Valid")
    else:
        print('Invalid')

def validate(email):
    answer = validators.email(email)
    return answer

if __name__ == '__main__':
    main()