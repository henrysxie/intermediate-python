def print_evens():
    for i in range(1, 10001):
        if i % 2 == 0:
            print i


def thirds():
    list_3 = []
    for i in xrange(3, 10001, 3):
        list_3.append(i)
    return list_3


def list_comprehension():
    return [x for x in xrange(5, 10001, 5)]


def get_max(numbers):

    # Init max_number
    max_number = numbers[0]

    # Loop over list
    for number in numbers:

        # If current number > max_number, update max_number
        if number > max_number:
            max_number = number

    # Return max_number
    return max_number


def is_odd_or_div_by_7(x):
    # If number is not divisible by 2 OR divisible by 7, return it
    return x % 2 == 1 or x % 7 == 0


def get_sublist_of_numbers_odd_or_div_by_7(numbers):
    return [x for x in numbers if is_odd_or_div_by_7(x)]


def get_aggregate_order_counts(orders):

    # Create empty dict
    order_counts = {}

    # Loop over list
    for order in orders:

        # Check if already exists in dict
        if order in order_counts:
            order_counts[order] += 1
        else:
            order_counts[order] = 1

    # Return dict
    return order_counts

print get_aggregate_order_counts(
    ["burger", "fries", "burger", "tenders", "apple pie", "burger", "burger", "fries"]
)
