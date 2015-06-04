from collections import Counter
def print_evens():
    for i in xrange(2, 10000, 2):
        print i

def div_3():
    three_list = []
    for x in xrange(3, 10001, 3):
        three_list.append(x)
    return three_list

def get_max(nums):
    max_num = 0
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


def is_odd_or_div_7(some_list):
    return [x for x in some_list if (x % 7 == 0) | (x % 2 > 0)]


def num_is_odd_or_div_7(number):
    return number % 7 == 0 or not number % 2


def aggregate_counts(food):
    return Counter(food)
    # menu = {}
    # for item in food:
    #     if item in menu:
    #         menu[item] += 1
    #     else:
    #         menu[item] = 1
    # return menu


# print aggregate_counts(["burger", "fries", "burger", "tenders", "apple pie"])


def most_common(food):
    agg_counts = aggregate_counts(food)
    return max(agg_counts.iteritems(), key=lambda x: x[1])


print most_common(["burger", "fries", "burger", "tenders", "apple pie"])


