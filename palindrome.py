def check_palindrome(str):
    str = str.lower()
    if str == str[::-1]:
        return f"{str} is a Palindrome"
    else:
        return f"{str} is not a palindrome"


def main():
    str_in = input("Enter the string: ")
    print(check_palindrome(str_in))


if __name__ == '__main__':
    main()