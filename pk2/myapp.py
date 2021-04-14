import requests
URL = "http://127.0.0.1:8000/detail/5"
r = requests.get(url=URL)
print(r.json())