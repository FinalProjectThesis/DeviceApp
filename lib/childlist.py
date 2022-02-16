from imp import reload
import time
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.metrics import dp
from kivy.properties import StringProperty

from lib.login import LoginScreen

#for the HTTP 
from kivy.network.urlrequest import UrlRequest
import json


Builder.load_file('lib/childlist.kv')

class ChildListScreen(Screen):
    parent_username = 'tempuser'
    parent_password = 'temppass'

    def define_username(self):
        print(self.manager.parent_username)
        self.parent_username = self.manager.parent_username

    def define_password(self):
        self.parent_username = self.manager.parent_password
        print(self.parent_username)
    
class ChildList(BoxLayout):
    # fromLogin = ChildListScreen
    # testuser = LoginScreen.ids.user_input
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(0, 5):
            # size = dp(100) + i * 10
            size = dp(100)
            b = Button(
                text = str(i+1),
                size_hint = (None, 1), 
                width = size)
            self.ids['btn'+str(i+1)] = b
            self.ids['btn'+str(i+1)].bind(on_press = lambda x: print('Clicked ' + str(i+1)))
            self.add_widget(b)
    
    # def testclick(fromLogin):
    #     print(fromLogin.manager.parent_password)
    

    # def test():
    #     params = json.dumps({"username": str(ChildListScreen.define_username),  "password": 'temp'})
    #     print(params)
    #     headers= {'Content-type':'application/json','Accept':'text/plain'}
    #     print(params)
    #     childRequest = UrlRequest('https://uslsthesisapi.herokuapp.com/login', req_body=params,req_headers=headers)