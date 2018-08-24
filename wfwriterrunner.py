from wfwriter24hr import Weather24hrForecastWriter 
from wfwriter2hr import Weather2hForecastWriter
from wfreader24hr import Weather24hrForecastReader
from wfreader2hr import Weather2hForecastReader
from wfutility import extractDateTime
from datetime import datetime
from dateutil.parser import parse
import pymongo

db_name = "sgwftimestamp"
timestamp_2hr_collection = "wf_2hr_last_timestamp_log"
timestamp_24hr_collection = "wf_24hr_last_timestamp_log"

def collection_exist(dbname, collection_name):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[dbname]
    # dblist = myclient.list_database_names()
    collectionlist = mydb.list_collection_names()
    # mycol = mydb[collection_name]
    print("List of Collection:", collectionlist)

    if collection_name in collectionlist:
        return True
    else:
        return False

def getlasttimestamp(dbname, collection_name):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[db_name]
    mycol = mydb[timestamp_2hr_collection]
    
    for record in mycol.find({}):  
        timestamp = record["Updated"]
        return timestamp
    
    return ""

# def last_2hr_timestamp():
#     pass

def launch_2hr_wfwriter():
    print("\nChecking 24h Weather Forecast")
    #get latest data that is saved in database and get the timestamp.
    current_wf_2hr = Weather2hForecastReader()
    current_wf_2hr.read()
    
    current_forecast_item = current_wf_2hr.getForecastItem()

    current_timestamp = current_forecast_item.getItemAsDic()["time_stamp"]
    # print("Timestamp in Mongodb: ", current_timestamp)

    current_date_time = extractDateTime(current_timestamp)
    currentdatetime = datetime.strptime(current_date_time, "%Y-%m-%dT%H:%M:%S")

    #get latest timestamp.
    latest_wf_2hr = Weather2hForecastWriter()
    latest_wf_2hr.pullLatestForecast()

    latest_forecast = latest_wf_2hr.getForecast()

    latest_timestamp = latest_forecast.getItemAsDic()["time_stamp"]
    # print("Timestamp in latest data pulled: ", latest_timestamp)

    latest_date_time = extractDateTime(latest_timestamp)
    latestdatetime = datetime.strptime(latest_date_time, "%Y-%m-%dT%H:%M:%S")

    if latestdatetime == currentdatetime or latestdatetime < currentdatetime:
        print("The timestamp in data api is the same or older than as timestamp than data in mongodb. Update not required")
    else: 
        print("The timestamp in data api is newer than the timestamp than data in mongodb. Update is required")
        latest_wf_2hr.write()
    

def launch_24hr_wfwriter():
    print("\nChecking 24hr Weather Forecast")
    current_wf_24hr = Weather24hrForecastReader()
    current_wf_24hr.read()

    current_forecast_item = current_wf_24hr.getForecast()

    current_timestamp = current_forecast_item.get('Timestamp')
    # print("Timestamp in Mongodb: ", current_timestamp)

    current_date_time = extractDateTime(current_timestamp)
    currentdatetime = datetime.strptime(current_date_time, "%Y-%m-%dT%H:%M:%S")

    #get latest timestamp.
    latest_wf_24hr = Weather24hrForecastWriter()
    latest_wf_24hr.pullLatestForecast()

    latest_forecast = latest_wf_24hr.getItemDic()

    latest_timestamp = latest_forecast["update_timestamp"]
    # print("Timestamp in latest data pulled: ", latest_timestamp)

    latest_date_time = extractDateTime(latest_timestamp)
    latestdatetime = datetime.strptime(latest_date_time, "%Y-%m-%dT%H:%M:%S")

    if latestdatetime == currentdatetime or latestdatetime < currentdatetime:
        
        print("\nThe timestamp in data api is the same or older than as timestamp than data in mongodb. Update not required")
    else: 
        print("\nThe timestamp in data api is newer than the timestamp than data in mongodb. Update is required")
        latest_wf_24hr.write()


datetime_now = datetime.now()
print("\nDate Now:",datetime_now)
# Check update for 2hr Forecast.
if collection_exist(db_name,timestamp_2hr_collection):
    print("2hr timestamp log Exist")
    print(getlasttimestamp(db_name, timestamp_2hr_collection))
    launch_2hr_wfwriter()
else:
    print("2hr timestamp log Not Exist")

#check Update for 24hr Forecast.
if collection_exist(db_name,timestamp_24hr_collection):
    print("24hr timestamp log Exist")
    print(getlasttimestamp(db_name, timestamp_24hr_collection))
    launch_24hr_wfwriter()
else:
    print("24hr timestamp log Not Exist")
