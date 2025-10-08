import requests
from pprint import pprint

yangilik="https://api.open-meteo.com/v1/forecast?latitude=41.31&longitude=69.28&current_weather=true"
r =  requests.get(yangilik)
pprint(r.json())