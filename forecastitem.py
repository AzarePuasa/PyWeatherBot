from townforecast import *

class ForecastItem():
    
    def __init__(self, time_stamp, updated_timestamp, valid_start, valid_end):
        self.updated_timestamp = updated_timestamp
        self.time_stamp = time_stamp
        self.valid_start = valid_start
        self.valid_end = valid_end
        
        self.townforecast = Town_And_Forecast()
        
    def populateTownForecast(self,raw_forecast_dic):
        self.townforecast.populate(raw_forecast_dic)
           
    def getHeader(self):
        header = []
        
        header.append("time_stamp")
        header.append("updated_timestamp")
        header.append("valid_start")
        header.append("valid_end")
        
        for town in self.townforecast.getTownList():
            header.append(town)
        
        return header

    def printItem(self):
        print("Time Stamp: {}\
              \tUpdated Time Stamp: {}\
              \tValid Start: {}\
              \tValid End: {}".format(self.time_stamp, self.updated_timestamp,self.valid_start, self.valid_end)) 
        self.townforecast.getForecasts()
        
    def getItemAsList(self):
        item_list = []
        item_list.append(self.time_stamp)
        item_list.append(self.updated_timestamp)
        item_list.append(self.valid_start)
        item_list.append(self.valid_end)
        
        town_forecasts = self.townforecast.getForecasts()
        for town in town_forecasts.keys():
            forecast = town_forecasts.get(town)
            item_list.append(forecast)
        
        return item_list
    
    def getItemAsDic(self):
        item_dic = {}
    
        item_dic["time_stamp"] = self.time_stamp
        item_dic["updated_timestamp"] = self.updated_timestamp
        item_dic["valid_start"] = self.valid_start
        item_dic["valid_end"] = self.valid_end
        
        town_forecasts = self.townforecast.getForecasts()
        for town in town_forecasts.keys():
            forecast = town_forecasts.get(town)
            item_dic[town] = forecast
        
        return item_dic