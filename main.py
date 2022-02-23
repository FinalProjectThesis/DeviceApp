# from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.properties import StringProperty
# from kivy.uix.vkeyboard import VKeyboard

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

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

class MainApp(MDApp):
    def build(self):
        # print("Playing Song")
        # sound = SoundLoader.load('assets/music/general_bg_music.wav')
        # sound.loop = True
        # sound.play()
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        
        return Builder.load_file('lib/kv/mainapp.kv')
    
    def on_start(self):
        self.fps_monitor_start()    # to check speed on rasp
   
MainApp().run()