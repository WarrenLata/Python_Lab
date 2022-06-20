from daoModels.baseModel import database
from daoModels.model import Model
from daoModels.modelTrack import ModelTrack
# simple utility function to create tables


def create_tables():
    """[Create tables]
    """
    with database:
        database.create_tables([Model])
    return database