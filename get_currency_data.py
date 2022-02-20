import requests
import json


def parse_site(url):
    response = requests.get(url)
    return response.json()

url = "https://www.cbr-xml-daily.ru/daily_json.js"



def get_json_data(url):
    data_json = parse_site(url)
    return data_json

url = "https://www.cbr-xml-daily.ru/daily_json.js"
def main():
    with open('data_json.json', 'r') as f:
        data_json = json.load(f)
        print(data_json)
main()



