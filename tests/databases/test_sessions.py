from src.databases.database import SessionLocal, Base, engine
from src.databases.classes.sessions import sessions
from src.databases.classes.telemetrics import telemetrics
from src.databases.classes.commands import commands
 
def test_create_session():
    Base.metadata.create_all(bind=engine)

    s = SessionLocal()
    obj = sessions(date_time="15.01.2026 15:41",
               glider_model="glider",
               takeoff_location="ste-croix")
    s.add(obj)
    s.commit()
    s.refresh(obj)

    r = s.query(sessions).filter(sessions.date_time == "2026-01-15 15:41:00.000000").first()

    assert r.id == obj.id

    s.close()