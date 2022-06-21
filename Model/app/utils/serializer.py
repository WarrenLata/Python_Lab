from decimal import Decimal
import datetime
from playhouse.shortcuts import model_to_dict
import json
try:
    import uuid
    _use_uuid = True
except ImportError:
    _use_uuid = False

datetime_format = "%Y/%m/%d %H:%M:%S"
date_format = "%Y/%m/%d"
time_format = "%H:%M:%S"


def more(obj):
    if isinstance(obj, Decimal):
        return str(obj)

    if isinstance(obj, datetime.datetime):
        return obj.strftime(datetime_format)

    if isinstance(obj, datetime.date):
        return obj.strftime(date_format)

    if isinstance(obj, datetime.time):
        return obj.strftime(time_format)

    if _use_uuid and isinstance(obj, uuid.UUID):
        return str(obj.db_value())

    raise TypeError("%r is not JSON serializable" % obj)


def serialization(model, backrefs=False, recurse=True, max_depth=2):
    preparedModel = model_to_dict(
        model, backrefs=backrefs, recurse=recurse, max_depth=max_depth)
    return json.loads(json.dumps(preparedModel, default=more))