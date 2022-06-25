from flask_restx import fields, reqparse
from configUtil.config import Config
import werkzeug


class Models():
    def __init__(self, ns):
        self.ns = ns
        self.config = Config()



    def postModel(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'author', type=str,
            location='form',
            required=True,
        )
        parser.add_argument(
            'numPage', type=int,
            location='form',
            required=True,
        )
        parser.add_argument(
            'ratingCount', type=int,
            location='form',
            required=True,
        )
        parser.add_argument(
            'textReviewCount', type=int,
            location='form',
            required=True,
        )
        parser.add_argument(
            'publisher', type=str,
            location='form',
            required=True,
        )
        return parser

    def uploadModelParser(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'file', type=werkzeug.datastructures.FileStorage,
            location='files',
            required=True,
        )
        parser.add_argument(
            'name',
            required=False
        )
        parser.add_argument(
            'description',
            required=False
        )

        return parser