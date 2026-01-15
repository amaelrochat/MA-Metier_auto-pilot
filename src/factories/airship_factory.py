from src.models.airships.virtual_airship import VirtualAirship


class AirshipFactory:
    @staticmethod
    def get_airship(airship_type):
        switcher = {
            "VirtualAirship": VirtualAirship(),
        }
        return switcher.get(airship_type, None)
