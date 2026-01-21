import os
from fastapi import APIRouter

from src.factories.aircraft_factory import AircraftFactory


router = APIRouter(prefix="/aircraft")

aircraft = AircraftFactory.get_aircraft(
    os.getenv("CURRENT_AIRCRAFT", "VirtualAircraft"))


@router.get("")
async def get_aircraft_info():
    return aircraft.to_array()


@router.post("")
async def set_aircraft_controls(controls: dict):
    if "throttle" in controls:
        aircraft.throttle = controls["throttle"]
    if "aileron_position" in controls:
        aircraft.aileron_position = controls["aileron_position"]
    if "rudder_position" in controls:
        aircraft.rudder_position = controls["rudder_position"]
    if "elevator_position" in controls:
        aircraft.elevator_position = controls["elevator_position"]
    if "spoiler_position" in controls:
        aircraft.spoiler_position = controls["spoiler_position"]
    return {"status": aircraft.to_array()}
