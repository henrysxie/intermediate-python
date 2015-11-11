def tally(orders):
    """
    tally(["burger", "fries", "burger", "tenders", "apple pie"])
    -> { "burger": 2, "fries": 1, "tenders": 1, "apple pie": 1 }
    """
    order_dict = {}

    for order in orders:

        if order not in order_dict:

            # If it's the first time we've seen this 'order'
            order_dict[order] = 1

        else:

            # If we've seen it before
            order_dict[order] += 1

    return order_dict



def divide(a, b):
    try:
        return a / float(b)
    except TypeError:
        print "Numbers only!"
    except ZeroDivisionError:
        print "Cannot divide by zero."


def get_max(numbers):
    """
    get_max([1, 7, 3, 87, 2])
    -> 87
    """
    # initialize max_number to first number
    max_number = numbers[0]

    # Loop over numbers
    for num in numbers:

        # If num greater than max_number -> update max_number
        if num > max_number:
            max_number = num

    # Return max_number after for loop
    return max_number




def print_evenly_divisible_by(start, stop, div):

    num_list = []

    for number in range(start, stop + 1):
        if number % div == 0:
            num_list.append(number)

    return num_list



print tally(["burger", "fries", "burger", "tenders", "apple pie", "fries", "fries"])