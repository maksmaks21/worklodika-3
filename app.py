from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton


class WeatherScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Lclaud(MDApp):
    def build(self):
        Builder.load_file('syle.kv')
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightGreen" #'Teal'


        return WeatherScreen()

Lclaud().run()
