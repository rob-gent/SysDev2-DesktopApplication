from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3

con = sqlite3.connect('MyApp.db') #Create Database

# Create table
cur.execute('''CREATE TABLE people
               (text, text)''')

cur.execute('''CREATE TABLE products
               (text, price real,)''')

# Insert a row of data
cur.execute("SELECT FROM people VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
con.commit()


class MenuApp(App):
    pass

MenuApp().run()