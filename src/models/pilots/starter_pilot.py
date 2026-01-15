from time import sleep
from src.models.pilots.pilot_interface import PilotInterface


class StarterPilot(PilotInterface):
    def main(self) -> None:
        print("StarterPilot main method executed.")

    def loop(self) -> None:
        print("Current airship altitude:", self.airship.altitude)
        print("Current airship speed:", self.airship.speed)
        sleep(1)
