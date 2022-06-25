import json
import os


class Config:
    def __init__(self):
        pass
    def getDataBase(self):
        """[get the database name]
        Returns:
            [str]: [database name]
        """
        db = os.getenv("MYSQL_DATABASE", "PROJECT_DB")
        return db

    def getModelsPath(self):
        """[get the trained model path ]

        """
        modelsPATH = os.getenv("MODEL_DATA_PATH", "./modeldata/")
        return os.path.abspath(modelsPATH)

    def getDBUser(self):
        """[get the database user to connect with]
        Returns:
            [str]: [the mysql user ]
        """
        user = os.getenv("MYSQL_USER", "user")
        return user

    def getDBPassword(self):
        """[get the database password]
        Returns:
            [str]: [the database password]
        """
        password = os.getenv("MYSQL_PASSWORD", "user")
        return password

    def getDBHost(self):
        """[Get the database host]
        Returns:
            [str]: [the database host]
        """
        dbHost = os.getenv("MYSQL_HOST", "0.0.0.0")
        return dbHost

    def getDBPort(self):
        """[Get the database Port]
        Returns:
            [str]: [the database port]
        """
        port = os.getenv("MYSQL_PORT", 3306)
        return int(port)

    def hasSSL(self):
        """[get if SSL mode is enabled]
        Returns:
            [bool]: [if ssl mode is enabled]
        """
        hasSSL = os.getenv("ENABLE_SSL", "false")
        return hasSSL == "true"