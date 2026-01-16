from src.models.pilots.starter_pilot import StarterPilot


class PilotFactory:
    @staticmethod
    def get_pilot(pilot_type, *args, **kwargs):
        switcher = {
            "StarterPilot": StarterPilot(*args, **kwargs),
        }
        return switcher.get(pilot_type, None)
