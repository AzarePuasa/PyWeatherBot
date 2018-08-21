from pymongo import MongoClient

class Weather24hrForecastReader():
    
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['weather_24hr_forecast']
        
        self.mycol = self.db.weather_24hr_forecast
        self.forecast_dic = {}
    
    def read(self):
        cursor = self.mycol.find({})
        
        for document in cursor:
            self.forecast_dic['Forecast'] = document.get('Forecast')
            self.forecast_dic['Humidity'] = document['Humidity']
            self.forecast_dic['Temperature'] = document['Temperature']
            self.forecast_dic['Windspeed'] = document['Windspeed']
            self.forecast_dic['Winddirection'] = document['Winddirection']

            self.forecast_dic['West'] = document['West']
            self.forecast_dic['East'] = document['East']
            self.forecast_dic['Central'] = document['Central']
            self.forecast_dic['South'] = document['South']
            self.forecast_dic['North'] = document['North']
            self.forecast_dic['Timestamp'] = document['Timestamp']
    
    def getForecast(self):
        return self.forecast_dic
         
    def printForecast(self):  

        forecast = "Latest 24 hr Weather for Singapore:"   
            
        forecast += "\nGeneral Forecast:"
        forecast += "\nForecast: {}". format(self.forecast_dic.get('Forecast'))
        forecast += "\nHumidity: {}". format(self.forecast_dic.get('Humidity')) 
        forecast += "\nTemperature: {}". format(self.forecast_dic.get('Temperature')) 
        forecast += "\nWind Speed: {}". format(self.forecast_dic.get('Windspeed')) 
        forecast += "\nWind Direction: {}". format(self.forecast_dic.get('Winddirection')) 

        forecast += "\n\nRegion Specific Forecast:" 
        forecast += "\nWest: {}".format(self.forecast_dic.get('West')) 
        forecast += "\nEast: {}".format(self.forecast_dic.get('East')) 
        forecast += "\nCentral: {}".format(self.forecast_dic.get('Central')) 
        forecast += "\nSouth: {}".format(self.forecast_dic.get('South')) 
        forecast += "\nNorth: {}".format(self.forecast_dic.get('North')) 

        forecast += "\n\nUpdated on {}". format(self.forecast_dic.get('Timestamp')) 

        return forecast