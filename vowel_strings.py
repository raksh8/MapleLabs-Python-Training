import itertools


def all_possible_strings(str):
    """This function will return all
     possible strings of a given string"""
    lst = list(itertools.permutations(str))
    list_of_string = [''.join(x) for x in lst]
    return list_of_string


def main():
    # str_in = input("Enter the string")
    str_in = 'aeiou'
    for i in all_possible_strings(str_in):
        print(i)


if __name__ == '__main__':
    main()
