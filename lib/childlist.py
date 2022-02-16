from imp import reload
from queue import PriorityQueue
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
    token = ''

    def define_user(self):
        self.parent_username = self.manager.parent_username
        self.token = self.manager.token

        # On Success Message of below's request 
        def successrequest(self,*args):
            print ("Success request") # GOTO next screen
            print("Result is " + str(childRequest.result))
            data = childRequest.result
            print(len(data))

        # On Fail Message of below's request 
        def failedrequest(self,*args):
            print ("Failed Request") # show error message
            print ("Result is "+ str(childRequest.result))

        params = json.dumps({"parent_username" : self.parent_username})
        headers= {'Content-type':'application/json','Accept':'text/plain', 'token': self.token}
        print(params)
        childRequest = UrlRequest('https://uslsthesisapi.herokuapp.com/childlist', on_success= successrequest, on_failure=failedrequest, req_body=params, req_headers=headers)


    
    def test_print(self):
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
            self.ids['btn'+str(i+1)].bind(on_press = lambda x: print('Clicked'))
            self.add_widget(b)
    
    # def testclick(fromLogin):
    #     print(fromLogin.manager.parent_password)