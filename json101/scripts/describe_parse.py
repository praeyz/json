#we are trying to tell if a json file is a list or a dictionary 
import json 
import os 

path = r'api-scrapping\jsonfiles'

#looping through the files in our system
for files in os.listdir(path=path):
    if files.endswith('.json'):
        with open(os.path.join(path, files)) as f:
            data = json.load(f)
            print('file', files)
            print('type', type(data))

            if isinstance(data, list):
                print('here are the List-items:')
                for item in data:
                    print(item)

            elif isinstance(data, dict):
                print('here are the dict-items:')
                for key, value in data.items():
                    print(f"{key}:{value}")
            
            else:
                print('Data:')
                print(data)
            print('------------------------------------------------------------------------------------')



