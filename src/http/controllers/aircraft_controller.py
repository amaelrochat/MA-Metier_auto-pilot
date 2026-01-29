import asyncio
from fastapi import APIRouter

from src.services.aircraft_service import AircraftService
from src.utils.auto_pilot_utils import AutoPilotUtils

from fastapi import BackgroundTasks


router = APIRouter(prefix="/aircraft")

aircraft_service = AircraftService()

autopilot_status = False
heading = 0
speed = 70
altitude = 10000


async def autopilot():
    global autopilot_status, heading, speed, altitude
    while autopilot_status:
        AutoPilotUtils.maintain_heading(aircraft_service, heading)
        AutoPilotUtils.maintain_speed(aircraft_service, speed)
        AutoPilotUtils.maintain_altitude(aircraft_service, altitude)
        await asyncio.sleep(0.05)


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


@router.get("/autopilot")
async def get_autopilot_status():
    return {"enabled": autopilot_status, "heading": heading, "speed": speed, "altitude": altitude}


@router.post("/autopilot")
async def set_autopilot(controls: dict, background_tasks: BackgroundTasks):
    global autopilot_status, heading, speed, altitude
    autopilot_status = controls.get("enabled", autopilot_status)
    heading = controls.get("heading", heading)
    speed = controls.get("speed", speed)
    altitude = controls.get("altitude", altitude)
    if controls.get("enabled", False):
        background_tasks.add_task(autopilot)
    return {"enabled": autopilot_status, "heading": heading, "speed": speed, "altitude": altitude}
