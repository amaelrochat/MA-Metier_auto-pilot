from datetime import datetime
from sqlalchemy import Column, Float, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from src.databases.database import Base


class Command(Base):
    __tablename__ = "commands"

    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime, nullable=False)
    aileron_position = Column(Float)
    rudder_position = Column(Float)
    elevator_position = Column(Float)
    spoiler_position = Column(Float)
    throttle = Column(Float)
    session_id = Column(Integer, ForeignKey("sessions.id"))

    # relation
    Session = relationship("Session", back_populates="Command")

    def __init__(self, **kwargs):
        """Initialize a command instance

        Accepts keyword arguments for all attributes
        """
        self.session_id = kwargs.get("session_id")
        self.aileron_position = kwargs.get("aileron_position")
        self.rudder_position = kwargs.get("rudder_position")
        self.elevator_position = kwargs.get("elevator_position")
        self.spoiler_position = kwargs.get("spoiler_position")
        self.throttle = kwargs.get("throttle")
        self.date_time = datetime.strptime(
            kwargs.get("date_time"), "%Y-%m-%d %H:%M")
