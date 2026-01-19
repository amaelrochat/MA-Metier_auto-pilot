from time import sleep
from src.models.pilots.pilot_interface import PilotInterface


class StarterPilot(PilotInterface):
    def main(self) -> None:
        print("StarterPilot main method executed.")

    def loop(self) -> None:
        print("Current airship altitude:", self.airship.altitude)
        print("Current airship ground altitude:", self.airship.ground_altitude)
        print("Current airship speed:", self.airship.speed)
        print("Current airship throttle:", self.airship.throttle)
        print("Current aileron position:", self.airship.aileron_position)
        print("Current rudder position:", self.airship.rudder_position)
        print("Current elevator position:", self.airship.elevator_position)
        print("Current airbrake position:", self.airship.spoiler_position)
        sleep(1)
