from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_restful import Resource


app = Flask(__name__)
CORS(app)
api = Api(app)


class Quote(Resource):
    """ The quotes View """

    def get(self):
        """ Returns a list of quotes """

        return {
            'quotes': "test"
        }


api.add_resource(Quote, '/')


if __name__ == "__main__":
    app.run()