import os
from src.factories.aircraft_factory import AircraftFactory
from src.utils.log_utils import Log


class AircraftService:
    def __init__(self):
        self.aircraft = AircraftFactory.get_aircraft(
            os.getenv("CURRENT_AIRCRAFT", "VirtualAircraft"))
        self.sessions = Log.new_session()

    def get_aircraft_state(self) -> dict:
        self.log_telemetry()
        return self.aircraft.to_array()

    def set_throttle(self, value: float) -> None:
        self.aircraft.throttle = value
        Log.command_entry(
            session_id=self.sessions.id,
            throttle=value
        )

    def set_aileron_position(self, value: float) -> None:
        self.aircraft.aileron_position = value
        Log.command_entry(
            session_id=self.sessions.id,
            aileron=value
        )

    def set_rudder_position(self, value: float) -> None:
        self.aircraft.rudder_position = value
        Log.command_entry(
            session_id=self.sessions.id,
            rudder=value
        )

    def set_elevator_position(self, value: float) -> None:
        self.aircraft.elevator_position = value
        Log.command_entry(
            session_id=self.sessions.id,
            elevator=value
        )

    def set_spoiler_position(self, value: float) -> None:
        self.aircraft.spoiler_position = value
        Log.command_entry(
            session_id=self.sessions.id,
            spoiler=value
        )

    def log_telemetry(self) -> None:
        Log.telemetry_entry(
            session_id=self.sessions.id,
            altitude=self.aircraft.altitude,
            ground_altitude=self.aircraft.ground_altitude,
            speed=self.aircraft.speed,
            ground_speed=self.aircraft.ground_speed,
            heading=self.aircraft.heading,
            latitude=self.aircraft.latitude,
            longitude=self.aircraft.longitude,
            plane_angle=self.aircraft.plane_angle
        )
