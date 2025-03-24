import os 
import json 


dir = 'jsonfiles/'
cdata = []

for fn in os.listdir(dir):
    if fn.endswith('.json'):
        with open(os.path.join(dir, fn), 'r') as f:
            data = json.load(f)
            if isinstance(data, dict):
                # Extract values of the keys that contain lists
                for value in data.values():
                    if isinstance(value, list):
                        cdata.extend(value)
            elif isinstance(data, list):
                cdata.extend(data)

for item in cdata:
    print(item)

output = 'output.json'

with open(output, 'w') as f: 
    json.dump(cdata, f)