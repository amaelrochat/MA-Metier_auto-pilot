from src.services.aircraft_service import AircraftService
import math as Math

def auto_pilot(args):
    heading_degrees = 90

    aircraft_service = AircraftService()

    def maintain_angle(angle_to_maintain):
        current_state = aircraft_service.get_aircraft_state()
        current_angle = current_state['plane_angle']
        angle_difference = -(angle_to_maintain - current_angle)
        aileron_adjustment = angle_difference * 0.5
        aircraft_service.set_aileron_position(aileron_adjustment)

    while True:
        plane_state = aircraft_service.get_aircraft_state()
        print(f"Current angle: {plane_state['plane_angle']}, Heading: {plane_state['heading']}, Altitude: {plane_state['altitude']}, Aileron: {plane_state['aileron_position']}")
        current_heading = plane_state['heading']
        heading_error = heading_degrees - current_heading
        
        if heading_error > 180:
            heading_error -= 360
        elif heading_error < -180:
            heading_error += 360
        
        desired_angle = heading_error * 0.1
        
        maintain_angle(Math.radians(desired_angle))