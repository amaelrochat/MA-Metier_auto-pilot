from src.services.aircraft_service import AircraftService
from src.utils.auto_pilot_utils import AutoPilotUtils


def auto_pilot(args):
    aircraft_service = AircraftService()
    heading = float(args[0]) if len(args) > 0 else 0
    speed = float(args[1]) if len(args) > 1 else 70
    altitude = float(args[2]) if len(args) > 2 else 10000

    while True:
        AutoPilotUtils.maintain_heading(aircraft_service, heading)
        AutoPilotUtils.maintain_speed(aircraft_service, speed)
        AutoPilotUtils.maintain_altitude(aircraft_service, altitude)
