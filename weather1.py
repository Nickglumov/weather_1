import requests

def get_weather(city):
    base_url = "http://wttr.in/"
    params = {
        'm': '',
        'n': '',
        'q': '',
        'T': '',
        'lang': 'ru'
    }
    
    try:
        response = requests.get(f"http://wttr.in/{city}", params=params)
        response.raise_for_status()
        return response.text

def main():
    cities = ["Лондон", "Шереметьево", "Череповец"]
    
    for city in cities:
        weather = get_weather(city)
        print(weather)

if __name__ == '__main__':
    main()
