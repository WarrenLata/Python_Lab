from daoModels.baseModel import BaseModel
from peewee import CharField, UUIDField, TextField, DateTimeField, ForeignKeyField, IntegerField,FloatField
import datetime


# the model entity specifies its fields (or columns) declaratively, like django


class Sample(BaseModel):
    """[Model book real value]
    Args:
        BaseModel ([Model]): [the peewee base model]
    """
    sampleId = CharField(primary_key=True)
    title = CharField()
    numPage = IntegerField(default=100)
    ratingCount = IntegerField(default=100)
    textReviewCount = IntegerField(default=100)
    author = CharField()
    languageCode=charFiedl()
    publisher = CharField()
    publicationDate = DateTimeField(null=True)
    datepos = DateTimeField(default=datetime.datetime.now)
    actualvalue=FloatField()

    class Meta:
        """[Meta informatins]
        """
        # the name of table in the database
        table_name = 'Sample'