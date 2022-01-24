import requests
import json
URL = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey=GpvYpPBAKwBLiqPMwheV1D2PjB7gIzj8&q=Ankara"

# sending get request and saving the response as response object
response = requests.get(url=URL)

# extracting data in json format
data = response.json()

# type(data)
# type(data[1])
count = len(data)
# data[Region[LocalizedName]]

for i in range(count):
    print(data[i]["Region"]["LocalizedName"])
