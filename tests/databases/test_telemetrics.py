import os
os.environ["DATABASES_URI"] = "sqlite:///src/databases/test_database.db"

from src.databases.database import SessionLocal, Base, engine
from src.databases.classes.sessions import Session
from src.databases.classes.telemetrics import Telemetry
from src.databases.classes.commands import Command
def test_create_session():
    Base.metadata.create_all(bind=engine)

    s = SessionLocal()

    obj = Telemetry(
    coordonate=46.8223,
    altitude=1234.5,
    horizontal_speed=38.2,
    vertical_speed=1.6,
    time_since_departure="0:15",
    session_id=1
    )

    s.add(obj)
    s.commit()
    s.refresh(obj)

    r = s.query(Telemetry).filter(Telemetry.coordonate == 46.8223).first()

    assert r.session_id == obj.session_id

    s.close()
    engine.dispose()
    os.remove("src/databases/test_database.db")