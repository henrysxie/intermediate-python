from collections import Counter
import csv

csvfile = open('rock.csv', 'rb')
reader = csv.DictReader(csvfile)

rows = [row for row in reader]

eightyone = [row for row in rows if row['Release Year'] == '1981']


def is_valid_year(candidate):
    # return candidate.isdigit()
    return candidate[0:2] in ['19', '20']

# first_song = min([
#     int(row['Release Year']) for row in rows
#     if is_valid_year(row['Release Year'])
# ])

artists = [row['ARTIST CLEAN'] for row in rows]
top_artists = Counter(artists).most_common(10)
# print top_artists
# print len(set(artists))



titles = [row['Song Clean'] for row in rows]
rock_songs = [title for title in titles if 'rock' in title.lower()]
print len(rock_songs)



# sorted_play_count = sorted(rows, reverse=True, key=lambda row: int(row['PlayCount']))
# print sorted_play_count[:20]




# row_count = 0
# for row in rows:
#     if row['Release Year'] == '1981':
#         row_count += 1

# print row_count