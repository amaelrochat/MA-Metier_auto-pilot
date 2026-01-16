"""
Program name : sessions.py
Date : 15.01.2026
Edit : 15.01.2026
Description : Class model of a session for the ORM
Version : V 0.1
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DATETIME
from sqlalchemy.orm import relationship
from database import Base

class sessions(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    date_time = Column(DATETIME, nullable=False)
    glider_model = Column(String, nullable=False)
    takeoff_location = Column(String, nullable=False)

    #relations
    telemetry = relationship("telemetrics", back_populates="session")
    command = relationship("commands", back_populates="session")


    def __init__(self, **kwargs):
        """
        Initialize a session instance
        Accepts keyword arguments for all attributes
        """
        self.date_time = datetime.strptime(kwargs.get("date_time"), "%d.%m.%Y %H:%M")
        self.glider_model = kwargs.get("glider_model")
        self.takeoff_location = kwargs.get("takeoff_location")