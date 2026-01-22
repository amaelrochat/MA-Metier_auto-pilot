from src.models.aircrafts.aircraft_interface import AircraftInterface


class FakeAircraft(AircraftInterface):
    """Fake implementation of AircraftInterface for testing purposes."""

    def __init__(self):
        self._altitude = 1000.0
        self._ground_altitude = 100.0
        self._speed = 150.0
        self._heading = 0.0
        self._throttle = 0.5
        self._aileron_position = 0.0
        self._rudder_position = 0.0
        self._elevator_position = 0.0
        self._spoiler_position = 0.0

    @property
    def altitude(self) -> float:
        return self._altitude

    @property
    def ground_altitude(self) -> float:
        return self._ground_altitude

    @property
    def ground_speed(self) -> float:
        # Dummy calculation
        return self._speed - (self._altitude - self._ground_altitude) * 0.01

    @property
    def speed(self) -> float:
        return self._speed

    @property
    def heading(self) -> float:
        return self._heading

    @property
    def throttle(self) -> float:
        return self._throttle

    @throttle.setter
    def throttle(self, value: float):
        self._throttle = value

    @property
    def aileron_position(self) -> float:
        return self._aileron_position

    @aileron_position.setter
    def aileron_position(self, value: float):
        self._aileron_position = value

    @property
    def rudder_position(self) -> float:
        return self._rudder_position

    @rudder_position.setter
    def rudder_position(self, value: float):
        self._rudder_position = value

    @property
    def elevator_position(self) -> float:
        return self._elevator_position

    @elevator_position.setter
    def elevator_position(self, value: float):
        self._elevator_position = value

    @property
    def spoiler_position(self) -> float:
        return self._spoiler_position

    @spoiler_position.setter
    def spoiler_position(self, value: float):
        self._spoiler_position = value
