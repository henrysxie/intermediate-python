def print_evens():
    for number in range(2, 10001, 2):
        print(number)


def get_thirds(divisor):
    return [x for x in range(1, 10000) if x % divisor == 0]


def get_number():
    number = raw_input("Give me a number!")
    try:
        int(number)
    except ValueError:
        print("You must give me a legit number.")
    except DifferentError:
        print("You must give me a legit number.")
    else:
        print("Cool, {} is a fine number. {}".format(
            number, number))


def divide(a, b):
    try:
        result = a / float(b)
    except (ValueError, TypeError):
        print("One of these things don't go into the other")
    except ZeroDivisionError:
        print("You can't divide by zero.")
    else:
        return result

def tally(strings):

    # Declare our dictionary
    shake_frequency = {}

    # Loop over the strings
    for string in strings:

        # Case 1: I've seen it before
        if string in shake_frequency:

            # Increment dictionary value by 1 at this key
            shake_frequency[string] += 1

        # Otherwise: First time I'm seeing this string
        else:

            # Add it as a key to our dictionary, and set value to 1
            shake_frequency[string] = 1

    # Return our dictionary
    return shake_frequency


def get_most_popular(strings, top=3):
    freqs = tally(strings)
    return sorted(
        freqs.items(),
        key=lambda pair: pair[1],
        reverse=True
    )[:top]



print get_most_popular(["burger", "fries", "burger", "burger", "burger", "fries", "fries", "apple pie", "tenders", "apple pie"])