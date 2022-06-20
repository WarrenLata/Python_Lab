from daoModels.baseModel import BaseModel
from peewee import CharField, UUIDField, TextField, DateTimeField, ForeignKeyField, IntegerField
import datetime


# the model entity specifies its fields (or columns) declaratively, like django


class Model(BaseModel):
    """[Model book]
    Args:
        BaseModel ([Model]): [the peewee base model]
    """
    modelId = CharField(primary_key=True)
    name = CharField()

    description = CharField()


    class Meta:
        """[Meta informatins]
        """
        # the name of table in the database
        table_name = 'model'