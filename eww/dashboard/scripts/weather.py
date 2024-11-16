import sys
import requests

API_KEY = "OpenWeatherMap API KEY"
LAT = "City LAT"
LON = "City LON"
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}"
def main():
    r = requests.get(URL)
    rj = r.json()

    argument = sys.argv[1]
    if argument == "status":
        print(rj["weather"][0]["main"])
    elif argument == "temp":
        print(int(rj["main"]["temp"] - 273))

if __name__ == "__main__":
    try:
        main()
    except:
        pass
