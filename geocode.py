import requests
import json
from codes import *

def geoCodeLocation(inputString):
    location = inputString.replace(" ","+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (location, google_api_key))

    content = requests.get(url)
    result = content.json()
    if (result['status'] == 'OK'):
        return result['results'][0]['geometry']['location']
    else:
        return None


def findARestaurant(mealType, location):
    loc = geoCodeLocation(location)
    if not loc:
        return 'No Google data for %s in %s'%(mealType, location)

    url="""https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s"""\
        %(CLIENT_ID,CLIENT_SECRET,loc['lat'], loc['lng'], mealType)

    result = requests.get(url).json()

    try:
        venue = result['response']['venues'][0]
    except IndexError:
        return None

    if venue:
        venue_id = venue['id']
        url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' % (
        (venue_id, CLIENT_ID, CLIENT_SECRET)))
        result = (requests.get(url)).json()

        image_ref = result['response']['photos']['items']
        img = next((s for s in image_ref if s), None)
        return (img and img['prefix']+"300x300"+img['suffix']) or None
    else:
        return 'No data for %s in %s'%(mealType, location)


    return result['response']['venues'][0]
