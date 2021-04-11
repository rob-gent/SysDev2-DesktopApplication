from datetime import datetime
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
import time

#Define the different screens
class Dashboard(Screen):
    pass
class ViewAllOrders(Screen):
    pass
class OrdersAwaitingPostage(Screen):
    pass
class OrdersAwaitingPacking(Screen):
    pass
class OrdersAwaitingPicking(Screen):
    pass
class ApplicationSettings(Screen):
    pass
class WindowManager(ScreenManager):
    pass

#Comment
class DynamicPackingRow(Widget):
    pass 

#Displays the current time
class MyClock(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_my_clock, 1 / 10.)
 
    def update_my_clock(self, delta):
        self.ids.time.text = str(datetime.today().time())[0:8]

#Displays the current date
class MyCalendar(Label):
    def __init__(self, **kwargs):
            super().__init__(**kwargs)
            Clock.schedule_interval(self.update_my_calendar, 1 / 10.)

    def update_my_calendar(self, delta):
        self.ids.date.text = str(datetime.today().date())

#Designate the .kv design file
kv = Builder.load_file('app_design.kv')

#
class MyApp(App):
    def build(self):
        return kv

#Runs the app
if __name__ == '__main__':
    MyApp().run()

#Dashboard
#ViewAll Orders
#View Orders Awaiting Postaage
#awaiting packing
#awaiting picking
#refresh order button
#settings page