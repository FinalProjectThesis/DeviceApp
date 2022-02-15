from lib2to3.pgen2 import token
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.properties import StringProperty

from lib.login import LoginScreen

Builder.load_file('lib/childlist.kv')

class ChildListScreen(Screen):
    login = LoginScreen()
    token = login.btn_login_function()

    def test(self):
        print(self.token)