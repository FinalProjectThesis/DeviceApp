from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty,Clock
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.core.audio import SoundLoader 
#for the HTTP 
from kivy.network.urlrequest import UrlRequest
import json

Builder.load_file('lib/kv/login.kv')

class LoginScreen(Screen):
    username = StringProperty('')
    password = StringProperty('')

    def on_login(self):
        self.username = self.ids.user_input.text
        self.password = self.ids.pass_input.text

        # play music
        sound = SoundLoader.load("assets/music/button_click.wav")
        sound.play()

        # Temp data or easy access out of login, remove for final/actual testing
        # self.username = 'Carmen'
        # self.password = '123'

        if len(str(self.username)) == 0 or len(str(self.password)) == 0:
            print ("both fields are empty") # for debugging
            if len(str(self.username)) == 0:
                # print this at the error label
                print('Please Enter a Username')
                self.ids.user_input.focus = True
                self.ids.user_input.helper_text_mode = 'on_error'
                self.ids.user_input.error = True
                self.ids.user_input.helper_text = 'Please Enter a Username'
                self.ids.user_input.focus = True
            else:
                print("username is full") # erase error label text 
                self.reset_username()
            if len(str(self.password)) == 0:
                # self.ids.pass_msg.text = 'Please Enter Your Password' # print this at the error label
                print('Please Enter a Password')
                self.ids.pass_input.focus = True
                self.ids.pass_input.helper_text_mode = 'on_error'
                self.ids.pass_input.error = True
                self.ids.pass_input.helper_text = 'Please Enter a Password'
                self.ids.pass_input.focus = True
            else:
                print ("password is full") # erase error label text
                self.reset_password()
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
    
            # On Fail Message of below's request 
            def failedrequest(self,*args):
                print ("Failed Request") # show error message
                print ("Result is "+ str(Loginrequest.result))
            
            def display_nosuchuser():
                self.ids.user_input.focus = True
                self.ids.user_input.helper_text_mode = 'on_error'
                self.ids.user_input.error = True
                self.ids.user_input.helper_text = 'No such User!'
                self.ids.user_input.focus = False
                # reset pass_input just in case
                self.reset_password()

            def display_failedauthentication():
                self.ids.pass_input.focus = True
                self.ids.pass_input.helper_text_mode = 'on_error'
                self.ids.pass_input.error = True
                self.ids.pass_input.helper_text = 'Wrong password'
                self.ids.pass_input.focus = False
                # reset user_input just in case
                self.reset_username()
            
            def goto_Childlist():
                # store needed parameters in screenmanager
                self.manager.token = str(Loginrequest.result)
                self.manager.parent_username = Username
                # leave
                self.manager.current = 'childlist'

            # request
            params = json.dumps({"username":Username,"password":Password})
            print (params)
            headers= {'Content-type':'application/json','Accept':'text/plain'}
            Loginrequest =  UrlRequest('https://uslsthesisapi.herokuapp.com/login', on_success= successrequest,on_failure=failedrequest, req_body=params,req_headers=headers)\
    

    def reset_username(self):
        self.ids.user_input.focus = True
        self.ids.user_input.error = False
        self.ids.user_input.helper_text_mode = 'on_focus'
        self.ids.user_input.helper_text = 'Please Enter your Username'
        self.ids.user_input.focus = False

    def reset_password(self):
        self.ids.pass_input.focus = True
        self.ids.pass_input.error = False
        self.ids.pass_input.helper_text_mode = 'on_focus'
        self.ids.pass_input.helper_text = 'Please Enter your Password'
        self.ids.pass_input.focus = False

    def on_pre_leave(self, *args):
        self.ids.user_input.text = ''
        self.ids.pass_input.text = ''
        self.reset_password()
        self.reset_username()
        return super().on_pre_leave(*args)