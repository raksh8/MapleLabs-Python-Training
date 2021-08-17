def interchange(lst):
    """This function interchanges the
     first and last value of the list"""
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


def main():
    lst1 = input("Enter the list separated by spaces: ").split()
    print(interchange(lst1))


if __name__ == '__main__':
    main()

