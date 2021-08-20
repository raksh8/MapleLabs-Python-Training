def missing_digits(n_set):
    """This function will return missing
    digits from a phone number"""
    dig_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
    return dig_set - n_set


def main():
    num = set(map(int, list(input("Enter the phone number: "))))
    print(missing_digits(num))


if __name__ == '__main__':
    main()
