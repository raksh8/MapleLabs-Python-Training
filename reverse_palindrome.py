def reverse_sum(num):
    """This function returns sum of given
    number and its reverse"""
    return int(num) + int(num[::-1])


def check(r_sum):
    pal = "not a palindrome"
    if r_sum == r_sum[::-1]:
        pal = "a palindrome"
        return int(r_sum), pal

    else:
        return int(r_sum)+int(r_sum[::-1]), pal


def main():
    n = input("Enter the number: ")
    r_sum = str(reverse_sum(n))
    ans, status = check(r_sum)
    print(f'The output of the given number is {ans} and it is {status}')


if __name__ == '__main__':
    main()




