import csv

csvfile = open('rock.csv', 'rb')

reader = csv.DictReader(csvfile)

songs = [song for song in reader]


def is_valid_year(year):
    return year.isdigit() and int(year) > 1900


print "Number of songs: {}".format(len(songs))

print "# songs released in 1981: {}".format(
    len([song for song in songs if song['Release Year'] == '1981'])
)

print "Earliest release year: {}".format(
    min([
        song['Release Year'] for song in songs
        if is_valid_year(song['Release Year'])
    ])
)

print "# songs released before 1984: {}".format(
    len([
            song for song in songs
            if (
                is_valid_year(song['Release Year'])
                and int(song['Release Year']) < 1984)
        ])
)

print "Top 20 hits were: {}".format(
    [song['Song Clean'] for song in
        sorted(
            songs,
            key=lambda x: x['PlayCount'],
            reverse=True
        )[:20]
    ]
)

from collections import Counter

artists = [song['ARTIST CLEAN'] for song in songs]

print len(set(artists))

print len([song for song in songs if "rock" in song['Song Clean'].lower()])







