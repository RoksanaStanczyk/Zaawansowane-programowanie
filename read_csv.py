import csv
from Movie import Movie

file = open('movies.csv', encoding="utf8")


def read(path):
    type(file)
    csvreader = csv.reader(file)

    rows = []
    for row in csvreader:
        movie = Movie(row[0], row[1], row[2]).__dict__
        rows.append(movie)
    return rows

