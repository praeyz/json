import requests
import json 
"""
#Fetching data from URL 
url = 'https://edfreitas.me/test/wired_brain.json'

res = requests.get(url)
##print(res.text)  #This is a JSON document which doesnt allow to interact programatically, hence we need to deserialize the JSON document

if res.status_code == 200:
    #parsing a JSON formatted string and convert it to a python data structure which is a dictionary 
    data = json.loads(res.text)
    for item in data:
        pass
        #print(item)
"""



#Fetching data through and API 

Api_url = "https://jsonplaceholder.typicode.com/users"

#headers tells the server what format of document we expect, although the standard format by which it sends document is in JSON
headers = {
    'content-type' :'application/json'
}

#with params, we tell exactly what we require from the request
params = {
    "name": "Leanne Graham"
}

data = requests.get(url=Api_url,headers=headers, params=params )

#status code for an api call is different from a webpage
if data.status_code==200:
    api_data = json.loads(data.text)
    for datas in api_data:
        print(datas)
else:
    print('false')