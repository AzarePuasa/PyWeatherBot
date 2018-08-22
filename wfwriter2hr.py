from pymongo import MongoClient
from forecastitem import ForecastItem
import requests
import time

class Weather2hForecastWriter():
    def __init__(self):
        self.client = MongoClient()
    
    def pullLatestData(self):
        date = time.strftime("%Y-%m-%d")

        url = "https://api.data.gov.sg/v1/environment/2-hour-weather-forecast?date={}".format(date)

        response= requests.get(url)
        print(response.text)
        api_response = response.json()
        items = api_response['items']
        last_item = items[-1]

        return last_item
        
    def write(self):
        item = self.pullLatestData()

        forecast_dict = {}

        for item_key in item.keys():
            if item_key == 'update_timestamp':
                update_timestamp = item.get(item_key)
            if item_key == 'timestamp':
                timestamp = item.get(item_key)
            if item_key == 'valid_period':
                valid_values = item.get(item_key)
                for key in valid_values.keys():
                    if key == 'start':
                        valid_start = valid_values.get(key)
                    if key == 'end':
                        valid_end = valid_values.get(key) 
            if item_key == 'forecasts':
                forecasts = item.get(item_key)
                area = ''
                forecast_item = ''
                for forecast in forecasts:
                    for forecast_key in forecast.keys():
                        if  forecast_key == 'area':
                            area = forecast.get(forecast_key)
                        if forecast_key == 'forecast':
                            forecast_item = forecast.get(forecast_key) 
                    forecast_dict[area] = forecast_item
        self.forecast_item = ForecastItem(timestamp,update_timestamp,valid_start,valid_end)
        self.forecast_item.populateTownForecast(forecast_dict)
        
        print(self.forecast_item)
        
        client = MongoClient('mongodb://localhost:27017')
        db = client['weather_2hr_forecast']
        
        mycol = db.weather_2hr_forecast
        mycol.drop()
        
        post_data = self.forecast_item.getItemAsDic()
        
        print(post_data)
        
        result = mycol.insert_one(post_data)
        print('One post: {0}'.format(result.inserted_id))

    def getForecast(self):
        return self.forecast_item

weather_2h_forecast_writer = Weather2hForecastWriter()

weather_2h_forecast_writer.write()