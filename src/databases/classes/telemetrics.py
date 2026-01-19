from datetime import time
from sqlalchemy import Column, Integer, Time, ForeignKey
from sqlalchemy.orm import relationship
from src.databases.database import Base

class Telemetry(Base):
    __tablename__ = "telemetrics"

    id = Column(Integer, primary_key=True)
    coordonate = Column(Integer, nullable=False)
    altitude = Column(Integer, nullable=False)
    horizontal_speed = Column(Integer, nullable=False)
    vertical_speed = Column(Integer, nullable=False)
    time_since_departure = Column(Time, nullable=False)

    session_id = Column(Integer, ForeignKey("sessions.id"))

    #relation
    Session = relationship("Session", back_populates="Telemetry")

    
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