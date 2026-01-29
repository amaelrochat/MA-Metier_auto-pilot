import React, { useEffect, useState } from "react";
import { Autopilot } from "../models/autopilot";

export const AutopilotDashboard: React.FC = () => {
  const [enabled, setEnabled] = useState<boolean>(false);
  const [autopilot, setAutopilot] = useState<Autopilot | null>(null);
  const [altitude, setAltitude] = useState<number>(0);
  const [speed, setSpeed] = useState<number>(0);
  const [heading, setHeading] = useState<number>(0);

  useEffect(() => {
    Autopilot.current().then((ap) => {
      setAutopilot(ap);
      setEnabled(ap.enabled);
      setAltitude(ap.altitude);
      setSpeed(ap.speed);
      setHeading(ap.heading);
    });
  }, []);

  useEffect(() => {
    if (autopilot) {
      autopilot.toggle(enabled);
    }
  }, [enabled, autopilot]);

  useEffect(() => {
    if (autopilot) {
      autopilot.setAltitude(altitude);
    }
  }, [altitude, autopilot]);

  useEffect(() => {
    if (autopilot) {
      autopilot.setSpeed(speed);
    }
  }, [speed, autopilot]);

  useEffect(() => {
    if (autopilot) {
      autopilot.setHeading(heading);
    }
  }, [heading, autopilot]);

  if (!autopilot) {
    return <div className="autopilot-dashboard p-5">Loading...</div>;
  }

  return (
    <div className="autopilot-dashboard p-5">
      <h1 className="text-2xl font-bold mb-5">Autopilot Control</h1>

      <div className="mb-5">
        <label className="flex items-center gap-3 cursor-pointer">
          <input
            type="checkbox"
            checked={enabled}
            onChange={() => {
              setEnabled(!enabled);
            }}
            className="w-5 h-5"
          />
          <strong>{enabled ? "ON" : "OFF"}</strong>
        </label>
      </div>

      <div className="grid gap-4">
        <div>
          <label className="block mb-2">Altitude (ft): {altitude}</label>
          <input
            type="range"
            min="0"
            max="50000"
            step="100"
            value={altitude}
            onChange={(e) => setAltitude(Number(e.target.value))}
            disabled={!enabled}
            className="w-full disabled:opacity-50"
          />
        </div>

        <div>
          <label className="block mb-2">Speed (knots): {speed}</label>
          <input
            type="range"
            min="0"
            max="500"
            step="5"
            value={speed}
            onChange={(e) => setSpeed(Number(e.target.value))}
            disabled={!enabled}
            className="w-full disabled:opacity-50"
          />
        </div>

        <div>
          <label className="block mb-2">Heading (°): {heading}</label>
          <input
            type="range"
            min="0"
            max="359"
            step="1"
            value={heading}
            onChange={(e) => setHeading(Number(e.target.value))}
            disabled={!enabled}
            className="w-full disabled:opacity-50"
          />
        </div>
      </div>
    </div>
  );
};
