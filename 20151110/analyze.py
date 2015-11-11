from exercises import tally

import csv

csv_file = open('rock.csv', 'rb')  # Use rU for Python 3

reader = csv.DictReader(csv_file)

rows = [row for row in reader]


def is_valid_year(string):
    """
    '1981' -> True
    '' -> False
    'Gibberish' -> False
    """
    try:
        int(string)
    except ValueError:
        return False
    else:
        return int(string) > 1900


print "The first song is called: {}".format(
    rows[0]['Song Clean'])

print "There were {} songs from 1981".format(
    len([row for row in rows if row['Release Year'] == '1981']))

print "There were {} songs before 1984".format(
    len([row for row in rows
        if is_valid_year(row['Release Year'])
        and int(row['Release Year']) < 1984])

)

print "The earliest release year is: {}".format(
    min([int(row['Release Year'])
        for row in rows
        if is_valid_year(row['Release Year'])])
)


print "The top 20 songs by play count are: {}".format(
    [(row['Song Clean'], row['PlayCount'])
    for row in sorted(
        rows,
        key=lambda row: int(row['PlayCount']),
        reverse=True)][:20])



artist_names = [row['ARTIST CLEAN'] for row in rows]

artists_by_song_count = tally(artist_names)

pairs = artists_by_song_count.items()

sorted_pairs = sorted(pairs, key=lambda pair: pair[1], reverse=True)

top_10 = sorted_pairs[:10]

print "The top 10 most profilic artists are: {}".format(
    top_10
)

