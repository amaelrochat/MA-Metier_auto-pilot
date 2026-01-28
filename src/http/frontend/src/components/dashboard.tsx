import React from "react";

interface DashboardProps {
  altitude: number;
  groundAltitude: number;
  speed: number;
  heading: number;
  groundSpeed: number;
  planeAngle: number;
}

const Dashboard: React.FC<DashboardProps> = ({
  altitude,
  groundAltitude,
  speed,
  heading,
  groundSpeed,
  planeAngle,
}) => {
  return (
    <div className="p-8 bg-linear-to-br from-gray-900 to-gray-800 rounded-lg border border-gray-700 text-white shadow-2xl max-w-6xl mx-auto">
      <h2 className="text-2xl font-bold mb-6 text-cyan-400">
        Flight Dashboard
      </h2>
      <div className="grid grid-cols-2 gap-4 md:grid-cols-3">
        <div className="bg-gray-700 p-4 rounded border border-cyan-500">
          <p className="text-gray-400 text-sm uppercase">Altitude</p>
          <p className="text-xl font-bold text-cyan-400 truncate">{altitude}</p>
          <p className="text-gray-500 text-xs">ft</p>
        </div>
        <div className="bg-gray-700 p-4 rounded border border-cyan-500">
          <p className="text-gray-400 text-sm uppercase">Ground Alt</p>
          <p className="text-xl font-bold text-cyan-400 truncate">
            {groundAltitude}
          </p>
          <p className="text-gray-500 text-xs">ft</p>
        </div>
        <div className="bg-gray-700 p-4 rounded border border-cyan-500">
          <p className="text-gray-400 text-sm uppercase">Speed</p>
          <p className="text-xl font-bold text-cyan-400 truncate">{speed}</p>
          <p className="text-gray-500 text-xs">knots</p>
        </div>
        <div className="bg-gray-700 p-4 rounded border border-cyan-500">
          <p className="text-gray-400 text-sm uppercase">Heading</p>
          <p className="text-xl font-bold text-cyan-400 truncate">{heading}°</p>
        </div>
        <div className="bg-gray-700 p-4 rounded border border-cyan-500">
          <p className="text-gray-400 text-sm uppercase">Ground Speed</p>
          <p className="text-xl font-bold text-cyan-400 truncate">
            {groundSpeed}
          </p>
          <p className="text-gray-500 text-xs">knots</p>
        </div>
        <div className="bg-gray-700 p-4 rounded border border-cyan-500">
          <p className="text-gray-400 text-sm uppercase">Plane Angle</p>
          <p className="text-xl font-bold text-cyan-400 truncate">
            {planeAngle} rad
          </p>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
