from decimal import Decimal
import datetime
from playhouse.shortcuts import model_to_dict
from daoModels.sample import Sample
from daoModels.model import Model
from utils.serializer import serialization, more
import uuid
import logging
import json
from flask import jsonify


class SampleService:
    """[Sample database service]
    """

    def __init__(self):
        pass



    def createSample(self, title, numPage,ratingCount ,textReviewCount,author,languageCode,publisher,publicationDate,datepos,actualvalue):
        """[create new sample]
        Args:
            name ([str]): [name of the sample]
            description ([str]): [description of the sample]
            contractId ([str]): [the contract id]
        Raises:
            Exception: [failed to create the sample]
        Returns:
            [Sample]: [the created sample]
        """
        try:
            sample = Sample.create(
                sampleId=str(uuid.uuid4()),
                title=title,
                numPgae=numPage,
                rationCoung=ratingCount,
                textReviewCount=textReviewCount,
                author=author,
                languageCode=languageCode,
                publisher=publisher,
                publicationDate=publicationDate,
                datepos=datepos,
                actualvalue=actualvalue
            )
            return sample
        except Exception as ex:
            logging.error(str(ex))
            raise Exception("Failed to create the new Sample")

    def deleteSample(self, sampleId):
        """[delete a sample by id]
        Args:
            sampleId ([str]): [the sample id]
        Raises:
            Exception: [failed to delete the sample]
        Returns:
            [Sample]: [the sample deleted]
        """
        try:
            sample = Sample.get(
                Sample.sampleId == sampleId
            )
            sample.delete_instance(recursive=True)
            return serialization(sample)
        except Exception as ex:
            logging.error(str(ex))
            raise Exception('Failed while deleting the sample')

