# FUNCTIONS
def int_to_string(num, base):
    """Converts number to string in any base"""
    all_digits = "0123456789ABCDEF"
    dividend = num / base
    if dividend < 1:
        return all_digits[num]
    else:
        return int_to_string(dividend, base) + all_digits[num % base]
    #The logic: this will make every leftover number the new leftmost number,
    #which is how conversion between bases works


# MAIN
def main():
    print int_to_string(90, 9)


if __name__ == '__main__':
    main()
