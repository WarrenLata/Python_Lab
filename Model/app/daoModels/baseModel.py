from peewee import MySQLDatabase, Model
from configUtil.config import Config
# Connect to a MySQL database on network.
config = Config()
if not config.hasSSL() :
    database = MySQLDatabase(config.getDataBase(), user=config.getDBUser(), password=config.getDBPassword(),
                         host=config.getDBHost(), port=config.getDBPort())
### if you have a certifcate
else:
    database = MySQLDatabase(config.getDataBase(), user=config.getDBUser(), password=config.getDBPassword(),
                         host=config.getDBHost(), port=config.getDBPort(),
                         ssl={'ca': '/app/BaltimoreCyberTrustRoot.crt.pem'})


class BaseModel(Model):
    """[The base Model of DB]
    Args:
        Model ([Model]): []
    """
    class Meta:
        database = database