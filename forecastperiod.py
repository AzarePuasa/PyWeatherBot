from datetime import datetime
from wfutility import *

class ForecastPeriod():
    REGION_WEST = "west"
    REGION_EAST = "east"
    REGION_CENTRAL = "central"
    REGION_SOUTH = "south"
    REGION_NORTH = "north"
    
    def __init__(self, periodItems):
        for periodItem in periodItems:
            if periodItem == 'time':
                self.periodtime = periodItems.get(periodItem)
            if periodItem == 'regions':
                self.region = periodItems.get(periodItem)
  
    def getStartTime(self):
        return self.periodtime.get('start')

    def getEndTime(self):
        return self.periodtime.get('end')           
        
    def getForecastWest(self):
        return self.region.get(self.REGION_WEST)
    
    def getForecastEast(self):
        return self.region.get(self.REGION_EAST)

    def getForecastCentral(self):
        return self.region.get(self.REGION_CENTRAL)  

    def getForecastSouth(self):
        return self.region.get(self.REGION_SOUTH)   
    
    def getForecastNorth(self):
        return self.region.get(self.REGION_NORTH) 
    
    def summarize(self):
        print("Start: {}".format(self.getStartTime()))
        print("End: {} ".format(self.getEndTime()))
        print("Forecast(West): {}".format(self.getForecastWest()))
        print("Forecast(East): {}".format(self.getForecastEast()))
        print("Forecast(Central): {}".format(self.getForecastCentral()))
        print("Forecast(South): {}".format(self.getForecastSouth()))
        print("Forecast(North): {}".format(self.getForecastNorth()))


class ForecastPeriods():
    def __init__(self, periods):
        self.periods = periods
        self.active_period = []
        
    def getActivePeriod(self):

        datetime_now = datetime.now()
        for period in self.periods:       
            datetime_start_str = extractDateTime(period.getStartTime())
            datetime_end_str = extractDateTime(period.getEndTime())
            
            datetime_start = datetime.strptime(datetime_start_str, "%Y-%m-%dT%H:%M:%S")
            datetime_end = datetime.strptime(datetime_end_str, "%Y-%m-%dT%H:%M:%S")
            
            #compare and show period
            if datetime_now > datetime_start and datetime_now < datetime_end:
                self.active_period = period 
                
    def summaryInDic(self):
        validperiod = {}
        validperiod['Forecast(West)'] = "{}".format(self.active_period.getForecastWest())
        validperiod['Forecast(East)'] = "{}".format(self.active_period.getForecastEast())
        validperiod['Forecast(Central)'] = "{}".format(self.active_period.getForecastCentral())
        validperiod['Forecast(South)'] = "{}".format(self.active_period.getForecastSouth())
        validperiod['Forecast(North)'] = "{}".format(self.active_period.getForecastNorth())        
        return validperiod         