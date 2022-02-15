from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

# screen imports
from lib.login import LoginScreen
from lib.signup import SignupScreen
from lib.childlist import ChildListScreen

class WindowManager(ScreenManager):
    pass

sm = ScreenManager()
sm.add_widget(LoginScreen(name = 'login'))
sm.add_widget(SignupScreen(name = 'signup'))
sm.add_widget(ChildListScreen(name = 'childlist'))

class MainApp(App):
    pass

MainApp().run()