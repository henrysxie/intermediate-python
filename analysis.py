from collections import Counter
import csv
csvfile = open('rock.csv', 'rb')
reader = csv.DictReader(csvfile)

rows = [row for row in reader]

num_from_1981 = len([
    row['Song Clean']
    for row in rows
    if row['Release Year'] == '1981'
])

def is_valid_year(candidate):
    return candidate.isdigit() and int(candidate) > 1900 and int(candidate)

get_earliest = min([
    int(row['Release Year'])
    for row in rows
    if is_valid_year(row['Release Year'])
])

num_before_1984 = len([
    subrow for subrow in rows
    if is_valid_year(subrow['Release Year'])
    and is_valid_year(subrow['Release Year']) < 1984
])

top_20 = sorted(
    rows,
    key=lambda row: row['PlayCount'],
    reverse=True
)[:20]


# Get all the artists names
artists = [row['ARTIST CLEAN'] for row in rows]

# Get frequency tally of artists
artists_by_song = Counter(artists)

# Order tally by frequency
ordered_artists = sorted(artists_by_song.items(), key=lambda tuple: tuple[1], reverse=True)

# Grab top 5
top_5 = ordered_artists[:5]

num_unique_artists = len(set(artists))

import ipdb; ipdb.set_trace();
