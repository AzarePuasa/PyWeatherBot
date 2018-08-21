class AreaMetadata():
    def __init__(self,town, geolocation):
        self.town = town
        self.geolocation = geolocation
    
    def print(self):
        print("town: {}\
        \tlatitude: {}\
        \tlongitude: {}"\
              .format(self.town,self.geolocation[0],self.geolocation[1])) 
        
    def areaInfoAsList(self):
        areaInfo = []   
        areaInfo.append(self.town)
        areaInfo.append(self.geolocation[0])
        areaInfo.append(self.geolocation[1])
        
        return areaInfo  
    
    def areaInfoAsDic(self):
        areaInfo_dic = {} 
        areaInfo_dic['town'] = self.town
        areaInfo_dic['latitude'] = self.geolocation[0]
        areaInfo_dic['longitude'] = self.geolocation[1]
        return areaInfo_dic 