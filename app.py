from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screenmanager import MDScreenManager
import requests
from settings import *

class WeatherScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_weather(self, city):
        params = {
        "q": city,
        "appid": API_KEY,
        }
        data = requests.get(CURRENT_WEATHER_URL, params)
        response = data.json()
        print(response)

    def search(self):
        city = self.ids.city.text
        weather = self.get_weather (city)

        temp = weather ["main"]["temp"]
        self.ids.temp.text = f"{temp}°C"    

        feels_like =  weather ["main"] ["feels_like"]
        self.ids.feels_like.text = f"Відчувається як {round(feels_like)}°C"

        desc = weather["weather"][0]["description"]
        self.ids.desc.text = desc.capitalizen()

        humidity = weather["main"]["humidity"]
        self.ids.humidity.text = "Вологість: {humidity}%"

        wind = weather["wind"]["speed"]
        self.ids.wind.text = f"вітер: {wind} м/с "

        icon = weather["weather"][0]["icon"]
        self.ids.icon.source = f'https://openweathermap.org/img/wn/{icon}@2x.png'

class Lclaud(MDApp):
    def build(self):
        Builder.load_file('syle.kv')
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightGreen" #'Teal'

    def show_forecast(self):
        self.manager.transition.direction='right'
        self.manager.current = 'forecast'

class ForecastScreen (MDScreen):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)

class LCloudApp (MDApp):
    def build(self):
        Builder.load_file('style.kv')
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        sm = MDScreenManager()
        self.weather_screen WeatherScreen(name='home')
        self.forecast_screen = ForecastScreen (name='forecast')
        sm.add_widget(self.weather_screen)
        sm.add_widget(self.forecast_screen)
        return sm


Lclaud().run()
