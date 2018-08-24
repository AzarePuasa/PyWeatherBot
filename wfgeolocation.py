from urllib.request import urlopen as OPEN
from urllib.parse import urlencode as ENCODE
from xml.etree import ElementTree as XML
import math

from areametadatareader import AreaMetadataReader
# importing only the necessary for memory saving

class wfGeolocation():
    def __init__(self):   
        self.list_areas = self.getWFAreaMetaData()
        self.area_distance_dic = {}
        
    #get the list of Area and its LatLng    
    def getWFAreaMetaData(self):    
        area_metadata_read = AreaMetadataReader()
        area_metadata_read.read()
        
        return area_metadata_read.getAreas()
    
    def getAddressLatLng(self,address):

        api_url = 'http://maps.googleapis.com/maps/api/geocode/xml?'
        # the location of Google's geolocation API
            
        url = api_url + ENCODE({'sensor': 'false', 'address': address})
        # putting the parts together in UTF-8 format
        print ('\nRetrieving location for:', address)
        data = OPEN(url).read()
        # getting that data
        # print ('Retrieved',len(data),'characters')
        tree = XML.fromstring(data)
        # digging into the XML tree

        res = tree.findall('result')
        # let's see the results now
        print(res)

        lat = res[0].find('geometry').find('location').find('lat').text
        # dig into the XML tree to find 'latitude'
        lng = res[0].find('geometry').find('location').find('lng').text
        # and longitude
        lat = float(lat)
        lng = float(lng)
        if lat < 0:
            lat_c = chr(167)+'S'
        else:
            lat_c = chr(167)+'N'
        if lng < 0:
            lng_c = chr(167)+'W'
        else:
            lng_c = chr(167)+'E'
        # format the coordinates to a more appealing form

        location = res[0].find('formatted_address').text
        location_type = res[0].find('geometry').find('location_type').text
        # location holds the geomap unit found by API, based on user input
        place_id = res[0].find('place_id').text


        # Time for the second part...
        url = 'http://maps.googleapis.com/maps/api/place/details/xml?'
        # the location of Google Places API
        # will need a valid key for that 
        # url = api_url + ENCODE({'placeid': place_id, 'key': ''})

        data = OPEN(url).read()
        tree = XML.fromstring(data)
        res = tree.findall('status')[0].text
        # rating = res[0].find('rating').text
        
        return (abs(lat),abs(lng))
    
    def distance(self,origin, destination):
        lat1, lon1 = origin
        lat2, lon2 = destination
        radius = 6371 # km

        dlat = math.radians(lat2-lat1)
        dlon = math.radians(lon2-lon1)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c

        return d
    
    def calculateDistance(self, address):   
        origin_tup = self.getAddressLatLng(address)   
        
#         print("Origin :",origin)
        
        for area in self.list_areas:
            area_dic = area.areaInfoAsDic()
            destination_tup = (area_dic['latitude'],area_dic['longitude'])
#             print("destination :",destination)
            
            distance = self.distance(origin_tup, destination_tup)
            town = area_dic['town']
            
            self.area_distance_dic[town] = distance
            
    def getDistanceDic(self):
        return self.area_distance_dic 
    
    def getNearestArea(self):
        return min(self.area_distance_dic, key = lambda x: self.area_distance_dic.get(x) )