def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n < 0:
        print('Enter non negative integer')
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def main():
    n1 = int(input("Enter the starting number: "))
    n2 = int(input("Enter the ending number: "))
    for i in range(n1, n2+1):
        print(fibonacci(i), end=' ')


if __name__ == '__main__':
    main()

