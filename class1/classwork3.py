data = {
"markers": [
{
"name": "Rixos The Palm Dubai",
"position": [25.1212, 55.1535],
},
{
"name": "Shangri-La Hotel",
"location": [25.2084, 55.2719]
},
{
"name": "Grand Hyatt",
"location": [25.2285, 55.3273]
}
]
}
class Hotels:
    def __init__(self,dict1):
        self.dict1 = dict1


    def getnames(self):
        innerdict = self.dict1.values()
        hotelNames = []
        for i in innerdict:
            for j in i:
                hotelNames.append(j['name'])
        return hotelNames

    def getNameAndLocationsInDict(self):
        innerdict = self.dict1.values()
        hotelNames = []
        locations = []
        for i in innerdict:
            for j in i:
                a = list(j.values())
                for v in range(len(a)):
                    if v % 2 == 0:
                        hotelNames.append(a[v])
                    else:
                        locations.append(a[v])
        hotelDict = {
            'name':hotelNames,
            'location':locations,
        }
        return hotelDict
    
    def setId(self):
        innerdict = self.dict1.values()
        hotelNames = []
        count = 1
        for i in innerdict:
            for j in i:
                j['status_id'] = count
                count += 1
        return self.dict1

        

hyatt = Hotels(data)
# print(hyatt.getnames())
# print(hyatt.getNameAndLocationsInDict())
print(hyatt.setId())