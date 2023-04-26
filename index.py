from urllib.parse import urlencode
import json
import httpx
import requests
from pprint import pprint

# we should use browser-like request headers to prevent being instantly blocked
BASE_HEADERS = {
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-language": "en-US;en;q=0.9",
    "accept-encoding": "gzip, deflate, br",
}


url = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={"usersSearchTerm":"90247","mapBounds":{"west":-118.313493,"east":-118.28481,"south":33.87241,"north":33.91741},"isMapVisible":false,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true}},"isListVisible":true}&wants={"cat1":["listResults"],"cat2":["total"],"regionResults":["regionResults"]}&requestId=2'
parameters = {
    "searchQueryState": {
        "usersSearchTerm": "90247",
        "mapBounds": {
            "west": "-118.313493",
            "east": "-118.28481",
            "south": "33.87241",
            "north": "33.91741",
        },
        "isMapVisible": "false",
        "filterState": {
            "sortSelection": {"value": "globalrelevanceex"},
            "isAllHomes": {"value": "true"},
        },
        "isListVisible": "true",
    },
    "wants": {
        "cat1": ["listResults"],
        "cat2": ["total"],
        "regionResults": ["regionResults"],
    },
    "requestId": 2,
}
# response = httpx.get(url + urlencode(parameters), headers=BASE_HEADERS)
# response = requests.get(url, params=parameters, headers=BASE_HEADERS)
response = requests.get(
    # "https://www.zillow.com/search/GetSearchPageState.htm?",
    # params=parameters,
    url,
    headers=BASE_HEADERS,
)
# pprint(response.text)
data = response.json()
# pprint(data)
results = data["cat1"]["searchResults"]["listResults"]
# print(json.dumps(results, indent=2))
# print(f"found {len(results)} property results")
for result in results:
    pprint(result["price"])
