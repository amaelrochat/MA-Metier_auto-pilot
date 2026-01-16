"""
Program name : commands.py
Date : 15.01.2026
Edit : 15.01.2026
Description : Class model of a command for the ORM
Version : V 0.1
"""

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class commands(Base):
    __tablename__ = "commands"

    id = Column(Integer, primary_key=True)
    x_handle = Column(Integer, nullable=False)
    y_handle = Column(Integer, nullable=False)
    crossbar = Column(Integer, nullable=False)

    session_id = Column(Integer, ForeignKey("sessions.id"))

    #relation
    session = relationship("sessions", back_populates="command")

    
    def __init__(self, **kwargs):
        """
        Initialize a command instance
        Accepts keyword arguments for all attributes
        """
        self.x_handle = kwargs.get("x_handle")
        self.y_handle = kwargs.get("y_handle")
        self.crossbar = kwargs.get("crossbar")
        self.session_id = kwargs.get("session_id")