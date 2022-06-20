from daoModels.model import Model
from daoModels.sample import Sample
import uuid
from playhouse.shortcuts import model_to_dict
import logging
from utils.serializer import serialization, more


class ModelService:
    def __init__(self):
        pass

    def createModel(self, name,description):
        """[Create a new model in the DB]
        Args:
            name ([type]): [name of model]
            epochs ([type]): [One Epoch is when an ENTIRE dataset is passed forward and backward through the neural network only ONCE]
            description ([type]): [description of Model]
            contractId ([type]): [the contract id]
        Raises:
            Exception: [Failed to create the Model]
        Returns:
            [type]: [the model created]
        """
        try:
            model = Model.create(
                modelId=str(uuid.uuid4()),
                name=name,
                description=description
            )
            return serialization(model)
        except:
            raise Exception("Failed to create the new model")


    def add_sample(self, sampleId):
        """[Add sample to an existing model]
        Args:
            sampleId ([str]): [sample Id]
        Raises:
            Exception: [Failed to add a sample to the model]
        Returns:
            [ModelSamples]: []
        """
        try:
            sample = Sample.get(
                (Sample.sampleId == sampleId)
            )
            modelSamples = ModelSamples.create(
                sample=sample
            )
            return modelSamples
        except Exception as ex:
            logging.error(str(ex))
            raise Exception("Failed to create the new model_sample")


    def updateModel(self, modelId, **kwargs):
        """[update a model]
        Args:
            modelId ([str]): [Model Id]
        Raises:
            Exception: [Failed to update the model]
        """
        try:
            res = Model.update(kwargs).where(
                Model.modelId == modelId).execute()
        except Exception as ex:
            logging.error(str(ex))
            raise Exception('Failed while updating the model status')

    def getModelById(self, modelId):
        """[get a model by Id]
        Args:
            modelId ([type]): [model id]
        Raises:
            Exception: [Failed to get the model by id]
        Returns:
            [Model]: [The  model correspand to the given Id]
        """
        try:
            model = Model.get(
                (Model.modelId == modelId)
            )
            return serialization(model)
        except:
            raise Exception('Model doesn\'t exist')

