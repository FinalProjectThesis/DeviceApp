import urllib3
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color

#for the HTTP 
from kivy.network.urlrequest import UrlRequest
import urllib
import requests
import json

#Asyncio
import asyncio

#the URL 
url = 'https://uslsthesisapi.herokuapp.com'
token = 0

class main_app(App):
    pass
class login_screen(BoxLayout):
    username = StringProperty('')
    password = StringProperty('')

    
    
    
    def btn_login_function(self):

        

        self.username = self.ids.user_input.text
        self.password = self.ids.pass_input.text
        if len(str(self.username)) == 0 or len(str(self.password)) == 0:
            print ("both fields are empty")
            if len(str(self.username)) == 0:
                print("please enter a username") # print this at the error label
            else:
                print("username is full") # erase error label text 
            if len(str(self.password)) == 0:
                print("please enter a password") # print this at the error label
            else:
                print ("password is full") # erase error label text 
        else:  # if all checks pass 
            Username = str(self.username)
            Password = str(self.password)
            print("Username : " + Username + "\n" + "Password : " + Password)
            
            # On Success Message of below's request 
            def loginrequestbody(self,*args):
                print(params)
                print("Result is " + str(Loginrequest.result))

            # requests through KIVY's own thing
            params =({"username":Username,"password":Password})
            print(params)
            Loginrequest = UrlRequest('https://uslsthesisapi.herokuapp.com/login', on_success= loginrequestbody, req_body=str(params))

class signup_screen(BoxLayout):
    pass

main_app().run()