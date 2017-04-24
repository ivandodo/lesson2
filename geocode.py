import httplib2
import json

def geoCodeLocation(inputString):
    google_api_key = "AIzaSyCnTdi7mZwbJ0Lup58Z8BcBMyDR3_fxFOI"
    location = inputString.replace(" ","+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (location, google_api_key))

    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    print ("response header: %s \n \n" % response)
    result = json.load(content)
    return result