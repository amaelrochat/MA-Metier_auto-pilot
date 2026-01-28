from datetime import datetime

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

    # relation
    Session = relationship("Session", back_populates="Telemetry")

    def __init__(self, **kwargs):
        """Initialize a telemetry instance

        Accepts keyword arguments for all attributes
        """
        self.coordonate = kwargs.get("coordonate")
        self.altitude = kwargs.get("altitude")
        self.ground_altitude = kwargs.get("ground_altitude")
        self.ground_speed = kwargs.get("ground_speed")
        self.speed = kwargs.get("speed")
        self.heading = kwargs.get("heading")
        self.session_id = kwargs.get("session_id")
        self.latitude = kwargs.get("latitude")
        self.longitude = kwargs.get("longitude")
        self.plane_angle = kwargs.get("plane_angle")
