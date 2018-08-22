#store in mongoDB collection.
from pymongo import MongoClient
from generalforecast import GeneralForecast
from forecastperiod import *
import requests
import time

class Weather24hrForecastWriter():
    def __init__(self):
        self.item_dic = {}
        self.general_forecast_dic = {}
        self.active_period = {}
        self.client = MongoClient()

    #pull date and get the last item
    def pullLatestData(self):
        date = time.strftime("%Y-%m-%d")
        url = "https://api.data.gov.sg/v1/environment/24-hour-weather-forecast?date={}".format(date)
        response= requests.get(url)
        print(response.text)

        api_response = response.json()

        items = api_response['items']

        last_item = items[-1]

        return last_item

    def write(self): 
        item = self.pullLatestData()

        client = MongoClient('mongodb://localhost:27017')
        db = client['weather_24hr_forecast']
        
        mycol = db.weather_24hr_forecast
        
        for key in item:
    #         print("{} : {} | {}\n" .format(count, key, item.get(key)))
            if key == "update_timestamp": 
                self.item_dic[key] = item.get(key)
#                 print("{}: {}" .format(key, self.item.get(key)))
            if key == "timestamp" :
                self.item_dic[key] = item.get(key)
                print("{}: {}" .format(key, item.get(key)))
            if key == "valid_period":
                value_periods = item.get(key)
                for valid_period in value_periods:
                    self.item_dic[valid_period] = value_periods.get(valid_period) 
            if key == "general":
                generals = item.get(key)
                general_forecast = GeneralForecast(generals)
#                 general_forecast.summarize()  
                self.general_forecast_dic = general_forecast.summaryInDic()
            if key == "periods":
                periods = item.get(key)
                period_list = []
                for period in periods:
                    forecast_period = ForecastPeriod(period)
                    period_list.append(forecast_period)
                all_forecast_period = ForecastPeriods(period_list)
                all_forecast_period.getActivePeriod()
                self.active_period = all_forecast_period.summaryInDic()
        
        mycol.drop()
        
        forecast = self.general_forecast_dic['Forecast']
        humidity = self.general_forecast_dic['Relative Humidity']
        temperature = self.general_forecast_dic['Temperature']
        windspeed = self.general_forecast_dic['Wind Speed']
        winddirection = self.general_forecast_dic['Wind Direction']

        west = self.active_period['Forecast(West)']
        east = self.active_period['Forecast(East)']
        central = self.active_period['Forecast(Central)']
        south = self.active_period['Forecast(South)']
        north = self.active_period['Forecast(North)']
        
        timestamp = self.item_dic['update_timestamp']
        
        posts = db.weather_24hr_forecast

        post_data = {
            'Forecast': forecast,
            'Humidity': humidity,
            'Temperature': temperature,
            'Windspeed': windspeed,
            'Winddirection': winddirection,
            'West' : west,
            'East' : east,
            'Central' : central,
            'South' : south,
            'North' : north,
            'Timestamp' : timestamp
        }

        print(post_data)

        result = posts.insert_one(post_data)
        print('One post: {0}'.format(result.inserted_id)) 


latest_weather = Weather24hrForecastWriter()

latest_weather.write()