from lib2to3.pgen2 import token
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.properties import StringProperty

Builder.load_file('lib/childlist.kv')

class ChildListScreen(Screen):
    def test(self):
        print(self.manager.token)