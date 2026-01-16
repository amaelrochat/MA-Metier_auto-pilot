class AirshipInterface:
    @property
    def altitude(self) -> float:
        """Get the current altitude of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")

    @property
    def speed(self) -> float:
        """Get the current speed of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")
