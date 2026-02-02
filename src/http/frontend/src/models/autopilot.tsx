export class Autopilot {
  enabled: boolean;
  altitude: number;
  speed: number;
  heading: number;

  constructor(
    enabled: boolean,
    altitude: number,
    speed: number,
    heading: number,
  ) {
    this.enabled = enabled;
    this.altitude = altitude;
    this.speed = speed;
    this.heading = heading;
  }

  static async current(): Promise<Autopilot> {
    const response = await fetch("/api/aircraft/autopilot");

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const data = await response.json();
    return new Autopilot(data.enabled, data.altitude, data.speed, data.heading);
  }

  async setAltitude(altitude: number): Promise<void> {
    await fetch("/api/aircraft/autopilot", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ altitude }),
    });
    this.altitude = altitude;
  }

  async setSpeed(speed: number): Promise<void> {
    await fetch("/api/aircraft/autopilot", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ speed }),
    });
    this.speed = speed;
  }

  async setHeading(heading: number): Promise<void> {
    await fetch("/api/aircraft/autopilot", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ heading }),
    });
    this.heading = heading;
  }

  async toggle(enabled: boolean): Promise<void> {
    await fetch("/api/aircraft/autopilot", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ enabled }),
    });
    this.enabled = enabled;
  }
}
