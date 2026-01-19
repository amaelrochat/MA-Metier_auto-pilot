class AirshipInterface:
    @property
    def altitude(self) -> float:
        """Get the current altitude of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")

    @property
    def ground_altitude(self) -> float:
        """Get the current altitude above ground of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")

    @property
    def speed(self) -> float:
        """Get the current speed of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")

    @property
    def heading(self) -> float:
        raise NotImplementedError("Subclasses must implement this method.")

    @property
    def throttle(self) -> float:
        """Get the current throttle setting of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")

    @throttle.setter
    def throttle(self, value: float):
        """Set the throttle setting of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")

    @property
    def aileron_position(self) -> float:
        """Get the current aileron position of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")

    @aileron_position.setter
    def aileron_position(self, value: float):
        """Set the aileron position of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")

    @property
    def rudder_position(self) -> float:
        """Get the current rudder position of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")

    @rudder_position.setter
    def rudder_position(self, value: float):
        """Set the rudder position of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")

    @property
    def elevator_position(self) -> float:
        """Get the current elevator position of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")

    @elevator_position.setter
    def elevator_position(self, value: float):
        """Set the elevator position of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")

    @property
    def spoiler_position(self) -> float:
        """Get the current airbrake (spoiler) position of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")

    @spoiler_position.setter
    def spoiler_position(self, value: float):
        """Set the airbrake (spoiler) position of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")
