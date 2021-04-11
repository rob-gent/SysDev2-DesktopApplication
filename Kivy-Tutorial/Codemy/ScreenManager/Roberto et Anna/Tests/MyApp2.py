from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
#from kivy.uix.screenmanager import screenmanager, screen


class MenuApp(App):
    def build(self):
        root_widget = BoxLayout(orientation='vertical')

        output_label = Label(size_hint_y=1)

        button_navigation = ('Button 1','Button 2',
                          'Button 3','Button 4')

        button_grid = GridLayout(cols = 2, rows=2, size_hint_x=1, size_hint_y=0.5)
        for navigation in button_navigation:
            button_grid.add_widget(Button(text=navigation))

        root_widget.add_widget(output_label)
        root_widget.add_widget(button_grid)

        return root_widget

MenuApp().run()