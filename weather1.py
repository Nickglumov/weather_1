import requests

cities = ["Лондон","Шереметьево","Череповец"]

for city in cities:
    url = f"http://wttr.in/{city}?m?n?qTqu&lang=ru"
    response = requests.get(url)
    print(response.text)