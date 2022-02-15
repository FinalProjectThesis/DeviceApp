from lib2to3.pgen2 import token
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.metrics import dp
from kivy.properties import StringProperty

Builder.load_file('lib/childlist.kv')

class ChildListScreen(Screen):
    pass

class ChildList(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(0, 100):
            # size = dp(100) + i * 10
            size = dp(100)
            b = Button(text= 'Child ' + str(i+1), size_hint = (None, 1), width = size)
            self.add_widget(b)