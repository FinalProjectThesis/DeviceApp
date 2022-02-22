import random
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, NumericProperty, Clock
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color

from lib.menu import DifficultyScreen

# To add sound
from kivy.core.audio import SoundLoader

Builder.load_file('lib/kv/op_controller.kv')

class AdditionScreen(Screen):
    score = 0
    Sum = 0
    counter = 1

    def on_pre_enter(self, *args):
        # self.ids.add_label.text = DifficultyScreen.difficulty
        # reset inputs
        self.reset_inputs()

        # evaluate
        if self.counter > 10:
            print('counter is '+ str(self.counter))
            self.manager.current = 'result'
            AdditionScreen.score = 0
            self.counter = 1
        else:
            # conditions will load the answers
            if DifficultyScreen.difficulty == 'easy':
                self.load_easy()
            elif DifficultyScreen.difficulty == 'medium':
                self.load_medium()
            elif DifficultyScreen.difficulty == 'hard':
                self.load_hard()
        
        return super().on_pre_enter(*args)
    
    def load_easy(self):
        val1 = random.randint(1, 10)
        val2 = random.randint(1, 10)
        AdditionScreen.Sum = val1 + val2
        # generate labels
        self.ids.qcount_label.text = str('Q #' + str(self.counter))
        self.ids.add_label.text = str(val1) + ' + ' + str(val2)
        print(str(self.counter))
    
    def load_medium(self):
        val1 = random.randint(10, 100)
        val2 = random.randint(10, 100)
        AdditionScreen.Sum = val1 + val2
        # generate labels
        self.ids.qcount_label.text = str('Q #' + str(self.counter))
        self.ids.add_label.text = str(val1) + ' + ' + str(val2)
        print(str(self.counter))
    
    def load_hard(self):
        val1 = random.randint(50, 1000)
        val2 = random.randint(50, 1000)
        AdditionScreen.Sum = val1 + val2
        # generate labels
        self.ids.qcount_label.text = str('Q #' + str(self.counter))
        self.ids.add_label.text = str(val1) + ' + ' + str(val2)
        print(str(self.counter))

    def validate_ans(self):

        

        final_input = self.ids.thousands_input.text + self.ids.hundreds_input.text + self.ids.tens_input.text + self.ids.ones_input.text
        if len(final_input) == 0:
            final_input = 0

        if DifficultyScreen.difficulty == 'easy':
            self.counter += 1
            if self.Sum == int(final_input):
                AdditionScreen.score += 1
                # move to correct screen
                # play correct_answer on correct screen ( I'll add them into functions ;-;)
                sound = SoundLoader.load("assets/music/correct_answer.wav")
                sound.play()
                self.manager.current = 'correct'
            else:
                # move to wrong screen
                #play wrong_answer on wrong screen
                sound = SoundLoader.load("assets/music/wrong_answer.wav")
                sound.play()
                self.manager.current = 'wrong'
            
        elif DifficultyScreen.difficulty == 'medium':
            self.counter += 1
            if self.Sum == int(final_input):
                AdditionScreen.score += 1
                # move to correct screen
                self.manager.current = 'correct'
            else:
                # move to wrong screen
                self.manager.current = 'wrong'
        elif DifficultyScreen.difficulty == 'hard':
            self.counter += 1
            if self.Sum == int(final_input):
                AdditionScreen.score += 1
                # move to correct screen
                self.manager.current = 'correct'
            else:
                # move to wrong screen
                self.manager.current = 'wrong'
    
    def on_exit(self):
        self.manager.current = 'menu'
        self.score = 0
        self.counter = 1
    
    def reset_inputs(self):
        self.ids.thousands_input.text = ''
        self.ids.hundreds_input.text = ''
        self.ids.tens_input.text = ''
        self.ids.ones_input.text = ''
    

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
        self.ids.result_label.text = 'Scores is ' + str(AdditionScreen.score) + '/10'
        return super().on_pre_enter(*args)

class CorrectScreen(Screen):
    pass

class WrongScreen(Screen):
    def on_pre_enter(self, *args):
        self.ids.wrong_label.text = 'Wrong Answer, sum is = ' + str(AdditionScreen.Sum)
        return super().on_pre_enter(*args)
    
    def on_next(self):
        pass