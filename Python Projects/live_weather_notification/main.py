import requests
from plyer import notification

api_key = "2077c6d11f21406480a51937231110"
base_url="http://api.weatherapi.com/v1/current.json"

q = 23.880610615793042, 90.39552612229937

weather_params = {
    "key": api_key,
    "q": q,
}
response = requests.get(base_url,weather_params)
data = response.json()
location = data["location"]["name"]
temp = f'{data["current"]["temp_c"]}°C'
weather = data["current"]["condition"]["text"]

weather_data = f"Location: {location}\nTemperature: {temp}\nWeather: {weather}"

def send_notification(title,message):
    notification.notify(
        title = title,
        message = message,
        timeout = 10
    )

if __name__=="__main__":
    title = f"Current weather in {location}"
    message = weather_data
    send_notification(title,message)