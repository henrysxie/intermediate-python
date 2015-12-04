from exercises import tally

import csv
csv_file = open("rock.csv", 'rb')  # if Python 3, use 'rU'

reader = csv.DictReader(csv_file)

rows = [row for row in reader]



def is_valid_year(string):
    try:
        int(string)
    except ValueError:
        return False
    else:
        return int(string) > 1900


print "There were {} songs released in 1981.".format(
    len([x for x in rows if x['Release Year'] == '1981'])
)


print "There were {} songs released before 1984.".format(
    len([x for x in rows if is_valid_year(x['Release Year'])
                and int(x['Release Year']) < 1984])
)

print "The earliest release year is {}".format(
    min([row['Release Year']
        for row in rows
        if is_valid_year(row['Release Year'])])
)

top_5_songs = sorted(
    rows,
    key=lambda row: int(row['PlayCount']),
    reverse=True)

top_5_songs = top_5_songs[:5]

print "The top 5 songs were:"
for song in top_5_songs:
    print "{} {}".format(song['Song Clean'], song['PlayCount'])


# Transform list of dicts (rows) into list of artist names
artists = [row['ARTIST CLEAN'] for row in rows]

# Use the tally function to count how many times each artist name shows up
artist_freq = tally(artists)

# Sort it by count
top_artists = sorted(artist_freq.items(), key=lambda x: x[1], reverse=True)

# Slice to first 10
top_10_artists = top_artists[:10]

print "\nThe top 10 songs were:"

# Print out result
for pair in top_10_artists:
    print "{} {}".format(pair[0], pair[1])

