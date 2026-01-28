import math as Math
from src.services.aircraft_service import AircraftService


class AutoPilotUtils:
    @staticmethod
    def maintain_angle(aircraft_service: AircraftService, angle_to_maintain: float):
        current_state = aircraft_service.get_aircraft_state()
        current_angle = current_state['plane_angle']
        angle_difference = -(angle_to_maintain - current_angle)
        aileron_adjustment = angle_difference * 0.5
        aircraft_service.set_aileron_position(aileron_adjustment)

    @staticmethod
    def maintain_heading(aircraft_service: AircraftService, heading_degrees: float):
        plane_state = aircraft_service.get_aircraft_state()
        current_heading = plane_state['heading']
        heading_error = heading_degrees - current_heading

        if heading_error > 180:
            heading_error -= 360
        elif heading_error < -180:
            heading_error += 360

        desired_angle = -(heading_error * 0.5)

        AutoPilotUtils.maintain_angle(
            aircraft_service, Math.radians(desired_angle))

    @staticmethod
    def maintain_speed(aircraft_service: AircraftService, speed_to_maintain: float):
        plane_state = aircraft_service.get_aircraft_state()
        current_speed = plane_state['speed']
        speed_error = speed_to_maintain - current_speed

        elevator_adjustment = max(-0.2, min(0.2, -(speed_error * 0.01)))
        aircraft_service.set_elevator_position(elevator_adjustment)
