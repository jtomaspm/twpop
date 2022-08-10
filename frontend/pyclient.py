import requests

base_url = "http://127.0.0.1:8000/"
twinfo_url = base_url + "twinfo/"

r = requests.get(twinfo_url)
print(r.json())
r = requests.get(twinfo_url, params={"abc" : 123})
print(r.json())
r = requests.get(twinfo_url, json={"query": "bananas"})
print(r.json())