from pymongo import MongoClient
from forecastitem import *

class Weather2hForecastReader():
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['weather_2hr_forecast']
        
        self.mycol = self.db.weather_2hr_forecast
    
    def read(self):
        for record in self.mycol.find({}):
            timestamp = record["time_stamp"]
            update_timestamp = record["updated_timestamp"]
            valid_start = record["valid_start"]
            valid_end = record["valid_end"]
    
            #create ForecastItem    
            self.forecast_item = ForecastItem(timestamp,update_timestamp,valid_start,valid_end)        
            
            #attach town forecast
            forecast_dict = {}
            town_list = self.forecast_item.townforecast.getTownList()
            for town in town_list:
                forecast = record[town]
                forecast_dict[town] = forecast
                
            self.forecast_item.populateTownForecast(forecast_dict)
            
    def getForecastItem(self):
        return self.forecast_item