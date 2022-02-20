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
    score = 0
    Sum = 0
    counter = 1

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
        val1 = random.randint(1, 10)
        val2 = random.randint(1, 10)
        self.Sum = val1 + val2
        # generate labels
        self.ids.qcount_label.text = str('Q #' + str(self.counter))
        self.ids.add_label.text = str(val1) + ' + ' + str(val2)
        print(str(self.counter))
    
    def load_medium(self):
        val1 = random.randint(10, 100)
        val2 = random.randint(10, 100)
        self.Sum = val1 + val2
        # generate labels
        self.ids.qcount_label.text = str('Q #' + self.counter)
        # self.ids.add_label.text = str(val1) + ' + ' + str(val2)
    
    def load_hard(self):
        val1 = random.randint(100, 1000)
        val2 = random.randint(100, 1000)
        self.Sum = val1 + val2
        # generate labels
        self.ids.qcount_label.text = str('Q #' + self.counter)
        # self.ids.add_label.text = str(val1) + ' + ' + str(val2)

    def validate_ans(self):
        final_input = self.ids.thousands_input.text + self.ids.hundreds_input.text + self.ids.tens_input.text + self.ids.ones_input.text
        if len(final_input) == 0:
            final_input = 0
        
        if self.Sum == int(final_input):
            self.ids.add_label.text = 'Correct!'
        else:
            self.ids.add_label.text = 'Wrong Answer, sum is = ' + str(self.Sum)
        
        # reload question then move to next question
        if DifficultyScreen.difficulty == 'easy':
            if self.counter < 10:
                self.counter += 1
                self.load_easy()
            else:
                self.manager.current = 'result'
        elif DifficultyScreen.difficulty == 'medium':
            if self.counter <= 10:
                self.load_medium()
                self.counter += 1
            else:
                pass
        elif DifficultyScreen.difficulty == 'hard':
            if self.counter <= 10:
                self.load_hard()
                self.counter += 1
            else:
                pass
        

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

class ResultScreen(Screen):
    
    def on_pre_enter(self, *args):
        self.ids.result_label.text = 'Finished!'
        return super().on_pre_enter(*args)