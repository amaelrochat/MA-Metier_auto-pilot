export class Aircraft {
  altitude: number;
  latitude: number;
  longitude: number;
  ground_altitude: number;
  ground_speed: number;
  plane_angle: number;
  speed: number;
  heading: number;
  throttle: number;
  aileron_position: number;
  rudder_position: number;
  elevator_position: number;
  spoiler_position: number;

  constructor(
    altitude: number,
    latitude: number,
    longitude: number,
    ground_altitude: number,
    ground_speed: number,
    plane_angle: number,
    speed: number,
    heading: number,
    throttle: number,
    aileron_position: number,
    rudder_position: number,
    elevator_position: number,
    spoiler_position: number,
  ) {
    this.altitude = altitude;
    this.latitude = latitude;
    this.longitude = longitude;
    this.ground_altitude = ground_altitude;
    this.speed = speed;
    this.heading = heading;
    this.throttle = throttle;
    this.aileron_position = aileron_position;
    this.rudder_position = rudder_position;
    this.elevator_position = elevator_position;
    this.spoiler_position = spoiler_position;
    this.ground_speed = ground_speed;
    this.plane_angle = plane_angle;
  }

  async setThrottle(throttle: number): Promise<void> {
    await fetch("/api/aircraft", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ throttle }),
    });
    this.throttle = throttle;
  }

  async setControls(aileron: number, elevator: number): Promise<void> {
    await fetch("/api/aircraft", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        aileron_position: aileron,
        elevator_position: elevator,
      }),
    });
    this.aileron_position = aileron;
    this.elevator_position = elevator;
  }

  async setAileronPosition(position: number): Promise<void> {
    await fetch("/api/aircraft", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ aileron_position: position }),
    });
    this.aileron_position = position;
  }

  async setRudderPosition(position: number): Promise<void> {
    await fetch("/api/aircraft", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ rudder_position: position }),
    });
    this.rudder_position = position;
  }

  async setElevatorPosition(position: number): Promise<void> {
    await fetch("/api/aircraft", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ elevator_position: position }),
    });
    this.elevator_position = position;
  }

  async setSpoilerPosition(position: number): Promise<void> {
    await fetch("/api/aircraft", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ spoiler_position: position }),
    });
    this.spoiler_position = position;
  }

  static async current(): Promise<Aircraft> {
    const response = await fetch("/api/aircraft");
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    return new Aircraft(
      data.altitude,
      data.latitude,
      data.longitude,
      data.ground_altitude,
      data.ground_speed,
      data.plane_angle,
      data.speed,
      data.heading,
      data.throttle,
      data.aileron_position,
      data.rudder_position,
      data.elevator_position,
      data.spoiler_position,
    );
  }
}
