class AircraftFactory:
    @staticmethod
    def get_aircraft(aircraft_type: str):
        match aircraft_type:
            case "VirtualAircraft":
                from src.models.aircrafts.virtual_aircraft import VirtualAircraft
                return VirtualAircraft()
            case "FakeAircraft":
                from src.models.aircrafts.fake_aircraft import FakeAircraft
                return FakeAircraft()
            case _:
                raise ValueError(f"Unknown aircraft type: {aircraft_type}")
