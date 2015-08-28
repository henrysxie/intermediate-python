

def even_numbers():
    """
    Prints all even numbers between 1 and 10000.
    """
    for number in range(1, 10001):
        if number % 2 == 0:
            print number


def get_max(numbers):
    """
    Returns largest number in given list.
    """

    # Initialize temp variable to first in list
    best = numbers[0]

    # Loop over list
    for i in numbers:

        # if current number is > temp, reset temp to current number
        if i > best:
            best = i

    # Print result
    return best


def is_odd_or_div_by_7(num):
    return num % 2 != 0 or num % 7 == 0


def get_sublist_of_numbers_odd_or_div_by_7(numbers):
    return [x for x in numbers if is_odd_or_div_by_7(x)]



def get_aggregate_orders(food_list):

    # Create empty dict
    tally = {}

    # loop over food_list
    for item in food_list:

        # if we've seen the item before, increment by one
        if item in tally:
            tally[item] += 1
        # if it's the first time we see this item
        else:
            tally[item] = 1

    return tally



def get_most_popular_order_data(food_list):
    tally = get_aggregate_orders(food_list)

    # [("burger", 2), ("fries": 1)]
    max_value = max(tally.values())

    return [x for x in tally.items() if x[1] == max_value]


    # return tally.items()
    # return max(tally.items(), key=lambda x: x[1])


# print get_aggregate_orders(["burger", "fries", "burger", "ice_cream"])
print get_most_popular_order_data(["burger", "fries", "burger", "fries", "ice_cream"])

