from src.factories.airship_factory import AirshipFactory
from src.factories.pilot_factory import PilotFactory


def default():
    airship = AirshipFactory.get_airship("VirtualAirship")
    pilot = PilotFactory.get_pilot("StarterPilot", airship)

    pilot.main()

    while True:
        pilot.loop()
