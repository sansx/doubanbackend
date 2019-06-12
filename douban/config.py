import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://xiath:a88869321@192.168.1.103/test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False