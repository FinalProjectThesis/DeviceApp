from functools import partial
from lib2to3.pgen2 import token
from operator import mul
from threading import main_thread
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

    test = []
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        
        for i in range(0, 30):
            # partial(mul,i)
            # size = dp(100) + i * 10
            size = dp(100)
            b = Button(
                text = str(i+1),
                size_hint = (None, 1), 
                width = size)
            self.ids['btn'+str(i+1)] = b
            self.ids['btn'+str(i+1)].bind(on_press = lambda x: print(str(i+1)))
            self.test += str(i+1)
            self.add_widget(b)