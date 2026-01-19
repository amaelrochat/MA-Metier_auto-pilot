from src.models.pilots.pilot_interface import PilotInterface
from SimConnect import AircraftRequests, SimConnect

class shipGoInCircle(PilotInterface):
    def __init__(self, airship: AircraftRequests):
        self.airship = airship

    def execute(self):
