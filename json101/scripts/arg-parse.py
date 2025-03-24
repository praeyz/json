#Creating command line to automate our task

import argparse
import json
import requests
import os

parser = argparse.ArgumentParser(description='A command-line application to fetch, retrieve, read, import, and parse JSON data.')
parser.add_argument('--fetch', metavar='URL', help='Fetch JSON data from a URL')
parser.add_argument('--api', metavar='ENDPOINT', help='Retrieve JSON data from a web API')
parser.add_argument('--read', metavar='PATH', help='Read JSON data from a file')
parser.add_argument('--importjson', metavar='PATH', help='Import JSON data from a file and convert to a Python data structure')
parser.add_argument('--parse', metavar='PATH', help='Describe and parse JSON data from a file')
args = parser.parse_args()

if args.fetch:
    url = args.fetch
    response = requests.get(url)
    data = response.json()
    print(json.dumps(data, indent=4))

if args.api:
    endpoint = args.api
    response = requests.get(endpoint)
    data = response.json()
    print(json.dumps(data, indent=4))

if args.read:
    path = args.read
    with open(path) as f:
        data = json.load(f)
        print(json.dumps(data, indent=4))

if args.importjson:
    path = args.importjson
    with open(path) as f:
        data = json.load(f)
        if isinstance(data, list):
            print('List:')
            print(data)
        elif isinstance(data, dict):
            print('Dictionary:')
            print(data)
        else:
            print('Data:')
            print(data)

if args.parse:
    path = args.parse
    with open(path) as f:
        data = json.load(f)
        print('Type:', type(data))
        if isinstance(data, list):
            print('List Items:')
            for item in data:
                print(item)
        elif isinstance(data, dict):
            print('Dictionary Items:')
            for key, value in data.items():
                print(key, ':', value)
        else:
            print('Data:')
            print(data)