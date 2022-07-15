import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    email = Column(String(30), unique = True, nullable=False)
    password = Column(String(30), unique = True, nullable=False)
    subscription_date = Column(Integer, nullable=False)


class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique = True, nullable=False)
    gender = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    vehicles = Column(Integer, nullable=False)
    planet = relationship(User)


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique = True, nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)


class Character_Favorite(Base):
    __tablename__ = 'character_favorite'  
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))

    
class Planet_Favorite(Base):
    __tablename__ = 'planet_favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')