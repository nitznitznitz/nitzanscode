# FUNCTIONS
def list_sum(numbers_list):
    """Receives list of numbers, returns their sum"""
    return sum(numbers_list)


# MAIN
def main():
    list_of_numbers = [1, 2, 3]
    print list_sum(list_of_numbers)


if __name__ == '__main__':
    main()