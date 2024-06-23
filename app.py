import requests

def get_weather(city):
    api_key = '00edc2ccf69244eaf25aa870ba0db7af' 
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == 200:
            weather_description = data['weather'][0]['description']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            print(f"Weather in {city}:")
            print(f"Description: {weather_description}")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)

