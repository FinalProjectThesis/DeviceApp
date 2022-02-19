from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty,Clock
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color

Builder.load_file('lib/kv/menu.kv')

class MenuScreen(Screen):
    operation = StringProperty('')

    def on_addition(self):
        MenuScreen.operation = 'addition'
    
    def on_subtraction(self):
        MenuScreen.operation = 'subtraction'

    def on_multiplication(self):
        MenuScreen.operation = 'multiplication'
    
    def on_division(self):
        MenuScreen.operation = 'division'
    
class DifficultyScreen(Screen):
    difficulty = StringProperty('')
    operation = StringProperty('')
    
    def on_pre_enter(self, *args):
        DifficultyScreen.operation = MenuScreen.operation
        self.ids.op_label.text = self.operation.capitalize()
        return super().on_pre_enter(*args)

    def on_easy(self):
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
        DifficultyScreen.difficulty = 'hard'
        if self.operation == 'addition':
            self.manager.current = 'addition'
        elif self.operation == 'subtraction':
            self.manager.current = 'subtraction'
        elif self.operation == 'multiplication':
            self.manager.current = 'multiplication'
        elif self.operation == 'division':
            self.manager.current = 'division'