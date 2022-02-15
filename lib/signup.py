from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.properties import StringProperty

#for the HTTP 
from kivy.network.urlrequest import UrlRequest
import json

Builder.load_file('lib/signup.kv')

class SignupScreen(Screen):
    username = StringProperty('')
    first_name = StringProperty('')
    last_name = StringProperty('')
    password = StringProperty('')
    confirm_password = StringProperty('')

    def btn_register_function(self):
        self.username = self.ids.user_input.text
        self.first_name = self.ids.first_input.text
        self.last_name = self.ids.last_input.text
        self.password = self.ids.pass_input.text
        self.confirm_password = self.ids.confirmpass_input.text

        # Testing Inputs
        # params = {'Username' : self.username, 'FirstName' : self.first_name, 'LastName' : self.last_name, 'Password' : self.password, 'ConfirmPass' : self.confirm_password}
        # print('Parameters Inputted:\n' + str(params))

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