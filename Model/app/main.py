import os
from flask import Flask
from flask_restx import Api

# logs Config
from api.model.modelController import ns as PredictorNameSpace
from api.sample.sampleController import ns as AddNewDataNamespace
from logging.config import dictConfig
from utils.DAOHelper import create_tables
dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'root': {
        'level': os.getenv('URBA_BOT_LOG_LEVEL', "WARNING"),
        'handlers': ['wsgi']
    }

})
app = Flask(__name__)
api = Api(title='Prediction API',
          version='1.0',
          description='This APi handle predictions operation',)

# create if not exist
database = create_tables()
# This hook ensures that a connection is opened to handle any queries
# generated by the request.
@app.before_request
def _db_connect():
    database.connect()

# This hook ensures that the connection is closed when we've finished
# processing the request.
@app.teardown_request
def _db_close(exc):
    if not database.is_closed():
        database.close()


@app.teardown_appcontext
def close_database(error):
    if not database.is_closed():
        database.close()


app.config.setdefault('RESTX_MASK_HEADER', False)
app.config.setdefault('RESTPLUS_MASK_SWAGGER', False)
api.add_namespace(PredictorNameSpace)
api.add_namespace(AddNewDataNamespace)

api.init_app(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)