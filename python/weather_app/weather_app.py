import requests
import datetime

class Data:
    
    api_key = "6d0d1cf7dddd6e52c69375cd6c6d4d2c"
    base_urlL = "http://api.openweathermap.org/geo/1.0/direct?"
                #{city name},{state code},{country code}&limit={limit}&appid={API key}"
    base_urlW = "https://api.openweathermap.org/data/2.5/weather?"
                # lat={lat}&lon={lon}&exclude={part}&appid={API key}

    def get_location_data(base_urlL, api_key):
        city = input("Enter city: ".capitalize())
        country = input("Enter country: ".capitalize())
        print("")
        params = {
                    "q": f"{city},{country}",
                    "limit": 1,
                    "appid": api_key
                    }
        try:
            response = requests.get(base_urlL, params=params)
            data = response.json()
            if not data:
                print(f"error, city not available")
                return None
            city_data = data[0]
            name = city_data["name"]
            lon = city_data["lon"]
            lat = city_data["lat"]
            print(f"name: {name}")
            print(f"lon: {lon}")
            print(f"lat: {lat}\n")
            return lon, lat

        except requests.exceptions.RequestException as e:
                    print(f"Error fetching location data: {e}")
                    return None, None

    def get_weather_data(lon, lat):
        params = {
                    "lat": lat,
                    "lon": lon,
                    "appid": Data.api_key,
                    "units": "metric"
            }
        try:
            response = requests.get(Data.base_urlW, params=params)
            if response.status_code == 200:
                data = response.json()
                main = data["main"]
                temp = main["temp"]
                wind = data["wind"]["speed"]
                weather = data["weather"][0]["description"]
                sunrise_timestamp = data["sys"]["sunrise"]
                sunset_timestamp = data["sys"]["sunset"]

                sunrise = datetime.datetime.utcfromtimestamp(sunrise_timestamp)
                sunset = datetime.datetime.utcfromtimestamp(sunset_timestamp)

                print(f"temp: {temp}")
                print(f"wind: {wind}")
                print(f"weather: {weather}")
                print(f"sunrise: {sunrise}")
                print(f"sunset: {sunset}")
            else:
                print(f"error {response}")
        except:
            if not data:
                print(f"error {data}")


def main():
    lon, lat = Data.get_location_data(Data.base_urlL, Data.api_key)
    if lon and lat != None:
         Data.get_weather_data(lon, lat)
    else:
        print("city not found")

if __name__ == "__main__":
    main()