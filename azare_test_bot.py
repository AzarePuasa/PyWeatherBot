import botogram
from wfreader24hr import *
from wfreader2hr import *

bot = botogram.create(<API KEY>)

def sg_general_forecast():
    return "Thundery Showers"

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
    weather_forecast_reader = Weather24hrForecastReader()

    weather_forecast_reader.read()

    chat.send(weather_forecast_reader.printForecast())

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
