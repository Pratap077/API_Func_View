import requests

URL = "http://127.0.0.1:8000/allinfo/"

r = requests.get(url=URL)

print(r.json())