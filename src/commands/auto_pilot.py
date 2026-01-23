from src.services.aircraft_service import AircraftService


def auto_pilot(args):
    heading_degrees = args[0] if len(args) > 0 else 0
    altitude_feet = args[1] if len(args) > 1 else 5000

    aircraft_service = AircraftService()

    while True:
        current_state = aircraft_service.get_aircraft_state()

        print(
            f"Maintaining heading {heading_degrees}° and altitude {altitude_feet} ft.")
        print(
            f"Current State: {current_state}"
        )

        # Simple control logic (placeholder for real autopilot algorithms)
        if current_state["heading"] < heading_degrees:
            aircraft_service.set_aileron_position(0.05)  # Turn right
        elif current_state["heading"] > heading_degrees:
            aircraft_service.set_aileron_position(-0.05)  # Turn left
        else:
            aircraft_service.set_aileron_position(0.0)  # Straighten wings

        if current_state["altitude"] < altitude_feet:
            aircraft_service.set_elevator_position(0.05)  # Climb
            aircraft_service.set_throttle(100)  # Increase throttle
        elif current_state["altitude"] > altitude_feet:
            aircraft_service.set_elevator_position(-0.05)  # Descend
            aircraft_service.set_throttle(30)  # Decrease throttle
        else:
            aircraft_service.set_elevator_position(0.0)  # Level off
            aircraft_service.set_throttle(60)  # Maintain throttle
