"""
    Create database examle with Peewee ORM, sqlite and Python
"""
from personjob_modeli import *
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


from personjob_modeli import *

logger.info('One off program to build the classes from the model in the database')
database.create_tables([
        Job,

        Person,

        PersonNumKey,

        Department

    ]) #TODO: Might have to edit this for activity

database.close()