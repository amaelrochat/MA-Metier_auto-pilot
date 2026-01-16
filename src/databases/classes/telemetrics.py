"""
Program name : telemetrics.py
Date : 15.01.2026
Edit : 15.01.2026
Description : Class model of a telemetry for the ORM
Version : V 0.1
"""

from datetime import time
from sqlalchemy import Column, Integer, Time, ForeignKey
from sqlalchemy.orm import relationship
from src.databases.database import Base

class telemetrics(Base):
    __tablename__ = "telemetrics"

    id = Column(Integer, primary_key=True)
    coordonate = Column(Integer, nullable=False)
    altitude = Column(Integer, nullable=False)
    horizontal_speed = Column(Integer, nullable=False)
    vertical_speed = Column(Integer, nullable=False)
    time_since_departure = Column(Time, nullable=False)

    session_id = Column(Integer, ForeignKey("sessions.id"))

    #relation
    session = relationship("sessions", back_populates="telemetry")

    
    def __init__(self, **kwargs):
        """
        Initialize a telemetry instance
        Accepts keyword arguments for all attributes
        """
        self.coordonate = kwargs.get("coordonate")
        self.altitude = kwargs.get("altitude")
        self.horizontal_speed = kwargs.get("horizontal_speed")
        self.vertical_speed = kwargs.get("vertical_speed")
        self.time_since_departure = time.strptime(kwargs.get("time_since_departure"), "%H:%M")
        self.session_id = kwargs.get("session_id")