import csv
from Movie import Movie
from Links import Links
from Ratings import Ratings
from lab7.Tags import Tags


def read(path):
    type(path)
    csvreader = csv.reader(path)
    next(csvreader)
    return csvreader


def readMovies():
    rows = []
    for row in read(path = open('movies.csv', encoding="utf8")):
        movie = Movie(row[0], row[1], row[2]).__dict__
        rows.append(movie)
    return rows


def readLinks():
    rows = []
    for row in read(path = open('links.csv', encoding="utf8")):
        links = Links(row[0], row[1], row[2]).__dict__
        rows.append(links)
    return rows


def readRatings():
    rows = []
    for row in read(path = open('ratings.csv', encoding="utf8")):
        ratings = Ratings(row[0], row[1], row[2], row[3]).__dict__
        rows.append(ratings)
    return rows


def readTags():
    rows = []
    for row in read(path = open('tags.csv', encoding="utf8")):
        tags = Tags(row[0], row[1], row[2], row[3]).__dict__
        rows.append(tags)
    return rows


