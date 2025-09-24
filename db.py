import psycopg2
from config import DB_NAME, DB_USER, DB_PASS, DB_HOST

def connect():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST
    )

def insert_stations(stations):
    conn = connect()
    cur = conn.cursor()
    for s in stations:
        cur.execute("""
            INSERT INTO station (station_id, name, municipality)
            VALUES (%s, %s, %s)
            ON CONFLICT (station_id) DO NOTHING
        """, (s["station_id"], s["name"], s["municipality"]))
    conn.commit()
    cur.close()
    conn.close()

def insert_weather(weather_records):
    conn = connect()
    cur = conn.cursor()
    for obs in weather_records:
        cur.execute("""
            INSERT INTO weather (station_id, temp_celsius, date)
            VALUES (%s, %s, %s)
        """, (obs["station_id"], obs["value"], obs["time"]))
    conn.commit()
    cur.close()
    conn.close()