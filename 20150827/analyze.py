import csv
from collections import Counter

# Opening up raw csv file
csv_file = open('rock.csv', 'rb')  # if doesn't work: try just 'r', 'rU'

# Instantiating DictReader (reads in the data into Python dictionaries)
reader = csv.DictReader(csv_file)

rows = [row for row in reader]

num_songs_1981 = len([row for row in rows if row['Release Year'] == '1981'])

def is_valid_year(year):
    try:
        int(year)
    except ValueError:
        return False
    else:
        return int(year) > 1900


num_songs_before_1984 = len(
    [row for row in rows
    if is_valid_year(row['Release Year'])
    and int(row['Release Year']) < 1984])

earliest_release_year = min(
    [row['Release Year'] for row in rows if is_valid_year(row['Release Year'])
])

top_twenty_rows = sorted(rows, key=lambda row: row['PlayCount'], reverse=True)[:20]
top_twenty_songs = [row['Song Clean'] for row in top_twenty_rows]

# Get tally of artists (tallied by # songs written)

artists = [row['ARTIST CLEAN'] for row in rows]

artists_by_play_count = Counter(artists)

top_ten_prolific_artists = sorted(artists_by_play_count.items(), key=lambda x: x[1], reverse=True)[:10]

def contains_rock(song_title):
    return "rock" in song_title.lower()


print "There were {} songs released in 1981".format(num_songs_1981)

print "There were {} songs released before 1984".format(num_songs_before_1984)

print "Earliest release year is: {}".format(earliest_release_year)

print "The top 20 songs by play count are:"
print top_twenty_songs

print "The top 10 most profilic artists are:"
print top_ten_prolific_artists

print "There are {} different rock artists".format(
    len(set(artists)))


print "{} different rock artists wrote {} different songs, in total".format(
    len(set(artists)), len(rows))

print "There are {} songs with the word 'rock' in it".format(
    len([x for x in rows if contains_rock(x['Song Clean'])]))

