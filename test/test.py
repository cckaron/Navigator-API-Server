import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyBAHYSAVo_NiC6S6IMFx4-G7jSZI1GXyak')
geocode_result = gmaps.geocode('110台北市信義區信義路五段1號')
lat = geocode_result[0]['geometry']['location']['lat']
lng = geocode_result[0]['geometry']['location']['lng']
