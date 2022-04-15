# from kivy.app import App
from kivy.config import Config
Config.set('kivy', 'keyboard_mode','systemanddock')
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.vkeyboard import VKeyboard

from kivy.network.urlrequest import UrlRequest
import os 

ADDSCOREURL = os.getenv('ADDSCOREURL')

# for making it read from the json file on startup ( to parse json )
import json 

# screen imports
from lib.login import LoginScreen
from lib.signup import SignupScreen
from lib.childlist import ChildListScreen
from lib.menu import MenuScreen, DifficultyScreen, ProfileScreen
from lib.op_controller import ADDSCOREURL, OperationScreen, ResultScreen, CorrectScreen, WrongScreen



class WindowManager(ScreenManager):
    pass

class LoadingScreen(Screen):
    counter = 0
    length = 0 
    def on_enter(self, *args):
        Clock.schedule_once(self.execute,2)
        
        return super().on_pre_enter(*args)

    def execute(self, dt):
        #sync
        self.terminate = 0
        self.counter = 0
        self.length = 0
         
        def successrequest(self,*args):
            print("Score Uploaded")
            print ("results: " + str(Scorerequest.result))
            increment_counter()

        def failedrequestortimeout(self,*args):
            print("No internet.")
            set_terminate()

        def set_terminate():
            self.terminate = 1
            
        def increment_counter():
            self.counter += 1 
            if self.counter == self.length:
                clear_stored_scores()

        def clear_stored_scores():
            emptylist = json.dumps({})
            with open('lib/bin/StoredScores.json','w') as json_file:
                emptyjson  = json.dump(emptylist,json_file)
            print ("Emptying Stored JSON")
 
        with open('lib/bin/StoredScores.json') as json_file:
            data = json.load(json_file)
            if str(data) == '{}':
                print ("empty scorelist")
                pass
            else:
                with open('lib/bin/SavedLogin.json') as json_file:
                    data = json.load(json_file)
                json_object = json.loads(data)
                if json_object["checkvalue"] == "False":
                    print("Please login at least once to configure offline mode") 
                else:
                    token =  json_object["token"]
                    with open('lib/bin/StoredScores.json','r') as json_file:
                        data = json.load(json_file)
                    length = len(data)
                    self.length = length
                    print ("self.length is " + str(self.length))
                    print("number of scores is "+ str(length))
                    headers = {'Content-type':'application/json','Accept':'text/plain', 'token':token}
                    for index in range(0,length):
                        print(data[index]["student_name"])
                        params = json.dumps({
                            "student_id":data[index]["student_id"],
                            "student_name":data[index]["student_name"],
                            "date":data[index]["date"],
                            "time": data[index]["time"],
                            "operation":data[index]["operation"],
                            "difficulty":data[index]["difficulty"],
                            "rawscore":data[index]["rawscore"],
                            "totalscore":data[index]["totalscore"]
                        })         
                        #if self.test == 1:
                        #    break
                        print (self.counter)   
                        Scorerequest =  UrlRequest(ADDSCOREURL + '/' + str(data[index]["student_id"]) , on_success = successrequest,timeout = 5,on_error = failedrequestortimeout, req_body = params, req_headers = headers)
                    
        with open('lib/bin/SavedLogin.json') as json_file:
            data = json.load(json_file)
            json_object = json.loads(data)
            if json_object["checkvalue"] == "True":
                ChildListScreen.parent_username = json_object["username"]
                ChildListScreen.token = json_object["token"] 
                print ("proceed to childlist")
                print ("extracted value " + json_object["username"])
                self.manager.current = 'childlist'
            else:
                print("empty, proceed to login")
                self.manager.current = 'login'
        
class MainApp(MDApp):
    def build(self):
        # print("Playing Song")
        # sound = SoundLoader.load('assets/music/general_bg_music.wav')
        # sound.loop = True
        # sound.play()
        self.theme_cls.primary_palette = "Blue"
        
        return Builder.load_file('lib/kv/mainapp.kv')
    
    # def on_start(self):
    #     self.fps_monitor_start()    # to check speed on rasp
            
MainApp().run()