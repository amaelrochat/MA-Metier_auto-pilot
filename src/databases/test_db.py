"""
Program name : test_db.py
Date : 15.01.2026
Edit : 15.01.2026
Description : Test the ORM
Version : V 0.1
"""

from classes.sessions import sessions
from classes.telemetrics import telemetrics
from classes.commands import commands
from database import *

#CREATE TABLE
Base.metadata.create_all(bind=engine)

s = SessionLocal()
"""
obj = sessions(date_time="15.01.2026 15:41",
               glider_model="glider",
               takeoff_location="ste-croix")
s.add(obj)
s.commit()
s.refresh(obj)

obj = sessions(date_time="16.01.2026 15:41",
               glider_model="glider_2",
               takeoff_location="ste-croix")
s.add(obj)
s.commit()
s.refresh(obj)

obj = telemetrics(
    coordonate=48.8566,
    altitude=1200,
    horizontal_speed=250,
    vertical_speed=5,
    time_since_departure="00:15",
    session_id=1)
s.add(obj)
s.commit()
s.refresh(obj)

obj = telemetrics(
    coordonate=48.8566,
    altitude=1300,
    horizontal_speed=200,
    vertical_speed=-10,
    time_since_departure="00:15",
    session_id=2)
s.add(obj)
s.commit()
s.refresh(obj)
"""
print("\nall telemetrics")
for t in s.query(telemetrics).all():
    print(t.coordonate, t.altitude, t.session_id, t.session.glider_model, t.session.takeoff_location)

print("\nfirst session telemetrics")
for t in s.query(telemetrics).filter(telemetrics.session_id == 1).all():
    print(t.coordonate, t.altitude, t.session_id, t.session.glider_model, t.session.takeoff_location)

s.close()