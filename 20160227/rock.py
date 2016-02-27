# Importing built-in CSV module
import csv

# Importing out get_top function
from exercises import get_top

# Opening up our data set in read mode
csv_file = open('rock.csv', 'rb')  # Use 'rU' for Python 3

# Reading it into Python dictionaries
reader = csv.DictReader(csv_file)

# Reading through the file, into a list
songs = [row for row in reader]


def is_valid_year(string):
    try:
        int(string)
    except ValueError:
        return False
    else:
        return int(string) > 1900


print("There were {} songs released in 1981".format(
    len([song for song in songs if song['Release Year'] == '1981'])
))

print("There were {} songs released before 1984".format(
    len([
        song for song in songs
        if is_valid_year(song['Release Year'])
            and int(song['Release Year']) < 1984
    ])
))

print("The first rock song was written in {}".format(
    min([int(song['Release Year']) for song in songs if is_valid_year(song['Release Year'])])
))

#
top_20_songs = sorted(
    songs,
    key=lambda song: int(song['PlayCount']),
    reverse=True
)[:20]

print("The top 20 songs are: ")
for song in top_20_songs:
    print("{} ({})".format(
        song['Song Clean'],
        song['PlayCount']
))


# Get list of artist names
artist_names = [song['ARTIST CLEAN'] for song in songs]

# Call our get_top function from exercises
top_10 = get_top(artist_names, top=10)

# Print result
for pair in top_10:
    print(pair)

print("The number of songs with 'rock' in the title (case insensitive) is: {}".format(
    len([s for s in songs if "ROCK" in s['Song Clean'].upper()])
))
