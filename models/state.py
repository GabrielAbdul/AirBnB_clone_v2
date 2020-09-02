#!/usr/bin/python3
""" State Module for HBNB project """

from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all, delete", backref='state')
    else:
        name = ''

        @property
        def cities(self):
            ''' cities getter '''
            from models.engine.file_storage import FileStorage
            ret = []
            for n, city in FileStorage.all(City).items():
                if 'City' in n and city.state_id == self.id:
                    ret.append(City)
            return ret
