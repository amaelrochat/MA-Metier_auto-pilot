import React, { useRef, useEffect, useState } from "react";

interface JoystickState {
  x: number;
  y: number;
}

interface JoystickProps {
  onMove?: (state: JoystickState) => void;
  onRelease?: () => void;
}

export const Joystick: React.FC<JoystickProps> = ({ onMove, onRelease }) => {
  const containerRef = useRef<HTMLDivElement>(null);
  const knobRef = useRef<HTMLDivElement>(null);
  const [isDragging, setIsDragging] = useState(false);
  const [position, setPosition] = useState<JoystickState>({ x: 0, y: 0 });

  const RADIUS = 80;

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      if (!isDragging || !containerRef.current) return;

      const rect = containerRef.current.getBoundingClientRect();
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      let x = e.clientX - rect.left - centerX;
      let y = e.clientY - rect.top - centerY;

      const distance = Math.sqrt(x * x + y * y);
      if (distance > RADIUS) {
        const angle = Math.atan2(y, x);
        x = Math.cos(angle) * RADIUS;
        y = Math.sin(angle) * RADIUS;
      }

      setPosition({ x, y });
      onMove?.({ x: x / RADIUS, y: y / RADIUS });
    };

    const handleMouseUp = () => {
      setIsDragging(false);
      setPosition({ x: 0, y: 0 });
      onRelease?.();
    };

    document.addEventListener("mousemove", handleMouseMove);
    document.addEventListener("mouseup", handleMouseUp);

    return () => {
      document.removeEventListener("mousemove", handleMouseMove);
      document.removeEventListener("mouseup", handleMouseUp);
    };
  }, [isDragging, onMove, onRelease]);

  return (
    <div className="flex items-center justify-center">
      <div
        ref={containerRef}
        className="relative w-48 h-48 bg-gray-900 rounded-full shadow-lg border-2 border-gray-700 cursor-grab active:cursor-grabbing flex items-center justify-center"
        onMouseDown={() => setIsDragging(true)}
      >
        {/* Center dot */}
        <div className="absolute w-1 h-1 bg-gray-600 rounded-full" />

        {/* Knob */}
        <div
          ref={knobRef}
          className="absolute w-8 h-8 bg-blue-500 rounded-full shadow-md"
          style={{
            transform: `translate(${position.x}px, ${position.y}px)`,
          }}
        />
      </div>
    </div>
  );
};
