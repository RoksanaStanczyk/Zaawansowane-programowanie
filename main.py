from flask import Flask
from flask_restful import Resource, Api
from read_csv import read
app = Flask(__name__)
api = Api(app)

# path = open('movies.csv', encoding="utf8")
path = 'movies.csv'
class HelloWorld(Resource):
    def get(self):
        return read(path)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)