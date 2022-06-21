from flask_restx import Resource, reqparse, Namespace, fields
from flask import abort
import os
import shutil
import werkzeug
from werkzeug.datastructures import FileStorage
from configUtil.config import Config
from api.sample.sampleModel import SampleModel
from services.sampleService import SampleService
import datetime

ns = Namespace('Sample',
               description='Operation add model', ordered=True, path="/BookSample")
config = Config()
sampleModel = SampleModel(ns)
postParser = sampleModel.postBook()
sampleSer= SampleService()


@ns.route('/add/Sample')
class SampleController(Resource):
    @ns.doc('Return average_ration of a book')
    @ns.expect(postParser)
    def post(self):
        " prediction average rating of a book"

        data = postParser.parse_args()

        try:
            title=data["title"]
            numPage=data["numPage"]
            ratingCount= data["ratingCount"]
            textReviewCount = data["textReviewCount"]
            author = data["author"]
            languageCode = data["languageCoce"]
            publisher= data["publisher"]
            publicationDate = datetime.strptime(data["publicationDate"],'%Y/%m/%d %H:%M:%S')
            datepos=datetime.datetime.now()
            actualvalue=data["actualvalue"]
            sampleSer.createSample(title, numPage,ratingCount ,textReviewCount,author,languageCode,publisher,publicationDate,datepos,actualvalue)

            return {
                       'message': 'sample dadde',
                       'status': 'success'
                   },201
        except Exception as ex:
            abort(404, str(ex))



