from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, Clock
from kivymd.uix.screen import Screen
from kivy.core.audio import SoundLoader 
from dotenv import load_dotenv
import os
load_dotenv()
# for the HTTP 
from kivy.network.urlrequest import UrlRequest
import json
LOGINURL = os.getenv('LOGINURL')

Builder.load_file('lib/kv/login.kv')

class LoginScreen(Screen):
    username = ''
    password = ''
    token = ''
 
    def on_login(self):
        LoginScreen.username = self.ids.user_input.text
        self.password = self.ids.pass_input.text

        #shows when it's loading
        def isloading():
            self.ids.loading_spinner.active = True
            self.ids.login_button.text = "Loading.."
            self.ids.login_button.disabled = True

        def isnotloading():
            self.ids.loading_spinner.active = False
            self.ids.login_button.text = "Login"
            self.ids.login_button.disabled = False
        
        def showconnectionerrormessage():
            self.ids.connection_status.text = "Connection Failed, Please check internet connection"

        def clearconnectionerrormessage():
            self.ids.connection_status.text = ""

        def saveUserInfo():
            if (self.ids.remember_me_checkbox.active == True):
                savedinfo = json.dumps({"checkvalue":"True","username":str(self.username),"password":str(self.password),"token":str(Loginrequest.result)})
                with open('lib/bin/SavedLogin.json','w') as outfile:
                    json.dump(savedinfo,outfile)
            else:
                emptyinfo = json.dumps({"checkvalue":"False"})
                with open('lib/bin/SavedLogin.json','w') as outfile:
                    json.dump(emptyinfo,outfile)

        
        # play music
        sound = SoundLoader.load("assets/music/button_click.wav")
        sound.play()

        # Temp data or easy access out of login, remove for final/actual testing
        #LoginScreen.username = 'Carmen'
        #self.password = '123'

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
            isloading() 
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
                    clearconnectionerrormessage()
                    saveUserInfo()
                    isnotloading()
                    goto_Childlist() # GOTO next screen
            # On Fail Message of below's request 
            def showtimeoutmessage(self,*args):
                isnotloading()
                showconnectionerrormessage()

            def failedrequest(self,*args):
                print ("Failed Request") # show error message
                print ("Result is "+ str(Loginrequest.result))
                isnotloading()

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
            # will display while the program is loading the URL request
            #def whileloading():
                #self.ids.
            def goto_Childlist():
                LoginScreen.token = str(Loginrequest.result)
                # self.manager.parent_username = Username
                # leave
                self.manager.current = 'childlist'

             

            # request
            params = json.dumps({"username":Username,"password":Password})
            print (params)
            headers= {'Content-type':'application/json','Accept':'text/plain'}
            Loginrequest =  UrlRequest(LOGINURL, on_success= successrequest,on_failure=failedrequest,timeout=5,on_error=showtimeoutmessage,req_body=params,req_headers=headers)
        
        
                
    #def on_guest_enter(self):
    #    self.manager.connectionstatus = 'Disconnected'


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
        self.ids.remember_me_checkbox.active = False
        self.reset_password()
        self.reset_username()
        return super().on_pre_leave(*args)