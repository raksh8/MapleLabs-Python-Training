def find_median(lst):
    """This function returns the
    median of given numbers"""
    length = len(lst)
    lst.sort()
    m = length // 2
    if length % 2 == 0:
        return (lst[m] + lst[m - 1]) / 2
    return lst[m]


def main():
    lst_in = list(map(int, input("Enter the numbers separated by space: ").split()))
    print(find_median(lst_in))


if __name__ == '__main__':
    main()
