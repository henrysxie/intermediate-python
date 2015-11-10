## What is this class about?
In this class, you will:
- Learn intermediate Python techniques
- Become comfortable working with data

## Shell vs Scripting Python
### Shell:

1. Open Terminal
2. run
```bash
$ python
>>> "Hello"
Hello
>>> 2 + 2
4
>>> exit()
$
```

### Scripting
Run:
```bash
$ mkdir ~/Documents/ga-intermediate-python
$ cd ~/Documents/ga-intermediate-python
$ touch test.py
```

In your editor, open up test.py and write the following line:
`print "Hello, world!"`
Save and close the file.
Then in the terminal, run
```
$ python test.py
Hello, world!
```


## Python Exercises

1 - Write a function that prints all the even numbers between 1 and 10,000.

Solution:
```python
def print_evens():
    for x in xrange(10001):
        if x % 2 == 0:
           print x
```
This reviewed FOR LOOPS, IF CONDITIONS, and PRINTING

2 - Write a function that returns a list of the numbers between 1 and 10,000 that are divisible by 3.

Solution:
```python
def divisible_by_3():
    numbers = []
    for x in xrange(10001):
        if x % 3 == 0:
           numbers.append(x)
    return numbers
```
This reviews basic use of LISTS. Note: we use `xrange` instead of `range` because `range` loads the entire list into memory, while `xrange` just creates an iterator: https://mail.python.org/pipermail/python-list/2012-November/634509.html. If you have a really big list, `xrange` is way faster. In Python 3 `range` works the same way as `xrange`.

3 - The same as #2, but use Python list comprehensions.

Solution:
```python
def divisible_by_3():
    return [x for x in xrange(10001) if x % 3 == 0]
```
Note: List comprehensions are super useful. They allow you to iterate through lists and generate new lists on the fly with very little code.

4 - Write a function that takes a list of numbers and returns the max of those numbers, don't ues the max() function.

Solution:
```python
def get_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
           max_number = number
    return max_number
```
Note: Here we just tested out our logic skills.

5 - Write a function that returns True if a number is odd or divisble by 7 and False otherwise.

Solution:
```python
def is_odd_or_div_by_7(number):
    return number % 2 == 1 or number % 7 == 0
```

6 - Use the function in #5 and list comprehensions to write a function that given a list of numbers returns a sublist of numbers
that are odd or divisible by 7.

Solution:
```python
def get_sublist_of_numbers_odd_or_div_by_7(numbers):
    return [number for number in numbers if is_odd_or_div_by(number)]
```
Note: Here we are combining our knowledge of list comprehensions with some conditional logic inside the list comprehension.

7 - Write a division function `divide(a, b)` that catch exceptions and return an error string if the arguments do not make sense. 

Solution:
```python

def divide(a, b):
    try:
        result = a / b
    except TypeError:
        return "Both the numerator and denominator must be valid numbers."
    except ZeroDivisionError:
        return "The denominator cannot be zero."
    else:
        return result
```
Do not catch the general `Exception` since we won't know if some other error occurred.


8 - Given a list of food orders, write a function that takes the list and returns a dictionary with the different dishes as keys and the number of times they appear in the list as the values. For example,
Takes `["burger", "fries", "burger", "tenders", "apple pie"]` and returns:
```python
{
   "burger": 2,
   "fries": 1,
   "tenders": 1,
   "apple pie": 1
}
```

Solution:
```python
def tally(order_list):
    orders_by_count = {}
    for order in order_list:
        # if we've already seen this order, increment the count
        if order in orders_by_count:
           orders_by_count[order] += 1
        # otherwise, this is the first time we're seeing it, so set its count to 1
        else:
           orders_by_count[order] = 1
    return orders_by_count
```

9 - Write a function that takes the same kind of input as in #8 but instead of returning a dictionary with the counts, it just returns a tuple: the dish that appears the most in the list and the number of times it appears in the list. So the output given the example would be ("burger", 2)

