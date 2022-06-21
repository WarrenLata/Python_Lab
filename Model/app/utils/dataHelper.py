from daoModels.baseModel import database
from daoModels.model import Model
from daoModels.sample import Sample
# simple utility function to create tables


def create_tables():
    """[Create tables]
    """
    with database:
        database.create_tables([Model,Sample])
    return database