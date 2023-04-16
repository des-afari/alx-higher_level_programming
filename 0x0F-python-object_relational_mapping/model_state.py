#!/usr/bin/python3
"""First state model"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """State class inheriting from Base"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, id, name){
        self.id = id
        self.name = name
    }
