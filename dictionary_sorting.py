def sort_dict(dict1, sb):
    if sb.lower() == 'value':
        dict1 = {x: y for x, y in sorted(dict1.items(), key=lambda x: x[1])}
    elif sb.lower() == 'key':
        dict1 = {x: y for x, y in sorted(dict1.items())}

    return dict1


def main():
    count_dict = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
    sb_in = input("Enter if sorting should be based on 'key' or 'value': ")
    print(sort_dict(count_dict, sb_in))


if __name__ == '__main__':
    main()
