import os
os.environ["DATABASES_URI"] = "sqlite:///src/databases/test_database.db"

from src.databases.database import SessionLocal, Base, engine
from src.databases.classes.sessions import Session
from src.databases.classes.telemetrics import Telemetry
from src.databases.classes.commands import Command

def test_create_session():
    Base.metadata.create_all(bind=engine)

    s = SessionLocal()
    obj = Command(x_handle=90,
                  y_handle=-90,
                  crossbar=45,
                  session_id=1)
    s.add(obj)
    s.commit()
    s.refresh(obj)

    r = s.query(Command).filter(Command.x_handle == 90).first()

    assert r.session_id == obj.session_id

    s.close()
    engine.dispose()
    os.remove("src/databases/test_database.db")