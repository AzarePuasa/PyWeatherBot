import configparser

# function used by ForecastPeriods
def extractDateTime(strDateTime):
    datetime = strDateTime.split('+')[0]
    return datetime

def readAPIKey(keyname):
    config = configparser.ConfigParser()
    config.read("api_keys.txt")
    api_key = config.get("keys",keyname)

    return api_key