from areametadatareader import *

class Town_And_Forecast():
    def __init__(self):
        self.town_forecast_dic = {}
        self.town_list = []

        #get list of towns from CSV file. No longer needed as app is now using Mongodb.
#         with open(self.filename, 'r') as _filehandler:
#             csv_file_reader = csv.DictReader(_filehandler)
#             for row in csv_file_reader:
#                 # Do something here
#                 self.town_list.append(row['town'])

        #get list of towns from db
        area_metadata_reader = AreaMetadataReader()
        area_metadata_reader.read()
        areas_list = area_metadata_reader.getAreas()
        for area in areas_list:
            area_dic = area.areaInfoAsDic()
            self.town_list.append(area_dic['town'])

    def getTownList(self):
        return self.town_list
    
    def populate(self, raw_forecast_dic):
        for town in self.town_list: 
            self.town_forecast_dic[town] = raw_forecast_dic.get(town)
            
    def getForecast(self,forecast_town):
        for town_forecast in self.town_forecast_dic.keys():
            if forecast_town == town_forecast:
                return self.town_forecast_dic.get(town_forecast)
                          
    def getForecasts(self):
        return self.town_forecast_dic