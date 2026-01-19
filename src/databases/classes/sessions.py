from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from src.databases.database import Base


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime, nullable=False)
    glider_model = Column(String, nullable=False)
    takeoff_location = Column(String, nullable=False)

    # relations
    Telemetry = relationship("Telemetry", back_populates="Session")
    Command = relationship("Command", back_populates="Session")

    def __init__(self, **kwargs):
        """Initialize a session instance

        Accepts keyword arguments for all attributes
        """
        self.date_time = datetime.strptime(kwargs.get("date_time"), "%Y-%m-%d %H:%M")
        self.glider_model = kwargs.get("glider_model")
        self.takeoff_location = kwargs.get("takeoff_location")
