def fact(n):
    """This function returns factorial
    of the given number"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)


def trail_zero(n1):
    """This function returns trailing
        zeros of the given number"""
    count = 0
    while n1 > 0:
        if n1 % 10 == 0:
            count += 1
            n1 /= 10
        else:
            break

    return count


def main():
    num = int(input("Enter the number: "))
    fact_num = fact(num)
    print(trail_zero(fact_num))


if __name__ == '__main__':
    main()
