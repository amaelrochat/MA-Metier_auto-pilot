class AircraftInterface:
    @property
    def altitude(self) -> float:
        """Get the current altitude of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")

    @property
    def latitude(self) -> float:
        """Get the current latitude of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")

    @property
    def longitude(self) -> float:
        """Get the current longitude of the airship."""
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
    def plane_angle(self) -> float:
        """Get the current plane angle of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")

    @property
    def angle_of_attack(self) -> float:
        """Get the current angle of attack of the airship."""
        raise NotImplementedError("Subclasses must implement this method.")

    @property
    def ground_speed(self) -> float:
        """Get the current ground speed of the airship."""
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

    def to_array(self) -> dict:
        return {
            "altitude": self.altitude,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "ground_altitude": self.ground_altitude,
            "ground_speed": self.ground_speed,
            "speed": self.speed,
            "heading": self.heading,
            "throttle": self.throttle,
            "aileron_position": self.aileron_position,
            "rudder_position": self.rudder_position,
            "elevator_position": self.elevator_position,
            "spoiler_position": self.spoiler_position,
            "plane_angle": self.plane_angle,
            "angle_of_attack": self.angle_of_attack,
        }
