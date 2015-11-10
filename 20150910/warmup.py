def print_evens(max_num):
    for n in xrange(1, max_num + 1):
        if n % 2 == 0:
            print n


def divisible_by_3():
    return [x for x in range(10001) if x % 3 == 0]


def get_max(numbers):
    """
    Returns the largest number in `numbers`
    """

    # Initialize max_num to be first number in list
    # (Can't set to 0 in case of all negative numbers)
    if not numbers:
        return None

    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num



def aggregate(orders):
    aggregate = {}

    # loop through all the orders for each item
    for item in orders:

        # If key already exists, increment
        if item in aggregate:
            aggregate[item] += 1

        # Else create key and set value to 1
        else:
            aggregate[item] = 1

    # Return aggregate
    return aggregate



def tally_food_orders_2(orders):
    aggregate = {}

    # loop through all the orders for each item
    for item in orders:
        aggregate[item] = orders.count(item)

    # Return aggregate
    return aggregate



print tally_food_orders_2(["burger", "fries", "burger", "burger", "tenders"])