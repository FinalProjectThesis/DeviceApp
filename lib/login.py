from cgitb import text
from logging import root
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty,Clock
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color

#for the HTTP 
from kivy.network.urlrequest import UrlRequest
import json

Builder.load_file('lib/login.kv')
class LoginScreen(Screen):
    username = StringProperty('')
    password = StringProperty('')

    def clear_TextInput(self):
        self.ids.user_input.text = ''
        self.ids.pass_input.text = ''

    def btn_login_function(self):
        # self.username = self.ids.user_input.text
        # self.password = self.ids.pass_input.text

        # Temp data or easy access out of login, remove for final/actual testing
        self.username = 'Carmen'
        self.password = '123'

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
                print ("Success request") # GOTO next screen
                print("Result is " + str(Loginrequest.result))
                goto_Childlist()

            # On Fail Message of below's request 
            def failedrequest(self,*args):
                print ("Failed Request") # show error message
                print ("Result is "+ str(Loginrequest.result))

            # Move to next screen
            def goto_Childlist():
                self.manager.current = 'childlist'
                self.manager.token = str(Loginrequest.result) # store token in screen manager
                self.clear_TextInput()

            # requests through KIVY's own thing
            params = json.dumps({"username":Username,"password":Password})
            print (params)
            headers= {'Content-type':'application/json','Accept':'text/plain'}
            Loginrequest = UrlRequest('https://uslsthesisapi.herokuapp.com/login', on_success= successrequest,on_failure=failedrequest, req_body=params,req_headers=headers)