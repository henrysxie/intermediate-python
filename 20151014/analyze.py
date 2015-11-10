# Import built-in CSV module
import csv

csvfile = open('rock.csv', 'rb')   # 'rU'

reader = csv.DictReader(csvfile)

rows = [row for row in reader]


def tally(strings):

    # Create empty dict
    tally = {}

    # Loop over list
    for string in strings:

        # Check if already exists in dict
        if string in tally:
            tally[string] += 1
        else:
            tally[string] = 1

    # Return dict
    return tally


def is_valid_year(string):
    try:
        int(string)
    except ValueError:
        return False
    else:
        return int(string) > 1900


print "# songs released in 1981 is: {}".format(
    len([row for row in rows if row["Release Year"] == "1981"])
)

print "# songs released before 1984 is: {}".format(
    len([row for row in rows
        if is_valid_year(row["Release Year"])
        and int(row["Release Year"]) < 1984])
)

print "Earliest release year is: {}".format(
    min([x['Release Year'] for x in rows
        if is_valid_year(x['Release Year'])])
)


top = sorted(rows, key=lambda x: x['PlayCount'], reverse=True)
print "Top 20 songs by play count are: "
for data in [(row['PlayCount'], row['Song Clean']) for row in top[:20]]:
    print data

# ["Led Zeppelin", "Led Zeppelin", "Rolling Stones", ...]
artist_names = [row["ARTIST CLEAN"] for row in rows]

# {"Led Zeppelin": 69, "Rolling Stones": 56}
artist_tally = tally(artist_names)

# [("Led Zeppelin", 35), ...]
pairs = sorted(artist_tally.items(), key=lambda x: x[1], reverse=True)

print "Top 10 most prolific artists are: "
for pair in pairs[:10]:
    print pair

