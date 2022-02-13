from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color

class main_app(App):
    pass
class login_screen(BoxLayout):
    username = StringProperty('')
    password = StringProperty('')

    def btn_login_function(self):
        self.username = self.ids.user_input.text
        self.password = self.ids.pass_input.text

        # test
        print('Username: ' + self.username + '\nPassword: ' + self.password)

class signup_screen(BoxLayout):
    pass

main_app().run()