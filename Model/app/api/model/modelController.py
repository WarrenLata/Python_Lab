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




class ModelController:

    @ns.doc('Return average_ration of a book')
    @ns.expect(postParser)
    def post(self):
        " prediction average rating of a book"

        data = postParser.parse_args()

        try:
            result = 0
            if (data["ratings_cout"] != 0 and data["num_page"] != 0 and data["text_review_count"] != 0):
                modelPath = config.getModelsPath()
                result = chosen.predict(data["author"], data["num_page"], data["ratings_cout"],
                                        data["text_review_count"],
                                        data["publisher"])

            return result
        except Exception as ex:
            abort(404, str(ex))

    @ns.route('/contract/<contractId>/model/upload')
    @ns.param('contractId', 'The Contract Id')
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

                    # save model informations in DB
                    newModel = modelService.createModel(
                        name, epochs, description, contractId, category)

                    # create temporary file
                    tmpFile = os.path.join(config.getTmpTrainDataPath(), "my-temp-model.zip")
                    file.save(tmpFile)

                    # create directory to store the new model

                    # get the path of the output dir
                    export_dir = os.path.join(
                        config.getModelsPath(category), newModel["modelId"])
                    if os.path.exists(export_dir):
                        raise Exception(
                            "A model with the same name {0} already exists".format(self.modelId))
                    else:
                        os.mkdir(export_dir)

                    # unzip the temporary file in the export directory
                    shutil.unpack_archive(tmpFile, export_dir)

                    # remove the file after download
                    io.removeFile(tmpFile)

                    # rename the model file to modelId
                    oldFileName = os.path.join(export_dir, "model")
                    newFileName = os.path.join(export_dir, newModel["modelId"])
                    os.rename(oldFileName, newFileName)

                    # update status
                    modelService.updateModel(
                        newModel["modelId"], status="finished", stopedAt=datetime.datetime.now())

                    return {
                               'message': 'file uploaded',
                               'status': 'success'
                           }, 201
            except Exception as ex:
                abort(500, str(ex))