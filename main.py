from api import get_stations, get_weather
from db import insert_stations, insert_weather

ELEMENT = "air_temperature"
START = "2025-08-01"
END = "2025-08-31"

stations = get_stations()
insert_stations(stations)

weather = get_weather(stations, ELEMENT, START, END)
insert_weather(weather)

import config
print("DB_PASS:", repr(config.DB_PASS))