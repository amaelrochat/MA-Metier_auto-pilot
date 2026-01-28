from fastapi import APIRouter

from src.services.aircraft_service import AircraftService


router = APIRouter(prefix="/aircraft")

aircraft_service = AircraftService()


@router.get("")
async def get_aircraft_info():
    return aircraft_service.get_aircraft_state()


@router.post("")
async def set_aircraft_controls(controls: dict):
    if "throttle" in controls:
        aircraft_service.set_throttle(controls["throttle"])
    if "aileron_position" in controls:
        aircraft_service.set_aileron_position(controls["aileron_position"])
    if "rudder_position" in controls:
        aircraft_service.set_rudder_position(controls["rudder_position"])
    if "elevator_position" in controls:
        aircraft_service.set_elevator_position(controls["elevator_position"])
    if "spoiler_position" in controls:
        aircraft_service.set_spoiler_position(controls["spoiler_position"])
    return aircraft_service.get_aircraft_state()
