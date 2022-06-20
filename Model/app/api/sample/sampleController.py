from flask_restx import Resource, reqparse, Namespace, fields
from flask import abort
import os
import shutil
import werkzeug
from werkzeug.datastructures import FileStorage
from configUtil.config import Config
from api.sample.sampleModel import SampleModel
import datetime

ns = Namespace('Sample',
               description='Operation add model', ordered=True, path="/BookSample")
config = Config()
sampleModel = SampleModel(ns)
postParser = SampleModel.postBook()

chosen=ChosenModel()


@ns.route('/add/Sample')
class SampleController(Resource):
    @ns.doc('Return average_ration of a book')
    @ns.expect(postParser)
    def post(self):
        " prediction average rating of a book"

        data = postParser.parse_args()

        try:
            result=0
            if (data["ratings_cout"]!=0 and data["num_page"]!=0 and data["text_review_count"]!=0):
                modelPath=config.getModelsPath()
                result=chosen.predict(data["author"],data["num_page"],data["ratings_cout"],data["text_review_count"],
                                     data["publisher"])

            return result
        except Exception as ex:
            abort(404, str(ex))



