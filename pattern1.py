def pattern1(n):
    # for reversed triangle
    for i in range(n, 0, -1):

        for k in range(n - i + 1):
            print(' ', end='')

        for j in range(i):
            print('* ', end='')

        print()

    # for normal triangle
    for i in range(2, n + 1):
        for k in range(n - i + 1):
            print(' ', end='')

        for j in range(i):
            print('* ', end='')

        print()


def main():
    n = int(input('Enter the number of stars in first row: '))
    pattern1(n)


if __name__ == '__main__':
    main()
