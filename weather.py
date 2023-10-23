import os
import requests
from pprint import pprint
from dotenv import load_dotenv


load_dotenv()


def get_current_weather(city='Doaula'):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
  
  
  
    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    def weather_init():
        print('\n***** Get Current Weather ****')
        city = input("Enter a city:\n")
        if not bool(city.strip()):
            city = "Douala"

        weather = get_current_weather(city)
        print("\n")
        pprint(weather)

        if not weather['cod'] == 200:
            print("\nCity not found try again.\n\n")
            weather_init()

    
    weather_init()