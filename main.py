from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
# screen imports
from lib.login import LoginScreen
from lib.signup import SignupScreen
from lib.childlist import ChildListScreen
from lib.menu import MenuScreen, DifficultyScreen
from lib.op_controller import AdditionScreen, SubtractionScreen, MultiplicationScreen, DivisionScreen, ResultScreen, CorrectScreen, WrongScreen
from kivy.core.audio import SoundLoader
class WindowManager(ScreenManager):
    token = StringProperty('')
    parent_username = StringProperty('')
    student_id = StringProperty('')

sm = ScreenManager()
sm.add_widget(LoginScreen(name = 'login'))
sm.add_widget(SignupScreen(name = 'signup'))
sm.add_widget(ChildListScreen(name = 'childlist'))
sm.add_widget(MenuScreen(name = 'menu'))
sm.add_widget(DifficultyScreen(name = 'difficulty'))
sm.add_widget(ResultScreen(name = 'result'))
sm.add_widget(CorrectScreen(name = 'correct'))
sm.add_widget(WrongScreen(name = 'wrong'))
# Operations
sm.add_widget(AdditionScreen(name = 'addition'))
sm.add_widget(DivisionScreen(name = 'division'))
sm.add_widget(MultiplicationScreen(name = 'multiplication'))
sm.add_widget(SubtractionScreen(name = 'subtraction'))

class MainApp(App):
    def build(self):
        # print("Playing Song")
        # sound = SoundLoader.load('test.wav')
        # sound.loop = True
        # sound.play()
    
        return Builder.load_file('lib/kv/mainapp.kv')
        
        
MainApp().run()