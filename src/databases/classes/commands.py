from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.databases.database import Base

class Command(Base):
    __tablename__ = "commands"

    id = Column(Integer, primary_key=True)
    x_handle = Column(Integer, nullable=False)
    y_handle = Column(Integer, nullable=False)
    crossbar = Column(Integer, nullable=False)

    session_id = Column(Integer, ForeignKey("sessions.id"))

    #relation
    Session = relationship("Session", back_populates="Command")

    
    def __init__(self, **kwargs):
        """
        Initialize a command instance
        Accepts keyword arguments for all attributes
        """
        self.x_handle = kwargs.get("x_handle")
        self.y_handle = kwargs.get("y_handle")
        self.crossbar = kwargs.get("crossbar")
        self.session_id = kwargs.get("session_id")