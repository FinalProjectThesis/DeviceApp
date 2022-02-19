import random
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, Clock
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color

from lib.menu import DifficultyScreen

Builder.load_file('lib/kv/op_controller.kv')


class AdditionScreen(Screen):
    score = StringProperty('')
    Sum = 0

    def on_pre_enter(self, *args):
        self.ids.add_label.text = DifficultyScreen.difficulty
        if DifficultyScreen.difficulty == 'easy':
            self.load_easy()
        elif DifficultyScreen.difficulty == 'medium':
            pass
        elif DifficultyScreen.difficulty == 'hard':
            pass
        
        # conditions will load the answers
        return super().on_pre_enter(*args)
    
    def load_easy(self):
        val1 = random.randint(0, 10)
        val2 = random.randint(0, 10)
        self.Sum = val1 + val2

        self.ids.add_label.text = str(val1) + ' + ' + str(val2)

    def validate_ans(self):
        if self.Sum == int(self.ids.add_ans_input.text):
            self.ids.add_label.text = 'Correct!'
        else:
            self.ids.add_label.text = 'Wrong Answer, sum is = ' + str(self.Sum)
        
        

class SubtractionScreen(Screen):
    def on_pre_enter(self, *args):
        self.ids.sub_label.text = DifficultyScreen.difficulty
        return super().on_pre_enter(*args)

class MultiplicationScreen(Screen):
    def on_pre_enter(self, *args):
        self.ids.multi_label.text = DifficultyScreen.difficulty
        return super().on_pre_enter(*args)

class DivisionScreen(Screen):
    def on_pre_enter(self, *args):
        self.ids.div_label.text = DifficultyScreen.difficulty
        return super().on_pre_enter(*args)