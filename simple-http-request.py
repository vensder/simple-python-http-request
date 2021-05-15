from urllib.request import urlopen
from pprint import pprint
import json

with urlopen("https://ifconfig.me/ip") as response:
    response_content = response.read()

response_content.decode('utf-8')

with urlopen("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY") as response:
    response_content = response.read()

response_content.decode('utf-8')
json_response = json.loads(response_content)
pprint(json_response)
