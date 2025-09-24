import requests
from config import CLIENT_ID, PASSWORD

def get_stations(county="vestfold"):
    url = f"https://frost.met.no/sources/v0.jsonld?county={county}"
    res = requests.get(url, auth=(CLIENT_ID, PASSWORD))
    data = res.json()
    stations = []
    for s in data.get("data", []):
        stations.append({
            "station_id": s["id"],
            "name": s["shortName"],
            "municipality": s["municipality"]
        })
    return stations

def get_weather(stations, element, start, end):
    sources_str = ",".join([s["station_id"] for s in stations])
    url = (
        f"https://frost.met.no/observations/v0.jsonld?"
        f"sources={sources_str}&"
        f"elements={element}&"
        f"referencetime={start}/{end}"
    )
    res = requests.get(url, auth=(CLIENT_ID, PASSWORD))
    data = res.json()
    weather_records = []
    for entry in data.get("data", []):
        station_id = entry.get("sourceId").split(":")[0]
        time = entry.get("referenceTime").split("T")[0]
        for obs in entry.get("observations", []):
            if obs.get("value") is not None:
                weather_records.append({
                    "station_id": station_id,
                    "value": obs["value"],
                    "time": time
                })
    return weather_records