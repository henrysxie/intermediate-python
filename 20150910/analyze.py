import csv
from warmup import aggregate


csv_file = open('rock.csv', 'rb')  # 'rU for Python 3+'

reader = csv.DictReader(csv_file)

rows = [row for row in reader]


def is_valid_year(candidate):
    try:
        int(candidate)
    except ValueError:
        return False
    else:
        return int(candidate) > 1900


print "There were {} songs released in 1981".format(
    len([row for row in rows if row['Release Year'] == '1981'])
)

print "There were {} songs before 1984".format(
    len([
        row for row in rows
        if is_valid_year(row['Release Year'])
        and int(row['Release Year']) < 1984])
)

print "{} was the earliest release year".format(
    min([
        row['Release Year']
        for row in rows
        if is_valid_year(row['Release Year'])
    ])
)

sorted_rows = sorted(
    rows,
    key=lambda x: x['PlayCount'],
    reverse=True
)


print "Top 20 songs were: {}".format(
    [row['Song Clean'] for row in sorted_rows][:20]
)


artist_tally = aggregate([row['ARTIST CLEAN'] for row in rows])


print "Top 10 prolific artists were: {}".format(
    sorted(
        artist_tally.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]
)


import ipdb; ipdb.set_trace();