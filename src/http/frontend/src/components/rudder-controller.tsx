import React, { useState, useCallback } from "react";

interface RudderPosition {
  angle: number; // -1 to 1
}

interface RudderControllerProps {
  onChange?: (position: RudderPosition) => void;
  defaultPosition?: number;
}

export const RudderController: React.FC<RudderControllerProps> = ({
  onChange,
  defaultPosition = 0,
}) => {
  const [rudderPosition, setRudderPosition] = useState<RudderPosition>({
    angle: defaultPosition,
  });

  const handleRudderChange = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      const angle = Math.max(-1, Math.min(1, Number(e.target.value)));
      const newPosition = { angle };
      setRudderPosition(newPosition);
      onChange?.(newPosition);
    },
    [onChange],
  );

  const handleReset = useCallback(() => {
    const resetPosition = { angle: defaultPosition };
    setRudderPosition(resetPosition);
    onChange?.(resetPosition);
  }, [defaultPosition, onChange]);

  return (
    <div className="flex flex-col items-center gap-8 p-6">
      <div className="flex items-center justify-center">
        <div
          className="flex items-center justify-center w-24 h-24 border-2 border-gray-800 rounded-full transition-transform duration-100 ease-out"
          style={{
            transform: `rotate(${rudderPosition.angle * 30}deg)`,
          }}
        >
          <div className="w-1 h-10 bg-red-500" />
        </div>
      </div>

      <div className="flex flex-col items-center gap-4 w-full max-w-xs">
        <input
          type="range"
          min="-1"
          max="1"
          step="0.1"
          value={rudderPosition.angle}
          onChange={handleRudderChange}
          className="w-full cursor-pointer"
          aria-label="Rudder position"
        />
        <p className="text-lg font-semibold">
          Position: {rudderPosition.angle.toFixed(1)}
        </p>
        <button
          onClick={handleReset}
          className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
        >
          Center
        </button>
      </div>
    </div>
  );
};

export default RudderController;
