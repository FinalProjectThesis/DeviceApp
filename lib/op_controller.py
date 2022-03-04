import random
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.image import Image
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest
from kivy.core.audio import SoundLoader

from lib.childlist import ChildListScreen
from lib.login import LoginScreen
from lib.menu import DifficultyScreen, MenuScreen

from datetime import datetime, date
from dotenv import load_dotenv
import json
import os

load_dotenv()
ADDSCOREURL = os.getenv('ADDSCOREURL')

Builder.load_file('lib/kv/op_controller.kv')

# initialializing TTS 
import pyttsx3
engine = pyttsx3.init()
class OperationScreen(Screen):
    score = 0
    first_val = 0
    second_val = 0
    answer = 0
    counter = 1
    quiz_length = 15

    def on_pre_enter(self, *args):
        # reset inputs
        self.reset_inputs()

        # evaluate
        if self.counter > self.quiz_length:
            print('counter is '+ str(self.counter))
            self.manager.current = 'result'
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
        # evaluate what operation
        if MenuScreen.operation == 'addition':
            val1 = random.randint(1, 10)
            val2 = random.randint(1, 10)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 + val2
            # generate labels
            self.ids.qcount_label.text = str('Q #' + str(self.counter))
            self.ids.question_label.text = str(val1) + ' + ' + str(val2)
            print(str(self.counter))
        elif MenuScreen.operation == 'subtraction':
            val1 = random.randint(1, 10)
            val2 = random.randint(1, 10)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 - val2
            # check if negative
            if OperationScreen.answer <= 0:
                self.load_easy()
            else:
                # generate labels
                self.ids.qcount_label.text = str('Q #' + str(self.counter))
                self.ids.question_label.text = str(val1) + ' - ' + str(val2)
        elif MenuScreen.operation == 'multiplication':
            val1 = random.randint(1, 10)
            val2 = random.randint(1, 10)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 * val2
            # generate labels
            self.ids.qcount_label.text = str('Q #' + str(self.counter))
            self.ids.question_label.text = str(val1) + ' x ' + str(val2)
        elif MenuScreen.operation == 'division':
            val1 = random.randint(1, 20)
            val2 = random.randint(1, 20)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 // val2
            remainder_check = val1 % val2
            # check if if there is remainder
            if remainder_check != 0:
                self.load_easy()
            else:
                # generate labels
                self.ids.qcount_label.text = str('Q #' + str(self.counter))
                self.ids.question_label.text = str(val1) + ' ÷ ' + str(val2)
        
    
    def load_medium(self):
        # evaluate what operation
        if MenuScreen.operation == 'addition': 
            val1 = random.randint(10, 100)
            val2 = random.randint(10, 100)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 + val2
            # generate labels
            self.ids.qcount_label.text = str('Q #' + str(self.counter))
            self.ids.question_label.text = str(val1) + ' + ' + str(val2)
            print(str(self.counter))
        elif MenuScreen.operation == 'subtraction':
            val1 = random.randint(10, 100)
            val2 = random.randint(10, 100)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 - val2
            # check if negative
            if OperationScreen.answer <= 0:
                self.load_medium()
            else:
                # generate labels
                self.ids.qcount_label.text = str('Q #' + str(self.counter))
                self.ids.question_label.text = str(val1) + ' - ' + str(val2)
        elif MenuScreen.operation == 'multiplication':
            val1 = random.randint(1, 10)
            val2 = random.randint(10, 50)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 * val2
            # generate labels
            if OperationScreen.answer > 1000:
                self.load_medium()
            else:
                self.ids.qcount_label.text = str('Q #' + str(self.counter))
                self.ids.question_label.text = str(val1) + ' x ' + str(val2)
        elif MenuScreen.operation == 'division':
            val1 = random.randint(10, 100)
            val2 = random.randint(1, 100)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 // val2
            remainder_check = val1 % val2
            # check if there is remainder
            if remainder_check != 0:
                self.load_medium()
            else:
                # generate labels
                self.ids.qcount_label.text = str('Q #' + str(self.counter))
                self.ids.question_label.text = str(val1) + ' ÷ ' + str(val2)
            
    def load_hard(self):
        # evaluate what operation
        if MenuScreen.operation == 'addition':
            val1 = random.randint(100, 500)
            val2 = random.randint(100, 500)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 + val2
            # generate labels
            self.ids.qcount_label.text = str('Q #' + str(self.counter))
            self.ids.question_label.text = str(val1) + ' + ' + str(val2)
            print(str(self.counter))
        elif MenuScreen.operation == 'subtraction':
            val1 = random.randint(100, 500)
            val2 = random.randint(100, 500)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 - val2
            # check if negative
            if OperationScreen.answer <= 0:
                self.load_hard()
            else:
                # generate labels
                self.ids.qcount_label.text = str('Q #' + str(self.counter))
                self.ids.question_label.text = str(val1) + ' - ' + str(val2)
        elif MenuScreen.operation == 'multiplication':
            val1 = random.randint(10,20)
            val2 = random.randint(10,50)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 * val2
            # check if over 1K
            if OperationScreen.answer > 1000:
                self.load_hard()
            else:
                # generate labels
                self.ids.qcount_label.text = str('Q #' + str(self.counter))
                self.ids.question_label.text = str(val1) + ' x ' + str(val2)
        elif MenuScreen.operation == 'division':
            val1 = random.randint(50, 200)
            val2 = random.randint(1, 200)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 // val2
            remainder_check = val1 % val2
            # check if there is remainder
            if remainder_check != 0:
                self.load_hard()
            else:
                # generate labels
                self.ids.qcount_label.text = str('Q #' + str(self.counter))
                self.ids.question_label.text = str(val1) + ' ÷ ' + str(val2)

    def validate_ans(self):
        final_input = self.ids.thousands_input.text + self.ids.hundreds_input.text + self.ids.tens_input.text + self.ids.ones_input.text
        if len(final_input) == 0:
            final_input = 0

        self.counter += 1
        if self.answer == int(final_input):
            OperationScreen.score += 1
            # play correct_answer on correct screen ( I'll add them into functions ;-;)
            # sound = SoundLoader.load("assets/music/correct_answer.wav")
            # sound.play()
            # move to correct screen
            self.manager.current = 'correct'
        else:
            # move to wrong screen
            # sound = SoundLoader.load("assets/music/wrong_answer.wav")
            # sound.play()
            self.manager.current = 'wrong'  
    
    def on_exit(self):
        self.dialog = MDDialog(
            title = "Go back to Menu?",
            text = "This won't save your score and you will lose you progress",
            size_hint = (.6, None),
            buttons = [
                MDRaisedButton(
                    text = "Back to Menu",
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
            self.manager.current = 'menu'
            self.score = 0
            self.counter = 1
    
    def reset_inputs(self):
        self.ids.thousands_input.text = ''
        self.ids.hundreds_input.text = ''
        self.ids.tens_input.text = ''
        self.ids.ones_input.text = ''
    
class ResultScreen(Screen):
    rawscore = 0
    totalscore = 0
    def on_pre_enter(self, *args):
        self.ids.result_label.text = 'Scores is ' + str(OperationScreen.score) + '/' + str(OperationScreen.quiz_length)
        Average_score = OperationScreen.score * .6
        if (OperationScreen.score >= Average_score):
            above_average_sound = SoundLoader.load("assets/music/positive_results.wav")
            above_average_sound.play()
        #else: 
            #below_average_sound = Soundloader.load("assets/music/negative_results.wav")
        return super().on_pre_enter(*args)
    
    def on_leave(self, *args):
        OperationScreen.score = 0
        return super().on_leave(*args)
    
    def on_submit(self):
        # to get the current date and time 
        current_time = datetime.now()
        current_date = datetime.today()

        child_id = ChildListScreen.child_id
        child_name = ChildListScreen.child
        date = current_date.strftime("%D")
        time = current_time.strftime("%H:%M")
        operation = MenuScreen.operation
        difficulty = DifficultyScreen.difficulty
        rawscore = str(OperationScreen.score)
        totalscore = str(OperationScreen.quiz_length)

        def successrequest(self,*args):
            print ("Submitted Scores") 
            result =  str(Scorerequest.result)
            print(result)
            print(params)

            # back to menu
            goto_menu()

        # On Fail Message of below's request 
        def failedrequest(self,*args):
            print ("Failed Request") # show error message
            print ("Result is "+ str(Scorerequest.result))
        
        def goto_menu():
            self.manager.current = 'menu'
                              
        params = json.dumps({
            "student_id":child_id,
            "student_name":child_name,
            "date":date,
            "time": time,
            "operation":operation,
            "difficulty":difficulty,
            "rawscore":rawscore,
            "totalscore":totalscore
        })
        
        # data that is to be inserted(is a list) if there is no score inside the file
        no_data_params = ([{"student_id":child_id,
            "student_name":child_name,
            "date":date,
            "time": time,
            "operation":operation,
            "difficulty":difficulty,
            "rawscore":rawscore,
            "totalscore":totalscore}])

        # data that is to be inserted(is a list) if there is/are existing score(s) inside the file
        existing_data_params = ({"student_id":child_id,
            "student_name":child_name,
            "date":date,
            "time": time,
            "operation":operation,
            "difficulty":difficulty,
            "rawscore":rawscore,
            "totalscore":totalscore})    
        
        #if there is a timeout, run this code!!
        def on_timeout(self,*args):
            with open("lib/bin/StoredScores.json")as file:
                data = json.load(file)
            if str(data) =='{}':
                print ("Empty List, will now dump params")
                with open('lib/bin/StoredScores.json','w') as outfile:
                    json.dump(no_data_params,outfile,indent = 4)
                    goto_menu()
            else: # if there's already a file inside 
            # Read JSON file
                with open('lib/bin/StoredScores.json') as fp:
                    listObj = json.load(fp)
            # Verify existing list
                listObj.append(existing_data_params)
            # Verify updated list
                print(listObj)
                with open('lib/bin/StoredScores.json', 'w') as json_file:
                    json.dump(listObj, json_file,indent = 4)
                print('Successfully appended to the JSON file')
                goto_menu()
        
        headers = {'Content-type':'application/json','Accept':'text/plain', 'token':LoginScreen.token}
        Scorerequest =  UrlRequest(ADDSCOREURL + '/' + str(ChildListScreen.child_id) , on_success = successrequest,on_error=on_timeout,timeout = 5, on_failure = failedrequest, req_body = params, req_headers = headers)

class CorrectScreen(Screen):
    def on_enter(self, *args):
        self.ids.gif.anim_delay = 1/30
        return super().on_enter(*args)

class WrongScreen(Screen):
    Ans = 0
    first_val = 0
    second_val = 0
    
    def on_pre_enter(self, *args):
        # set and call values
        if MenuScreen.operation == 'addition':
            self.ids.op_label.text = '+'
        elif MenuScreen.operation == 'subtraction':
            self.ids.op_label.text = '-'
        elif MenuScreen.operation == 'multiplication':
            self.ids.op_label.text = 'x'
        else:
            self.ids.op_label.text = '÷'
        
        self.Ans = OperationScreen.answer
        self.first_val = OperationScreen.first_val
        self.second_val = OperationScreen.second_val
        #TTS TEST 
        actual_answer = str(self.Ans)
        engine.say("Answer is Wrong, The Correct answer is " + actual_answer)
        engine.runAndWait()

        self.ids.wrong_label.text = f'Answer is Wrong!\nCorrect answer is [color=#00FF00]{self.Ans}[/color]'
        if self.first_val == 1:
            self.ids.val1_label.text = f'{self.first_val} Apple'
        elif self.second_val == 1:  
            self.ids.val2_label.text = f'{self.second_val} Apple'
        else:
            self.ids.val1_label.text = f'{self.first_val} Apples'
            self.ids.val2_label.text = f'{self.second_val} Apples'
        self.ids.answer_label.text = f'Equals to [color=#ED2939]{self.Ans}[/color] apples!'
        
        def generate_truck(*args):
            val1 = int(args[0]) // 100
            val2 = int(args[1]) // 100
            val3 = int(args[2]) // 100
            remain1 = int(args[0]) % 100
            remain2 = int(args[1]) % 100
            remain3 = int(args[2]) % 100
            
            # first_grid
            if val1 > 9:
                self.ids.first_grid.rows = 4
            else:
                self.ids.first_grid.rows = 3
                
            for i in range(0, val1):
                truck = Image(
                    source = 'assets/images/truck_apples.png'
                )
                self.ids.first_grid.add_widget(truck)
            # second_grid
            if val2 > 9:
                self.ids.second_grid.rows = 4
            else:
                self.ids.second_grid.rows = 3
                
            for i in range(0, val2):
                truck = Image(
                    source = 'assets/images/truck_apples.png'
                )
                self.ids.second_grid.add_widget(truck)
            # answer_grid
            if val3 > 9:
                self.ids.answer_grid.rows = 4
            else:
                self.ids.answer_grid.rows = 3
                
            for i in range(0, val3):
                truck = Image(
                    source = 'assets/images/truck_apples.png'
                )
                self.ids.answer_grid.add_widget(truck)
            
            if remain1 != 0 or remain2 != 0 or remain3 != 0:
                generate_basket(remain1, remain2, remain3)
        
        def generate_basket(*args):
            val1 = int(args[0]) // 10
            val2 = int(args[1]) // 10
            val3 = int(args[2]) // 10
            remain1 = int(args[0]) % 10
            remain2 = int(args[1]) % 10
            remain3 = int(args[2]) % 10
            
            # first_grid
            if val1 > 9:
                self.ids.first_grid.rows = 4
            else:
                self.ids.first_grid.rows = 3
                
            for i in range(0, val1):
                basket = Image(
                    source = 'assets/images/basket_apples.png'
                )
                self.ids.first_grid.add_widget(basket)
            # second_grid
            if val2 > 9:
                self.ids.second_grid.rows = 4
            else:
                self.ids.second_grid.rows = 3
                
            for i in range(0, val2):
                basket = Image(
                    source = 'assets/images/basket_apples.png'
                )
                self.ids.second_grid.add_widget(basket)
            # answer_grid
            if val3 > 9:
                self.ids.answer_grid.rows = 4
            else:
                self.ids.answer_grid.rows = 3
                
            for i in range(0, val3):
                basket = Image(
                    source = 'assets/images/basket_apples.png'
                )
                self.ids.answer_grid.add_widget(basket)
            
            if remain1 != 0 or remain2 != 0 or remain3 != 0:
                generate_apple(remain1, remain2, remain3)
                
        def generate_apple(*args):
            remain1 = int(args[0])
            remain2 = int(args[1])
            remain3 = int(args[2])
            
            # first_grid
            if remain1 > 9:
                self.ids.first_grid.rows = 4
            else:
                self.ids.first_grid.rows = 3
                
            for i in range(0, remain1):
                apple = Image(
                    source = 'assets/images/apple.png'
                )
                self.ids.first_grid.add_widget(apple)
            # second_grid
            if remain2 > 9:
                self.ids.second_grid.rows = 4
            else:
                self.ids.second_grid.rows = 3
                
            for i in range(0, remain2):
                apple = Image(
                    source = 'assets/images/apple.png'
                )
                self.ids.second_grid.add_widget(apple)
            # answer_grid
            if remain3 > 9:
                self.ids.answer_grid.rows = 4
            else:
                self.ids.answer_grid.rows = 3
                
            for i in range(0, remain3):
                apple = Image(
                    source = 'assets/images/apple.png'
                )
                self.ids.answer_grid.add_widget(apple)
        
        if self.first_val >= 100 or self.second_val >= 100 or self.Ans >= 100:
            generate_truck(self.first_val, self.second_val, self.Ans)
        elif self.first_val >= 10 or self.second_val >= 10 or self.Ans >= 10:
            generate_basket(self.first_val, self.second_val, self.Ans)
        elif self.first_val < 10 or self.second_val < 10 or self.Ans < 10:
            generate_apple(self.first_val, self.second_val, self.Ans)
        
        return super().on_pre_enter(*args)
    
    def on_leave(self, *args):
        self.ids.first_grid.clear_widgets()
        self.ids.second_grid.clear_widgets()
        self.ids.answer_grid.clear_widgets()
        return super().on_leave(*args)