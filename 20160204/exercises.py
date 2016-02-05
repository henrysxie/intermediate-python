import math

def print_evens():
    for number in range(1, 10000):
        if number % 2 == 0:
            print(number)


def evens():
    for number in range(2, 10000, 2):
        print(number)

def div_by(divisor, start=0, end=10000):
    result = []
    for number in range(start, end):
        if number % divisor == 0:
            result.append(number)
    return result


def get_max(numbers):
    current_big = numbers[0]

    for number in numbers:
        if number > current_big:
            current_big = number

    return current_big


def is_odd_or_div_by_7(number):
    return number % 2 != 0 or number % 7 == 0


def get_sublist_of_numbers_odd_or_div_by_7(numbers):
    return [x for x in numbers if is_odd_or_div_by_7(x)]


def validate_number(text):
    try:
        number = int(text)
    except ValueError:
        return False
    else:
        return number


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Can't divide by zero buddy."
    except TypeError:
        return "You can't divide non-numbers dude."
    else:
        return result


def get_aggregate_order_counts(orders):
    tally = {}
    for food in orders:
        if food in tally:
            tally[food] += 1
        else:
            tally[food] = 1
    return tally


def get_most_popular_order_data(orders, limit=1):
    tally = get_aggregate_order_counts(orders)
    items = tally.items()
    return sorted(items, key=lambda x: x[1], reverse=True)[:limit]

print(get_most_popular_order_data([
    "burger",
    "fries",
    "burger",
    "tenders",
    "apple pie",
    "burger",
    "burger",
    "fries"
]))