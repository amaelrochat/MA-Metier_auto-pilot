from SimConnect import AircraftRequests, SimConnect
from src.models.airships.airship_interface import AirshipInterface

class VirtualAirship(AirshipInterface):
    def __init__(self):
        self._simconnect = SimConnect()
        self._aircraft = AircraftRequests(self._simconnect, _time=2000)

    @property
    def altitude(self) -> float:
        return self._aircraft.get("PLANE_ALTITUDE")

    @property
    def speed(self) -> float:
        return self._aircraft.get("AIRSPEED_INDICATED")
