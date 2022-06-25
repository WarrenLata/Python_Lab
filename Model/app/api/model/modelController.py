from flask_restx import Resource, reqparse, Namespace, fields
from flask import abort
import os
import shutil
import werkzeug
from flask import send_file
from werkzeug.datastructures import FileStorage
from configUtil.config import Config
from api.model.models import Models
from core.chosenModel import ChosenModel
import datetime

ns = Namespace('model',
               description='Chosen model related operations', ordered=True, path="/training")
config = Config()
methodsParamsModel = Models(ns)
postParser = methodsParamsModel.postModel()
uploadModelParser = methodsParamsModel.uploadModelParser()

chosen=ChosenModel()




@ns.route('/train/model/predic')
class ModelController(Resource):

    @ns.doc('Return average_ration of a book')
    @ns.expect(postParser)
    def post(self):
        " prediction average rating of a book"

        data = postParser.parse_args()

        try:
            result = 0
            if (data["ratingCount"] != 0 and data["numPage"] != 0 and data["textReviewCount"] != 0):
                result = chosen.predict(data["author"], data["numPage"], data["ratingCount"],
                                        data["textReviewCount"],
                                        data["publisher"])


            return result
        except Exception as ex:
            abort(404, str(ex))

@ns.route('/train/model/upload')
@ns.param('file', '')
@ns.response(500, 'When upload fails.')
@ns.response(201, 'When upload Succeeds.')
class ModelUploadController(Resource):

    @ns.doc("Upload local pretrained model")
    @ns.expect(uploadModelParser)
    def post(self):
        """[Upload local pretrained model]
        """
        data = uploadModelParser.parse_args()
        file = data['file']
        try:
            if file:
                    # default value
                name = "default"
                description = ""
                if "name" in data:
                    name = data['name']
                if "description" in data:
                    description = data["description"]



                    return {
                               'message': 'file uploaded',
                               'status': 'success'
                           }, 201
        except Exception as ex:
            abort(500, str(ex))