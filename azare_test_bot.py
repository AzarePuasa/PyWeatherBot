import botogram
from wfreader24hr import *
from wfreader2hr import *
from wfutility import readAPIKey

bot = botogram.create(readAPIKey("telegram"))

def sg_general_forecast():
    weather_forecast_reader = Weather24hrForecastReader()

    weather_forecast_reader.read()

    forecast_dic = weather_forecast_reader.getForecast()

    forecast = "Latest 24 hr Weather for Singapore:"   
        
    forecast += "\nGeneral Forecast:"
    forecast += "\nForecast: {}". format(forecast_dic.get('Forecast'))
    forecast += "\nHumidity: {}". format(forecast_dic.get('Humidity')) 
    forecast += "\nTemperature: {}". format(forecast_dic.get('Temperature')) 
    forecast += "\nWind Speed: {}". format(forecast_dic.get('Windspeed')) 
    forecast += "\nWind Direction: {}". format(forecast_dic.get('Winddirection')) 

    forecast += "\n\nRegion Specific Forecast:" 
    forecast += "\nWest: {}".format(forecast_dic.get('West')) 
    forecast += "\nEast: {}".format(forecast_dic.get('East')) 
    forecast += "\nCentral: {}".format(forecast_dic.get('Central')) 
    forecast += "\nSouth: {}".format(forecast_dic.get('South')) 
    forecast += "\nNorth: {}".format(forecast_dic.get('North')) 

    forecast += "\n\nGeneral Forecast updated on {}". format(forecast_dic.get('Timestamp')) 

    return forecast

def location_forecast(location):
    weather_forecast_reader_2h = Weather2hForecastReader()
    weather_forecast_reader_2h.read()
    current_forecast_item =  weather_forecast_reader_2h.getForecastItem()

    item_dic = current_forecast_item.getItemAsDic()

    for item in item_dic:
        if item == location:
            return item_dic.get(item)

    return "No Forecast Found."


@bot.command("weather")
def weather_command(chat, message, args):
    """
    Check the weather for today
    args[0] - Location(address). Optional.
    Accepts only SG address.
    if none, will provide general forecast for singapore.
    """
    general_forecast = sg_general_forecast()

    chat.send(general_forecast)

    if len(args) == 1:
        location = args[0]
        result = "Forecast for {}: {} ".format(location, location_forecast(location))
        chat.send(result)

@bot.command("hello")
def hello_command(chat, message, args):
    """Say hello to the world!"""

    if len(args) > 0:
        name = args[0]
        print(name)

        chat.send("Hello there " + name)
    else:
        chat.send(  " Usage: /hello <name> ")

@bot.command("test")
def test_command(chat, message, args):
    if len(args) > 0:
        name = args[0]
        print(name)

        chat.send(message)
    else:
        chat.send(  " Usage: /hello <name> ")

if __name__ == "__main__":
    bot.run()
