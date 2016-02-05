import csv

csv_file = open('rock.csv', 'rU')  # for Python 2, do 'rb'

reader = csv.DictReader(csv_file)

songs = [row for row in reader]


def tally(orders):

    menu = {}

    # Loop over input list of strings
    for item in orders:

        # Case 1: First time I've seen this string
        if not item in menu:

            # Add the string as a key in the dictionary and set value to 1
            menu[item] = 1

        # Case 2: I've seen this string before
        else:
            # Find the value in the dictionary and increment it by 1
            menu[item] += 1

    # Return the dictionary
    return menu


def get_top_artists(orders, top=3):
    menu = tally(orders)

    # Get list of key-value pairs from dictionary
    pairs = list(menu.items())

    # Sort it by the value in descending order
    sorted_pairs = sorted(pairs, key=lambda menu_item: menu_item[1], reverse=True)

    # Limit it to the first three elements
    return sorted_pairs[:top]


def is_valid_year(string):
    try:
        int(string)
    except ValueError:
        return False
    else:
        return int(string) > 1900

# Use list comprehension to filter down our list
# of all songs to just songs released in 1981
num_songs_from_1981 = len([
    song for song in songs
    if song['Release Year'] == '1981'
])

print("There were {} songs released in 1981".format(
    num_songs_from_1981))

num_songs_before_1984 = len([
    song for song in songs
    if is_valid_year(song['Release Year'])
    and int(song['Release Year']) < 1984
])

print("There were {} songs released before 1984".format(
    num_songs_before_1984))

print("The earliest release year in the data is: {}".format(
    # Our answer here
    min([
        song for song in songs
        if is_valid_year(song['Release Year'])],
        key=lambda song: song['Release Year'])
    ['Release Year']
))

top_20_songs = sorted(
    songs,
    key=lambda song: int(song['PlayCount']),
    reverse=True
)[:20]

print("The top 20 songs are:")
for song in top_20_songs:
    print("{}: {}".format(song['Song Clean'], song['PlayCount']))

artists = [song['ARTIST CLEAN'] for song in songs]

top_10_artists = get_top_artists(artists, top=10)

print("The top 10 artists are:")
for artist in top_10_artists:
    print(artist)

print("There are {} many different artists".format(
    len(list(set(artists)))
))

print("There are {} songs with 'rock' in it".format(
    len([
        song for song in songs
        if song['Song Clean'].lower().find('rock') > -1])
))
import ipdb; ipdb.set_trace();

print(reader.fieldnames)