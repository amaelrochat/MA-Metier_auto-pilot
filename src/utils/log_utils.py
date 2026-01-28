from datetime import datetime
from src.databases.database import SessionLocal, Base, engine
from src.databases.classes.sessions import Session
from src.databases.classes.telemetrics import Telemetry
from src.databases.classes.commands import Command


class Log():
    @staticmethod
    def new_session() -> Session:
        Base.metadata.create_all(bind=engine)

        s = SessionLocal()
        obj = Session(
            date_time=datetime.now().strftime("%Y-%m-%d %H:%M"),
        )
        s.add(obj)
        s.commit()
        s.refresh(obj)

        s.close()
        return obj

    @staticmethod
    def telemetry_entry(session_id: int, altitude: float,
                        ground_altitude: float, speed: float,
                        heading: float, ground_speed: float) -> Telemetry:
        s = SessionLocal()
        obj = Telemetry(
            session_id=session_id,
            date_time=datetime.now().strftime("%Y-%m-%d %H:%M"),
            altitude=altitude,
            ground_altitude=ground_altitude,
            ground_speed=ground_speed,
            speed=speed,
            heading=heading
        )
        s.add(obj)
        s.commit()
        s.refresh(obj)

        s.close()
        return obj

    @staticmethod
    def command_entry(session_id: int, throttle: float = None, aileron: float = None,
                      rudder: float = None, elevator: float = None,
                      spoiler: float = None) -> Command:
        s = SessionLocal()
        obj = Command(
            session_id=session_id,
            date_time=datetime.now().strftime("%Y-%m-%d %H:%M"),
            throttle=throttle,
            aileron_position=aileron,
            rudder_position=rudder,
            elevator_position=elevator,
            spoiler_position=spoiler
        )
        s.add(obj)
        s.commit()
        s.refresh(obj)

        s.close()
        return obj
