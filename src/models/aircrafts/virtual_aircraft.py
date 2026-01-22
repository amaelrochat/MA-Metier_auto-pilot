from SimConnect import AircraftRequests, SimConnect
from src.models.aircrafts.aircraft_interface import AircraftInterface


class VirtualAircraft(AircraftInterface):
    def __init__(self):
        self._simconnect = SimConnect()
        self._aircraft = AircraftRequests(self._simconnect, _time=2000)

    @property
    def altitude(self) -> float:
        return self._aircraft.get("PLANE_ALTITUDE")

    @property
    def ground_altitude(self) -> float:
        return self._aircraft.get("GROUND_ALTITUDE")
    
    @property
    def ground_speed(self) -> float:
        return self._aircraft.get("GROUND_VELOCITY")

    @property
    def speed(self) -> float:
        return self._aircraft.get("AIRSPEED_INDICATED")

    @property
    def heading(self) -> float:
        return self._aircraft.get("PLANE_HEADING_DEGREES_TRUE")

    @property
    def throttle(self) -> float:
        return self._aircraft.get("GENERAL_ENG_THROTTLE_LEVER_POSITION:1")

    @throttle.setter
    def throttle(self, value: float):
        """Set the throttle setting of the airship."""
        self._aircraft.set("GENERAL_ENG_THROTTLE_LEVER_POSITION:1", value)

    @property
    def aileron_position(self) -> float:
        """Get the current aileron position of the airship."""
        return self._aircraft.get("AILERON_POSITION")

    @aileron_position.setter
    def aileron_position(self, value: float):
        """Set the aileron position of the airship."""
        self._aircraft.set("AILERON_POSITION", value)

    @property
    def rudder_position(self) -> float:
        """Get the current rudder position of the airship."""
        return self._aircraft.get("RUDDER_POSITION")

    @rudder_position.setter
    def rudder_position(self, value: float):
        """Set the rudder position of the airship."""
        self._aircraft.set("RUDDER_POSITION", value)

    @property
    def elevator_position(self) -> float:
        """Get the current elevator position of the airship."""
        return self._aircraft.get("ELEVATOR_POSITION")

    @elevator_position.setter
    def elevator_position(self, value: float):
        """Set the elevator position of the airship."""
        self._aircraft.set("ELEVATOR_POSITION", value)

    @property
    def spoiler_position(self) -> float:
        """Get the current airbrake (spoiler) position of the airship."""
        return self._aircraft.get("SPOILERS_HANDLE_POSITION")

    @spoiler_position.setter
    def spoiler_position(self, value: float):
        """Set the airbrake (spoiler) position of the airship."""
        self._aircraft.set("SPOILERS_HANDLE_POSITION", value)
