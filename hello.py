from collections import Counter


def even_10000():
    for num in xrange(0, 10001, 2):
        print num


def divisble_by_3():
    print [num for num in xrange(0, 10001, 3)]


# divisble_by_3()

def get_max(numbers):
    current_max = numbers[0]
    for number in numbers:
        if number > current_max:
            current_max = number
    return current_max


def is_odd_or_div_by_7(number):
    return number % 7 == 0 or number % 2 != 0


def get_sublist(numbers):
    return [number for number in numbers if is_odd_or_div_by_7(number)]


def get_aggregate_counts(food_orders):
    return Counter(food_orders)


def get_max_agg_count(food_orders):
    agg_counts = get_aggregate_counts(food_orders)
    return max(agg_counts.iteritems(), key=lambda x: x[1])

print get_max_agg_count(["burger", "fries", "burger", "ice_cream", "burger"])