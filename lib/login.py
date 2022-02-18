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

Builder.load_file('lib/kv/login.kv')
class LoginScreen(Screen):
    username = StringProperty('')
    password = StringProperty('')

    def btn_login_function(self):
        # self.username = self.ids.user_input.text
        # self.password = self.ids.pass_input.text

        # Temp data or easy access out of login, remove for final/actual testing
        self.username = 'Carmen'
        self.password = '123'

        if len(str(self.username)) == 0 or len(str(self.password)) == 0:
            print ("both fields are empty") # for debugging
            if len(str(self.username)) == 0:
                self.ids.user_msg.text = 'Please Enter a Username' # print this at the error label
            else:
                print("username is full") # erase error label text 
                self.ids.user_msg.text = ''
            if len(str(self.password)) == 0:
                self.ids.pass_msg.text = 'Please Enter Your Password' # print this at the error label
            else:
                print ("password is full") # erase error label text
                self.ids.pass_msg.text = '' 
        else:  # if all checks pass 
            Username = str(self.username)
            Password = str(self.password)
            print("Username : " + Username + "\n" + "Password : " + Password)
            # On Success Message of below's request 
            def successrequest(self,*args):
                print ("Success request") 
                result =  str(Loginrequest.result)
                if result =='No such User':
                    print ("No such User!")
                    display_nosuchuser()
                elif result =='Failed':
                    print("Failed Auth, Wrong Password")
                    display_failedauthentication()
                else:
                    goto_Childlist() # GOTO next screen
            # Display No such User 
            def display_nosuchuser():
                self.ids.user_msg.text = 'No such User!'

            # Display Failed Authentication
            def display_failedauthentication():
                self.ids.pass_msg.text = 'Wrong password'
                self.ids.user_msg.text = ''
                
            # On Fail Message of below's request 
            def failedrequest(self,*args):
                print ("Failed Request") # show error message
                print ("Result is "+ str(Loginrequest.result))
            
            # Move to next screen
            def goto_Childlist():
                # store needed parameters in screenmanager
                self.manager.token = str(Loginrequest.result)
                self.manager.parent_username = Username
                # leave
                self.manager.current = 'childlist'

            # requests through KIVY's own thing
            params = json.dumps({"username":Username,"password":Password})
            print (params)
            headers= {'Content-type':'application/json','Accept':'text/plain'}
            Loginrequest =  UrlRequest('https://uslsthesisapi.herokuapp.com/login', on_success= successrequest,on_failure=failedrequest, req_body=params,req_headers=headers)\
    
    def on_pre_leave(self, *args):
        self.ids.user_input.text = ''
        self.ids.pass_input.text = ''
        return super().on_pre_leave(*args)