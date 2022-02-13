import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color

class WindowManager(ScreenManager):
    pass

class LoginScreen(Screen):
    username = StringProperty('')
    password = StringProperty('')

    def btn_login_function(self):
        self.username = self.ids.user_input.text
        self.password = self.ids.pass_input.text

        # test
        print('Username: ' + self.username + '\nPassword: ' + self.password)
        # return temp_app

    def btn_goto_signup(self):
        pass

class SignupScreen(Screen):
    pass

class MainApp(App):
    def build(self):
        return Builder.load_file('main_app.kv')

MainApp().run()