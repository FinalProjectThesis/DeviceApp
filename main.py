import imp
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty

# screen imports
from lib.login import LoginScreen
from lib.signup import SignupScreen
from lib.childlist import ChildListScreen
from lib.menu import MenuScreen
from lib.operations.addition import AdditionScreen
from lib.operations.division import DivisionScreen
from lib.operations.multiplication import MultiplicationScreen
from lib.operations.subtraction import SubtractionScreen

class WindowManager(ScreenManager):
    token = StringProperty('')
    parent_username = StringProperty('')
    student_id = StringProperty('')

sm = ScreenManager()
sm.add_widget(LoginScreen(name = 'login'))
sm.add_widget(SignupScreen(name = 'signup'))
sm.add_widget(ChildListScreen(name = 'childlist'))
sm.add_widget(MenuScreen(name = 'menu'))
sm.add_widget(AdditionScreen(name = 'addition'))
sm.add_widget(DivisionScreen(name = 'division'))
sm.add_widget(MultiplicationScreen(name = 'multiplication'))
sm.add_widget(SubtractionScreen(name = 'subtraction'))

class MainApp(App):
    def build(self):
        return Builder.load_file('lib/kv/mainapp.kv')
        
MainApp().run()