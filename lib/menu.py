from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.core.audio import SoundLoader

from lib.childlist import ChildListScreen

Builder.load_file('lib/kv/menu.kv')

class MenuScreen(Screen):
    dialog = None
    operation = StringProperty('')

    def on_pre_enter(self, *args):
        # app = MDApp.get_running_app()
        self.ids.menu_toolbar.title = ChildListScreen.child

        def set_icon_properties(i):
            counter = 0
            for icon in self.ids.menu_toolbar.ids.right_actions.children:
                counter += 1
                if counter == len(self.ids.menu_toolbar.ids.right_actions.children) - (len(self.ids.menu_toolbar.ids.right_actions.children) - 1):
                    icon.text_color = (210/255, 4/255, 45/255, 1)
            
            for icon in self.ids.menu_toolbar.ids.left_actions.children:
                icon.user_font_size = dp(28)

        Clock.schedule_once(set_icon_properties)

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
        self.dialog = MDDialog(
            title = "Do you really want to Exit?",
            text = 'This will exit and take you to the profile screen',
            size_hint = (.6, None),
            buttons = [
                MDRaisedButton(
                    text = "Back to Profile",
                    on_release = lambda x: exit(),
                    md_bg_color = (.8, 0, 0, 1)
                ),
                MDFlatButton(
                    text="Close",
                    on_release = lambda x: self.dialog.dismiss()
                ),
            ],
        )
        self.dialog.open()

        def exit():
            self.dialog.dismiss()
            self.manager.current = 'childlist'
    
    def on_profile(self):
        self.manager.current = 'profile'
    
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

class ProfileScreen(Screen):
    pass            