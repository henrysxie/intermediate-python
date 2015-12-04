

def print_evens(max_num):
    for num in range(max_num):
        if num % 2 == 0:
            print num


def get_div_by_3():
    result = []
    numbers = range(1, 10001)
    for num in numbers:
        if num % 3 == 0:
            result.append(num)

    return result


def get_max(numbers):

    # Initialize variable max_num to be first element in list
    max_number = numbers[0]

    # Loop over numbers list
    for number in numbers:

        # Compare max_num with current number
        if number > max_number:

            # If current numbers is greater, update max_num
            max_number = number

    # Return max_num
    return max_number


def tally(orders):

    # Initialize result variable to empty dictionary
    menu = {}

    # Loop over all orders
    for order in orders:

        # If order does not exist in our dictionary,
        # add a key-value pair where the key is the food order
        # and the value is 1
        if not order in menu:
            menu[order] = 1

        # Otherwise, it means the order already exists in our dictionary
        # so go ahead and increment that value by 1
        else:
            menu[order] += 1

    # Return result
    return menu


def get_most_popular_orders(orders):
    menu = tally(orders)
    print(sorted(menu.items(), key=lambda x: x[1], reverse=True))
