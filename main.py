# from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.vkeyboard import VKeyboard
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

# for making it read from the json file on startup ( to parse json )
import json 

# screen imports
from lib.login import LoginScreen
from lib.signup import SignupScreen
from lib.childlist import ChildListScreen
from lib.menu import MenuScreen, DifficultyScreen
from lib.op_controller import AdditionScreen, SubtractionScreen, MultiplicationScreen, DivisionScreen, ResultScreen, CorrectScreen, WrongScreen

class WindowManager(ScreenManager):
    token = StringProperty('')
    parent_username = StringProperty('')
    student_id = StringProperty('')

class LoadingScreen(Screen):
    def on_enter(self, *args):
        Clock.schedule_once(self.execute,2)
        return super().on_pre_enter(*args)

    def execute(self, dt):
        with open('SavedLogin.json') as json_file:
            data = json.load(json_file)
            json_object = json.loads(data)
            if json_object["checkvalue"] == "True":
                self.manager.parent_username = json_object["username"]
                self.manager.token = json_object["token"] 
                print ("proceed to childlist")
                print ("extracted value " + json_object["username"])
                self.manager.current = 'childlist' # just a placeholder for now. 
            else:
                print("empty, proceed to login")
                self.manager.current = 'login'

class MainApp(MDApp):
    def build(self):
        # print("Playing Song")
        # sound = SoundLoader.load('assets/music/general_bg_music.wav')
        # sound.loop = True
        # sound.play()
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Teal'
        
        return Builder.load_file('lib/kv/mainapp.kv')
    
    # def on_start(self):
    #     self.fps_monitor_start()    # to check speed on rasp
            
MainApp().run()