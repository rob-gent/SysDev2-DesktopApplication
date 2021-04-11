from kivy.app import app
from kivy.uix.screenmanager import screenmanager, screen
from kivy.uik.widget import widget
from kivy.uix.label import label
from kivy.lang import builder
from kivy.uix.floatlayout import floatlayout
from kivy.properties import ObjectProperty
from kivy.clock import Clock

Builder.load_file('Shop.kv')

class MyApp(App):

    def build(self):
        self.screen_manager = ScreenManager()


    

