from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty

# screen imports
from lib.login import LoginScreen
from lib.signup import SignupScreen
from lib.childlist import ChildListScreen

class WindowManager(ScreenManager):
    token = StringProperty('')

sm = ScreenManager()
sm.add_widget(LoginScreen(name = 'login'))
sm.add_widget(SignupScreen(name = 'signup'))
sm.add_widget(ChildListScreen(name = 'childlist'))

class MainApp(App):
    pass
    # def build(self):
    #     return Builder.load_file('mainapp.kv')

MainApp().run()