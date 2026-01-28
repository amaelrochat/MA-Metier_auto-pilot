from src.services.aircraft_service import AircraftService
from src.utils.auto_pilot_utils import AutoPilotUtils


def auto_pilot(args):
    aircraft_service = AircraftService()

    while True:
        # AutoPilotUtils.maintain_heading(aircraft_service, 90)
        AutoPilotUtils.maintain_speed(aircraft_service, 45)
