def print_evens(start, end):
    for number in range(start, end):
        if number % 2 == 0:
            print(number)


def div_by_3():
    triples = []
    for number in range(1, 10001):
        if number % 3 == 0:
            triples.append(number)
    return triples


def order_list(strings):

    # Init empty dict
    tally = {}

    # Loop over list of strings
    for string in strings:

        # Case 1: I've seen it before
        if string in tally:

            # Increment value
            tally[string] += 1

        # Case 2: It's a new string
        else:

            # Set value to 1
            tally[string] = 1

    # Return constructed dict
    return tally


def get_top(strings, top=2):
    tally = order_list(strings)
    return sorted(
        tally.items(),
        key=lambda pair: pair[1],
        reverse=True
    )[:top]
