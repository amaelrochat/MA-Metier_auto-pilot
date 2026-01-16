from src.models.airships.airship_interface import AirshipInterface


class PilotInterface:
    def __init__(self, airship: AirshipInterface):
        self.airship = airship

    def main(self) -> None:
        """Main entry point for the pilot. Initializes and starts the pilot logic."""
        raise NotImplementedError("Subclasses must implement this method.")

    def loop(self) -> None:
        """Main loop for the pilot to execute its logic."""
        raise NotImplementedError("Subclasses must implement this method.")
