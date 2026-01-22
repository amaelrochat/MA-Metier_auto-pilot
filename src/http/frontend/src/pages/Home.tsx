import { Joystick } from "../components/joystick";
import { useEffect, useState } from "react";
import { Aircraft } from "../models/aircraft";
import Dashboard from "../components/dashboard";
import { Lever } from "../components/lever";
import RudderController from "../components/rudder-controller";


export default function Home() {
  const [aircraft, setAircraft] = useState<Aircraft | null>(null);

  async function fetchAircraft() {
    try {
      const currentAircraft = await Aircraft.current();
      setAircraft(currentAircraft);
    } catch (error) {
      console.error("Failed to fetch aircraft data:", error);
    }
  }

  useEffect(() => {
    (async () => {
      await fetchAircraft();
    })();

    const interval = setInterval(() => {
      fetchAircraft();
    }, 2000);

    return () => clearInterval(interval);
  }, []);

  const onJoystickMove = async (state: { x: number; y: number }) => {
    await aircraft?.setControls(state.x, state.y);
  };

  const onJoystickRelease = async () => {
    await aircraft?.setControls(0, 0);
  }

  if (!aircraft) {
    return (
      <div className="container mx-auto px-4 py-8 flex flex-col items-center justify-center">
      <div className="flex flex-col items-center gap-4">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
        <p className="text-gray-600">Loading aircraft data...</p>
      </div>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8 flex flex-col items-center justify-center gap-8">
      <h1 className="text-3xl font-bold">Aircraft Controller</h1>
      <Dashboard 
        altitude={aircraft.altitude}
        groundAltitude={aircraft.ground_altitude}
        speed={aircraft.speed}
        heading={aircraft.heading}
      />
      <div className="flex items-center justify-center gap-16 md:flex-row flex-col">
        <Joystick onMove={onJoystickMove} onRelease={onJoystickRelease} />

        <RudderController
          defaultPosition={aircraft.rudder_position}
          onChange={async (position) => {
            await aircraft.setAileronPosition(position.angle);
          }}
        />

        <Lever
          title="Throttle"
          value={aircraft.throttle}
          onChange={async (value) => {
            await aircraft.setThrottle(value);
          }}
        />

        <Lever
          title="Spoilers"
          value={aircraft.spoiler_position}
          onChange={async (value) => {
            await aircraft.setSpoilerPosition(value);
          }}
        />
      </div>
    </div>
  )
}