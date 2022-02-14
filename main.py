from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
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

class WindowManager(ScreenManager):
    pass
class LoginScreen(Screen):
    username = StringProperty('')
    password = StringProperty('')

    def btn_login_function(self):
        self.username = self.ids.user_input.text
        self.password = self.ids.pass_input.text
        if len(str(self.username)) == 0 or len(str(self.password)) == 0:
            print ("both fields are empty") # for debugging
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
            def successrequest(self,*args):
                print ("Success request ") # GOTO next screen
                print(params)
                print("Result is " + str(Loginrequest.result))
            # On Fail Message of below's request 
            def failedrequest(self,*args):
                print ("Failed Request") # show error message 
                print (params)
                print ("Result is "+ str(Loginrequest.result))

        # test
            # requests through KIVY's own thing
            params =json.dumps({"username":Username,"password":Password})
            print (params)
            headers= {'Content-type':'application/json','Accept':'text/plain'}
            Loginrequest = UrlRequest('https://uslsthesisapi.herokuapp.com/login', on_success= successrequest,on_failure=failedrequest, req_body=params,req_headers=headers)

class SignupScreen(Screen):
    username = StringProperty('')
    password = StringProperty('')
    confirm_password = StringProperty('')
    first_name = StringProperty('')
    last_name = StringProperty('')

    def btn_register_function(self):

        if len(str(self.username)) == 0 or len(str(self.password)) == 0:
            print ("both fields are empty") # for debugging
            if len(str(self.username)) == 0:
                print("please enter a username") # print this at the username error label
            else:
                print("username is full") # erase username error label text 
            if len(str(self.password)) == 0:
                print("please enter a password") # print this at the password error label
            else:
                print ("password is full") # erase error label text
            if self.password != self.confirm_password:
                print("Please Confirm your password") # print this at the confirm_password  error label
            if len(str(self.first_name)) == 0:
                print("please enter your first name")
            else:
                print("firstname is full") # erase first name error label text
            if  len(str(self.last_name)) ==0:
                print("please enter your last name ") # print this at the last name  error label
            else:
                print("lastname is full") # erase last name error label text
        else:  # if all checks pass 
            Username = str(self.username)
            Password = str(self.password)
            First_name = str(self.first_name)
            Last_name = str(self.last_name)
            
            # On Success Message of below's request 
            def successrequest(self,*args):
                print("Register Success")
                print(params)
                print("Result is " + str(Registerrequest.result))
            # On Failed message of below's request             
            def failedrequest(self,*args):
                print ("Failed Request") # show error message 
                print (params)
                print ("Result is "+ str(Registerrequest.result))
            
            params =json.dumps({"username":Username,"password":Password, "first_name": First_name, "last_name": Last_name})
            print (params)
            headers= {'Content-type':'application/json','Accept':'text/plain'}
            Registerrequest = UrlRequest('https://uslsthesisapi.herokuapp.com/register', on_success= successrequest,on_failure=failedrequest, req_body=params,req_headers=headers)

            
            


class MainApp(App):
    def build(self):
        return Builder.load_file('main_app.kv')

MainApp().run()