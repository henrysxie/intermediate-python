from exercises import get_most_popular

import csv

csvfile = open("rock.csv", 'rb')  # 'rU'

reader = csv.DictReader(csvfile)

songs = [song for song in reader]


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
        and int(song['Release Year']) < 1984])
))


print("The earliest release year is: {}".format(
    min([
        int(song['Release Year'])
        for song in songs
        if is_valid_year(song['Release Year'])
    ])
))

print("The top 20 songs by play count are: {}".format(
    [(song['Song Clean'], song['PlayCount']) for song
        in sorted(
            songs,
            key=lambda song: int(song['PlayCount']),
            reverse=True
        )[:20]]

))

artist_names = [song['ARTIST CLEAN'] for song in songs]

print("The most prolific artists were: {}".format(
    get_most_popular(artist_names, top=10)
))


print("There are {} unique artists in our data set.".format(
    len(set(artist_names))
))


print("The word rock appears in {} songs.".format(
    len([song for song in songs if "rock" in song['Song Clean'].lower()])
))
