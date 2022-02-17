from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty

# screen imports
from lib.login import LoginScreen
from lib.signup import SignupScreen
from lib.childlist import ChildListScreen
from lib.menu import MenuScreen

class WindowManager(ScreenManager):
    token = StringProperty('')
    parent_username = StringProperty('')

sm = ScreenManager()
sm.add_widget(LoginScreen(name = 'login'))
sm.add_widget(SignupScreen(name = 'signup'))
sm.add_widget(ChildListScreen(name = 'childlist'))
sm.add_widget(MenuScreen(name = 'menu'))

class MainApp(App):
    pass
        
MainApp().run()