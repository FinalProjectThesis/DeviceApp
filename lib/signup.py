from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.properties import StringProperty

#for the HTTP 
from kivy.network.urlrequest import UrlRequest
import json

Builder.load_file('lib/kv/signup.kv')

class SignupScreen(Screen):
    username = StringProperty('')
    first_name = StringProperty('')
    last_name = StringProperty('')
    password = StringProperty('')
    confirm_password = StringProperty('')

    def on_register(self):
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
                self.ids.user_input.error = True
                self.ids.user_input.helper_text = 'Please enter a username'
                self.ids.user_input.focus = True
                self.ids.user_input.focus = False
            else:
                print("username is full") # erase username error label text 
                self.reset_username()
            if len(str(self.password)) == 0:
                print("please enter a password") # print this at the password error label
                self.ids.pass_input.error = True
                self.ids.pass_input.helper_text = 'Please enter a password'
                self.ids.pass_input.focus = True
                self.ids.pass_input.focus = False
            else:
                print ("password is full") # erase error label text
                self.reset_password()
            if self.password != self.confirm_password:
                print("Password doesn't match") # print this at the confirm_password  error label
                self.ids.confirmpass_input.error = True
                self.ids.confirmpass_input.helper_text = "Password doesn't match"
                self.ids.confirmpass_input.focus = True
                self.ids.confirmpass_input.focus = False
            else:
                self.reset_confirm_pass()
            if len(str(self.first_name)) == 0:
                print("please enter your first name")
                self.ids.first_input.error = True
                self.ids.first_input.helper_text = 'Please Enter your first name'
                self.ids.first_input.focus = True
                self.ids.first_input.focus = False
            else:
                print("firstname is full") # erase first name error label text
                self.reset_firstname()
            if  len(str(self.last_name)) == 0:
                print("please enter your last name ") # print this at the last name  error label
                self.ids.last_input.error = True
                self.ids.last_input.helper_text = 'Please Enter your last name'
                self.ids.last_input.focus = True
                self.ids.last_input.focus = False
            else:
                print("lastname is full") # erase last name error label text
                self.reset_lastname()
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
                to_login()
                
            # On Failed message of below's request             
            def failedrequest(self,*args):
                print ("Failed Request") # show error message 
                print (params)
                print ("Result is "+ str(Registerrequest.result))
            
            def to_login():
                self.manager.current = 'login'
            
            params =json.dumps({"username":Username,"password":Password, "first_name": First_name, "last_name": Last_name})
            print (params)
            headers= {'Content-type':'application/json','Accept':'text/plain'}
            Registerrequest = UrlRequest('https://uslsthesisapi.herokuapp.com/register', on_success= successrequest,on_failure=failedrequest, req_body=params,req_headers=headers)

    def reset_username(self):
        self.ids.user_input.error = False
        self.ids.user_input.focus = True
        self.ids.user_input.focus = False

    def reset_password(self):
        self.ids.pass_input.error = False
        self.ids.pass_input.focus = True
        self.ids.pass_input.focus = False
    
    def reset_confirm_pass(self):
        self.ids.confirmpass_input.error = False
        self.ids.confirmpass_input.helper_text = ''
        self.ids.confirmpass_input.focus = True
        self.ids.confirmpass_input.focus = False

    def reset_firstname(self):
        self.ids.first_input.error = False
        self.ids.first_input.helper_text = ''
        self.ids.first_input.focus = True
        self.ids.first_input.focus = False

    def reset_lastname(self):
        self.ids.last_input.error = False
        self.ids.last_input.helper_text = ''
        self.ids.last_input.focus = True
        self.ids.last_input.focus = False

    def reset_all(self):
        self.reset_username()
        self.reset_password()
        self.reset_confirm_pass()
        self.reset_firstname()
        self.reset_lastname()

    def on_pre_leave(self, *args):
        self.ids.user_input.text = ''
        self.ids.first_input.text = ''
        self.ids.last_input.text = ''
        self.ids.pass_input.text = ''
        self.ids.confirmpass_input.text = ''
        self.reset_all()
        return super().on_pre_leave(*args)