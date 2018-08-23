from pymongo import MongoClient
from areametadata import *

class AreaMetadataReader():
    def __init__(self):   
        self.list_areas = []
        self.client = MongoClient()
        
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['weather_area_metadata']
        self.mycol = self.db.weather_area_metadata
     
    #read from db and populate into list
    def read(self):
        for record in self.mycol.find({}):
            town = record['town']
            latitude = record['latitude'] 
            longitude = record['longitude']
            geoloc = (float(latitude),float(longitude))
            area_metadata = AreaMetadata(town,geoloc)
            self.list_areas.append(area_metadata)
             
    def getAreas(self):
        return self.list_areas

#test
area_metadata_read = AreaMetadataReader()
area_metadata_read.read()

areas_list = area_metadata_read.getAreas()

for area in areas_list:
    area.print()