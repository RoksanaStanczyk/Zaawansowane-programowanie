from flask import Flask
from flask_restful import Resource, Api
from read_csv import readLinks
from read_csv import readMovies
from read_csv import readRatings
from read_csv import readTags


app = Flask(__name__)
api = Api(app)


class Movies(Resource):
    def get(self):
        return readMovies()


class Links(Resource):
    def get(self):
        return readLinks()


class Ratings(Resource):
    def get(self):
        return readRatings()


class Tags(Resource):
    def get(self):
        return readTags()


class HelloWorld(Resource):
    def get(self):
        return 'Hello World!'


api.add_resource(HelloWorld, '/')
api.add_resource(Movies, '/movies')
api.add_resource(Links, '/links')
api.add_resource(Ratings, '/ratings')
api.add_resource(Tags, '/tags')


if __name__ == '__main__':
    app.run(debug=True)