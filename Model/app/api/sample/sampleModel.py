rom
flask_restx
import fields, reqparse
from configUtils.config import Config
import werkzeug


class SampleModel():
    def __init__(self, ns):
        self.ns = ns
        self.config = Config()


    def postBook(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'author', type=str,
            location='form',
            required=True,
        )
        parser.add_argument(
            'num_pages', type=int,
            location='form',
            required=True,
        )
        parser.add_argument(
            'language_code', type=str,
            location='form',
            required=True,
        )
        parser.add_argument(
            'ratings_count', type=int,
            location='form',
            required=True,
        )
        parser.add_argument(
            'text_review_count', type=int,
            location='form',
            required=True,
        )
        parser.add_argument(
            'publisher', type=str,
            location='form',
            required=True,
        )
        parser.add_argument(
            'actualValue', type=float,
            location='form',
            required=True,
        )

        return parser

