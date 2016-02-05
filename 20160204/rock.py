import csv
from exercises import get_most_popular_order_data


csvfile = open('rock.csv', 'rU') # 'rb' for Python 2
reader = csv.DictReader(csvfile)

rows = [row for row in reader]

print("There were {} songs released in 1981".format(
    len([row for row in rows if row['Release Year'] == '1981'])
))

print("There were {} songs released before 1984".format(
    len([row for row in rows if row['Release Year'].isdigit() and int(row['Release Year']) < 1984])
))

print("The first rock song was released in: {}".format(
    min([row['Release Year'] for row in rows if row['Release Year'].isdigit() and int(row['Release Year']) > 1900])
))

top_20 = sorted(rows, key=lambda row: int(row['PlayCount']), reverse=True)[:20]
for song in top_20:
    print("{} ({})".format(song['Song Clean'], song['PlayCount']))

artist_names = [row['ARTIST CLEAN'] for row in rows]
top_10 = get_most_popular_order_data(artist_names, 10)
print("The top 10 most prolific artists were:")
for artist in top_10:
    print(artist)

print("There are {} different artists in this data set.".format(
    len(set(artist_names))
))


print("The word rock appears in the title of {} songs.".format(
    len([row for row in rows if "rock" in row['Song Clean'].lower()])
))
