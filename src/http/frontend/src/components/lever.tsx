import React, { useState } from "react";

interface LeverProps {
  title: string;
  min?: number;
  max?: number;
  value?: number;
  onChange?: (value: number) => void;
}

export const Lever: React.FC<LeverProps> = ({
  title,
  min = 0,
  max = 100,
  value = 0,
  onChange,
}) => {
  const [position, setPosition] = useState(value);

  const handleChange = (newValue: number) => {
    setPosition(newValue);
    onChange?.(newValue);
  };

  return (
    <div className="flex flex-col items-center gap-4">
      <label
        htmlFor={title.toLowerCase() + "-lever"}
        className="text-lg font-semibold"
      >
        {title}
      </label>
      <input
        id={title.toLowerCase() + "-lever"}
        type="range"
        min={min}
        max={max}
        value={position}
        onChange={(e) => handleChange(Number(e.target.value))}
        className="w-12 h-48 cursor-pointer"
        style={{
          writingMode: "vertical-rl",
          transform: "rotate(180deg)",
        }}
      />
      <span className="text-sm text-gray-600">{position}%</span>
    </div>
  );
};
