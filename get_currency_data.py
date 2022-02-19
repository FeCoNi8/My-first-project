import requests


def parse_site(url):
    response = requests.get(url)
    return response

url = "https://www.cbr-xml-daily.ru/daily_json.js"
print(parse_site(url))
