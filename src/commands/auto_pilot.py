from src.services.aircraft_service import AircraftService

def auto_pilot(args):
    heading_degrees = args[0] if len(args) > 0 else 0
    altitude_feet = args[1] if len(args) > 1 else 5000

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
        maintain_angle(0.5)