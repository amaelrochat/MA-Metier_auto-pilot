from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from src.databases.database import Base


class Telemetry(Base):
    __tablename__ = "telemetrics"

    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime, nullable=False)
    altitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    ground_altitude = Column(Float, nullable=False)
    speed = Column(Float, nullable=False)
    ground_speed = Column(Float, nullable=False)
    heading = Column(Float, nullable=False)
    plane_angle = Column(Float, nullable=True)
    angle_of_attack = Column(Float, nullable=True)

    session_id = Column(Integer, ForeignKey("sessions.id"))

    # relation
    Session = relationship("Session", back_populates="Telemetry")

    def __init__(self, **kwargs):
        """Initialize a telemetry instance

        Accepts keyword arguments for all attributes
        """
        self.date_time = datetime.strptime(
            kwargs.get("date_time"), "%Y-%m-%d %H:%M")
        self.altitude = kwargs.get("altitude")
        self.ground_altitude = kwargs.get("ground_altitude")
        self.ground_speed = kwargs.get("ground_speed")
        self.speed = kwargs.get("speed")
        self.heading = kwargs.get("heading")
        self.session_id = kwargs.get("session_id")
        self.latitude = kwargs.get("latitude")
        self.longitude = kwargs.get("longitude")
        self.plane_angle = kwargs.get("plane_angle")
        self.angle_of_attack = kwargs.get("angle_of_attack")
