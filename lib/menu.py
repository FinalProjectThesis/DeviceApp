from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty,Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.core.audio import SoundLoader

from lib.childlist import ChildListScreen

Builder.load_file('lib/kv/menu.kv')

class MenuScreen(Screen):
    operation = StringProperty('')

    def on_pre_enter(self, *args):
        self.ids.menu_toolbar.title = ChildListScreen.child + ' ' + ChildListScreen.child_id
        return super().on_pre_enter(*args)

    def on_addition(self):
        MenuScreen.operation = 'addition'
    
    def on_subtraction(self):
        MenuScreen.operation = 'subtraction'

    def on_multiplication(self):
        MenuScreen.operation = 'multiplication'
    
    def on_division(self):
        MenuScreen.operation = 'division'
    
    def on_exit(self):
        self.manager.current = 'childlist'
    
class DifficultyScreen(Screen):
    difficulty = StringProperty('')
    operation = StringProperty('')

    
    def on_pre_enter(self, *args):
        DifficultyScreen.operation = MenuScreen.operation
        self.ids.op_label.text = self.operation.capitalize()
        return super().on_pre_enter(*args)

    def on_easy(self):
        
        sound = SoundLoader.load("assets/music/button_click.wav")
        sound.play()

        DifficultyScreen.difficulty = 'easy'
        if self.operation == 'addition':
            self.manager.current = 'addition'
        elif self.operation == 'subtraction':
            self.manager.current = 'subtraction'
        elif self.operation == 'multiplication':
            self.manager.current = 'multiplication'
        elif self.operation == 'division':
            self.manager.current = 'division'

    def on_medium(self):

        sound = SoundLoader.load("assets/music/button_click.wav")
        sound.play()

        DifficultyScreen.difficulty = 'medium'
        if self.operation == 'addition':
            self.manager.current = 'addition'
        elif self.operation == 'subtraction':
            self.manager.current = 'subtraction'
        elif self.operation == 'multiplication':
            self.manager.current = 'multiplication'
        elif self.operation == 'division':
            self.manager.current = 'division'
    
    def on_hard(self):

        sound = SoundLoader.load("assets/music/button_click.wav")
        sound.play()
        
        DifficultyScreen.difficulty = 'hard'
        if self.operation == 'addition':
            self.manager.current = 'addition'
        elif self.operation == 'subtraction':
            self.manager.current = 'subtraction'
        elif self.operation == 'multiplication':
            self.manager.current = 'multiplication'
        elif self.operation == 'division':
            self.manager.current = 'division'

            