def even():
    for x in xrange(0, 10001, 2):
        print x


def divisble_by_3():
    result = []
    for x in xrange(0, 10001):
        if x % 3 == 0:
            result.append(x)
    print result


def list_comp():
    print [x for x in xrange(0, 10001) if not x % 3]


def get_max(numbers):
    max_value = numbers[0]
    for x in numbers:
        if x > max_value:
            max_value = x
    print max_value



def is_odd_or_divisible_by_7(num):
    return bool(num % 2 or not num % 7)


def get_sublist_of_numbers_odd_or_div_7(alist):
    print [i for i in alist if is_odd_or_divisible_by_7(i)]


def agg_orders(orders):
    aggregate_orders = {}
    for x in orders:
        if x in aggregate_orders:
            aggregate_orders[x] += 1
        else:
            aggregate_orders[x] = 1
    return aggregate_orders


get_sublist_of_numbers_odd_or_div_7(xrange(15))