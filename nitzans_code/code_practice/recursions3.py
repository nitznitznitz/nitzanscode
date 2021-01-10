# FUNCTIONS
def recursive_list_sum(numbers_list):
    list_sum = 0
    for element in numbers_list:
        if type(element) == list:
            list_sum += recursive_list_sum(element)
        else:
            list_sum += element
    return list_sum


# MAIN
def main():
    print recursive_list_sum([1, 2, [3, 4], [5, 6]])


if __name__ == '__main__':
    main()