Solution:
```python
def get_most_popular_order_data(order_list):
    order_tally = tally(order_list)
    # the key is a function that tells `max` what to sort by
    # in this case, it's the second element of the tuple, e.g. 2 in ("burger", 2)
    # which is just the number of times it appears in the list of orders
    return max(order_tally.iteritems(), key=lambda x: x[1])
```
Note: for more on lambda functions, check this out http://www.diveintopython.net/power_of_introspection/lambda_functions.html


## Data Analysis
## Objectives
- use csv library to read in data
- use Python techniques to extract insights about the data

### Exercises

1 - Using csv library, read in data from https://raw.githubusercontent.com/suneel0101/data/master/classic-rock/classic-rock-song-list.csv.
NOTE: Make sure to open the file on the browser, highlight and copy the contents into your text editor and save. Otherwise, you'll get some errors when trying to read the file through the `csv` library.
HINT: Here's the relevant documentation on csv: https://docs.python.org/2/library/csv.html, use `DictReader`
```
$ python
>>> import csv
>>> csvfile = open('rock.csv', 'rb')   # Use 'rU' for Python 3
>>> reader = csv.DictReader(csvfile)
>>> dir(reader)
>>> reader.fieldnames
```

2 - How many songs are from 1981?

Solution:
```
print "# songs released in 1981 is: {}".format(
    len([row for row in rows if row["Release Year"] == "1981"])
)
```

3 - What is the earliest release year in the data?
HINT: You might have to account for/clean up dirty data

#### First pass
```
>>> min([int(row['Release Year']) for row in rows if row['Release Year']])
ValueError: invalid literal for int() with base 10: 'SONGFACTS.COM'
```
SONGFACTS.com is not a valid year, so we'll have to clean up Release Year by ensuring we are dealing with integers.

#### Second pass
```
def is_valid_year(string):
    try:
        year = int(string)
    except ValueError:
        return False
    else:
        return year

>>> release_years = [int(row['Release Year']) for row in rows if is_valid_year(row['Release Year'])]
>>> min(release_years)
1071
```

This doesn't make any sense! Exclude that!

#### Third pass
```
def is_valid_year(string):
    try:
        year = int(string)
    except ValueError:
        return False
    else:
        return year > 1900
        

print "Earliest release year is: {}".format(
    min([row['Release Year'] for row in rows
        if is_valid_year(row['Release Year'])])
)
```

That makes much more sense!

4 - How many songs are from before 1984
```
print "# songs released before 1984 is: {}".format(
    len([row for row in rows
        if is_valid_year(row["Release Year"])
        and int(row["Release Year"]) < 1984])
)
```

5 - What are the top 20 songs by play count
HINT: use builtin sorted() function
```
top = sorted(rows, key=lambda x: x['PlayCount'], reverse=True)
print "Top 20 songs by play count are: "
for data in [(row['PlayCount'], row['Song Clean']) for row in top[:20]]:
    print data
```

6 - Who are the top 10 most prolific artists in the data along with the number of their songs that appear in the data?
```
# ["Led Zeppelin", "Led Zeppelin", "Rolling Stones", ...]
artist_names = [row["ARTIST CLEAN"] for row in rows]

# {"Led Zeppelin": 69, "Rolling Stones": 56}
artist_tally = tally(artist_names)

# [("Led Zeppelin", 35), ...]
pairs = sorted(artist_tally.items(), key=lambda x: x[1], reverse=True)

print "Top 10 most prolific artists are: "
for pair in pairs[:10]:
    print pair
```

7 - How many different artists appear in the data?
```
print "# different artists is: {}".format(
    len(set(artists))
)
```
NOTE: How is a Python set different from a list?

8 - How many songs does 'Rock'/'rock' appear in the title of?
```
print "# songs with word rock (case insensitive) in title is: {}".format(
    len([row for row in rows if 'rock' in row['Song Clean'].lower()])
)
```
