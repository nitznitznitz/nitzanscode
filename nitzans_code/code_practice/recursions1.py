# FUNCTIONS
def list_sum(numbers_list):
    """Receives list of numbers, returns their sum"""
    if len(numbers_list) == 1:
        return numbers_list[0]
    else:
        return numbers_list[0] + list_sum(numbers_list[1:])


# MAIN
def main():
    list_of_numbers = [1, 2, 3, 4]
    print list_sum(list_of_numbers)


if __name__ == '__main__':
    main()
