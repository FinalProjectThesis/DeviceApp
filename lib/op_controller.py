from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty,Clock
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color


class AdditionScreen(Screen):
    def on_pre_enter(self, *args):
        # load questions?
        return super().on_pre_enter(*args)

class SubtractionScreen(Screen):
    pass

class DivisionScreen(Screen):
    pass

class MultiplicationScreen(Screen):
    pass