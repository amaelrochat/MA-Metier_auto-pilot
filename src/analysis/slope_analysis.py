from src.databases.database import SessionLocal, engine
from src.databases.classes.sessions import Session
from src.databases.classes.telemetrics import Telemetry
from src.databases.classes.commands import Command
import math


def coordonate_distance(lat1, lon1, lat2, lon2):
    R = 6371000  # Earth radius in m

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * \
        math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))

    return R * c


def calculate_slope(session_id):
    s = SessionLocal()
    data = s.query(Telemetry).filter(
        Telemetry.session_id == session_id).order_by(
        Telemetry.id).all()
    s.close()
    engine.dispose()

    result = []
    for i in range(len(data)):
        if i < (len(data) - 1):
            dist = coordonate_distance(
                data[i].latitude, data[i].longitude, data[i + 1].latitude, data[i + 1].longitude)
            alt_diff = data[i].altitude - data[i + 1].altitude
            if dist == 0:
                dist = 1
            result.append(alt_diff / dist)

    return result
