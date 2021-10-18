import googlemaps
import config

#Google Maps
class gmaps:
    def __init__(self):
        self.client = googlemaps.Client(key=config.Config.GOOGLE_MAP_API_KEY)
    
    def findLatAndLng(self, address):
        query = self.client.geocode(address)
        latitude = query[0]['geometry']['location']['lat']
        longitude = query[0]['geometry']['location']['lng']

        return (latitude, longitude)

    def findNearestTarget(self, target, location):
        query = self.client.places(query="消防", language="zh-tw", location=location, type="fire_station")
        return query["results"][0]["name"]
