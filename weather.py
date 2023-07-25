import requests
def get_weather_data():
  url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
  response = requests.get(url)
  return response.json()

#FUNCTION FOR GETTING TEMPERATURE
def get_weather_by_date(date):
  data = get_weather_data()
  for i in data['list']:
    if i['dt_txt'].startswith(date):
      return i['main']['temp']

#fUNCTION FOR GETTING WIND_SPEED
def get_wind_speed_by_date(date):
  data = get_weather_data()
  for i in data['list']:
    if i['dt_txt'].startswith(date):
      return i['wind']['speed']

#FUNCTION FOR GETTING PRESSURE
def get_pressure_by_date(date):
  data = get_weather_data()
  for i in data['list']:
    if i['dt_txt'].startswith(date):
      return i['main']['pressure']


def main():
  while True:
    print("1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
    choice = int(input("Enter your choice: "))
    
    #GIVE THE INPUT IN SPECIFIED FORMAT
    if choice == 1:
      date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
      temperature = get_weather_by_date(date)
      if temperature is not None:
        print(f"The temperature on {date} is {temperature}")
      else:
        print("No weather data available for the given date.")
    elif choice == 2:
      date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
      wind_speed = get_wind_speed_by_date(date)
      if wind_speed is not None:
        print(f"The wind speed on {date} is {wind_speed}")
      else:
        print("No weather data available for the given date.")
    elif choice == 3:
      date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
      pressure = get_pressure_by_date(date)
      if pressure is not None:
        print(f"The pressure on {date} is {pressure}")
      else:
        print("No weather data available for the given date.")
    elif choice == 0:
      print("Exiting the program.")
      break
    else:
      print("Invalid choice. Please try again.")


if __name__ == "__main__":
  main()
