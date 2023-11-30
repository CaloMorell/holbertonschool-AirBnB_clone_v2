#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.city import City
import os


class State(BaseModel):
    """ State class """


    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("Ciudad", backref="estado", cascade="all, delete-orphan")


    @property
    def cities(self):
        """Atributo getter para ciudades en FileStorage"""
        city_list = []
        all_cit = models.storage.all(City)
        for city in models.storage.all(models.Ciudad).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
