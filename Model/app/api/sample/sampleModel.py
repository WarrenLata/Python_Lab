
from flask_restx import fields, reqparse
from configUtil.config import Config
import werkzeug


class SampleModel():
    def __init__(self, ns):
        self.ns = ns
        self.config = Config()


    def postBook(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'title', type=str,
            location='form',
            required=True,
        )

        parser.add_argument(
            'publicationDate', type=str,
            location='form',
            required=True,
        )

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
            'languageCode', type=str,
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
        parser.add_argument(
            'actualvalue', type=float,
            location='form',
            required=True,
        )

        return parser

