class GeneralForecast():
    
    HIGH_READING = "high"
    LOW_READING = "low"
    
    def __init__(self, generalforecastItems):
        for general in generalforecastItems:
            if (general == 'forecast'):
                self.forecast = generalforecastItems.get('forecast')
            if (general == 'relative_humidity'):
                self.relative_humidity = generalforecastItems.get('relative_humidity')
            if (general == 'temperature'):
                self.temperature = generalforecastItems.get('temperature')
            if (general == 'wind'):
                self.wind = generalforecastItems.get('wind')
                self.wind_speed = self.wind.get('speed')
                self.wind_direction = self.wind.get('direction')
  
    def getGeneralForecast(self):
        return self.forecast  
    
    def getHighRelativeHumidity(self):
        return self.relative_humidity.get(self.HIGH_READING)
            
    def getLowRelativeHumidity(self):
        return self.relative_humidity.get(self.LOW_READING)  

    def getHighTemperature(self):
        return self.temperature.get(self.HIGH_READING)
            
    def getLowTemperature(self):
        return self.temperature.get(self.LOW_READING)

    def getHighWindSpeed(self):
        return self.wind_speed.get(self.HIGH_READING)
            
    def getLowWindSpeed(self):
        return self.wind_speed.get(self.LOW_READING)    
    
    def getLowWindDirection(self):
        return self.wind_direction
    
    def getType(self, item):
        return print(type(item))
    
    def summarize(self):
        print("---General Forecast---")
        print("Forecast: {}".format(self.forecast))
        print("Relative Humidity: {} - {}".format(self.getLowRelativeHumidity(),self.getHighRelativeHumidity()))
        print("Temperature: {} - {}".format(self.getLowTemperature(),self.getHighTemperature()))
        print("Wind Speed: {} - {}".format(self.getLowWindSpeed(),self.getHighWindSpeed()))
        print("Wind Direction: {}".format(self.wind_direction))
        print("---General Forecast---")
        
    def summaryInDic(self):
        result = {}
        result['Forecast'] = self.getGeneralForecast()
        result['Relative Humidity'] = "{} - {}".format(self.getLowRelativeHumidity(),self.getHighRelativeHumidity())
        result['Temperature'] = "{} - {}".format(self.getLowTemperature(),self.getHighTemperature())
        result['Wind Speed'] = "{} - {}".format(self.getLowWindSpeed(),self.getHighWindSpeed())
        result['Wind Direction'] = "{}".format(self.wind_direction) 
        return result