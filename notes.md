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
This reviews basic use of LISTS
def divisible_by_3():
    numbers = []
    for x in xrange(10001):
        if x % 3 == 0:
           numbers.append(x)
    return numbers
```
Note: we use `xrange` instead of `range` because `range` loads the entire list into memory, while `xrange` just creates an iterator: https://mail.python.org/pipermail/python-list/2012-November/634509.html. If you have a really big list, `xrange` is way faster. In Python 3 `range` works the same way as `xrange`.

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


8 - Given a list of food orders, e.g. ["burger", "fries", "burger", "tenders", "apple pie"], write a function that takes the list
and returns a dictionary with the different dishes as keys and the number of times they appear in the list as the values. For example,
Takes ["burger", "fries", "burger", "tenders", "apple pie"] and turns it into
{
   "burger": 2,
   "fries": 1,
   "tenders": 1,
   "apple pie": 1
}

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
    agg_counts = aggregate_counts(order_list)
    # the key is a function that tells `max` what to sort by
    # in this case, it's the second element of the tuple, e.g. 2 in ("burger", 2)
    # which is just the number of times it appears in the list of orders
    return max(agg_accounts.iteritems(), key=lambda: agg_count[1])
```
Note: for more on lambda functions, check this out http://www.diveintopython.net/power_of_introspection/lambda_functions.html


## Python Data Science Worksheet 1
## Objectives
- use csv library to read in data
- use pure Python techniques to extract insights about the data
- start getting acquainted with the Pandas library

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
>>> reader.filenames
```

2 - How many songs are from 1981?

Solution:
```
>>> rows = [row for row in reader]
>>> len([row for row in rows if row['Release Year'] == '1981'])
61
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
>>> def is_valid_year(value):
...     try:
...         val = int(value)
...     except ValueError:
...         pass
        else:
            return val
...

>>> release_years = [int(row['Release Year']) for row in rows if is_valid_year(row['Release Year'])]
>>> min(release_years)
1071
```

This doesn't make any sense! Exclude that!

#### Third pass
```
>>> def is_valid_year(value):
...     try:
...         val = int(value)
...     except ValueError:
...         pass
        else:
           if val > 1900:
              return val
>>> release_years = [int(row['Release Year']) for row in rows if is_valid_year(row['Release Year'])]
>>> min(release_years)
1955
```

That makes much more sense!

4 - How many songs are from before 1984
```
>>> before_1984 = [
    row for row in rows
    if is_valid_year(row['Release Year']) and is_valid_year(row['Release Year']) < 1984
]
>>> print len(before_1984)
```

5 - What are the top 20 songs by play count
HINT: use builtin sorted() function
```
>>> top_20_rows_by_play_count = sorted(rows, key=lambda row: row['PlayCount'], reverse=True)[:20]
>>> top_20_play_count_song_names = [row['Song Clean'] for row in top_20_rows_by_play_count]
["(Don't Fear) The Reaper", 'Layla', 'Back In Black', 'All Right Now', 'Refugee', 'Bad Company', 'Gimme Shelter', "Runnin' Down a Dream", "Jamie's Cryin'", 'Sweet Home Alabama', 'Foreplay (Long Time)', 'Over the Hills and Far Away', 'Who Are You', 'Lights', 'In the Air Tonight', 'Come Sail Away', 'Highway To Hell', 'Rock and Roll', 'Comfortably Numb', "Rock 'n' Roll Fantasy"]
```
6 - Who are the top 10 most prolific artists in the data along with the number of their songs that appear in the data?
```
>>> artists = [row['ARTIST CLEAN'] for row in rows]
>>> from collections import Counter
>>> artists_by_play_count = Counter(artists)
>>> artists_ordered_by_play_count = sorted(artists_by_play_count.items(), key=lambda artist_and_count: artist_and_count[1], reverse=True)
>>> artists_ordered_by_play_count[:10]
[('The Beatles', 100), ('Led Zeppelin', 69), ('Rolling Stones', 55), ('Van Halen', 44), ('Pink Floyd', 39), ('Aerosmith', 31), ('The Who', 31), ('Tom Petty & The Heartbreakers', 29), ('AC/DC', 29), ('Bob Seger', 24)]
```
7 - How many different artists appear in the data?
```
>>> artists = [row['ARTIST CLEAN'] for row in rows]
>>> len(set(artists))
475
```
NOTE: How is a Python set different from a list?

8 - How many songs does 'Rock'/'rock' appear in the title of?
```
>>> with_rock_in_title = [row for row in rows if 'rock' in row['Song Clean'].lower()]
>>> len(with_rock_in_title)
60
```
