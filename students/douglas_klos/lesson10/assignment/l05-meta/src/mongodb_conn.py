"""MondoDB Connection"""

from pymongo import MongoClient


class MongoDBConnection:
    """MongoDB Connection"""

    database_name = "HPNorton_PyMongo_L10"

    def __init__(self, host="127.0.0.1", port=27017):
        """ be sure to use the ip address not name for local windows"""
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        return self.connection.HPNorton_PyMongo_L10

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
