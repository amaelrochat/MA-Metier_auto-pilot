import React from "react";

interface MapProps {
  latitude: number;
  longitude: number;
}

export const Map: React.FC<MapProps> = ({ latitude, longitude }) => {
  return (
    <div
      style={{
        width: "100%",
        height: "400px",
        borderRadius: "8px",
        overflow: "hidden",
      }}
    >
      <iframe
        width="100%"
        height="100%"
        frameBorder="0"
        src={`https://www.openstreetmap.org/export/embed.html?bbox=${longitude - 0.01},${latitude - 0.01},${longitude + 0.01},${latitude + 0.01}&layer=mapnik&marker=${latitude},${longitude}`}
        style={{ border: 0 }}
      />
    </div>
  );
};
