#import httplib2
#import json
import requests
from codes import *

def geoCodeLocation(inputString):
    location = inputString.replace(" ","+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (location, google_api_key))

    content = requests.get(url)
    result = content.json()
    if (result['status'] == 'OK'):
        return result['results'][0]['geometry']['location']
    else:
        return None, None

def findARestaurant(mealType, location):
    latitude, longitude = geoCodeLocation(location)
    if (latitude == None):
        return 'No data for %s in %s'%(mealType, location)

    url="""https://api.foursquare.com/v2/venues/search?
    client_id=%s
    &client_secret=%s
    &v=20130815
    &ll=%s,%s
    &query=%s"""%(CLIENT_ID,CLIENT_SECRET,latitude, longitude, mealType)

    result = requests.get(url).json()
    return result
