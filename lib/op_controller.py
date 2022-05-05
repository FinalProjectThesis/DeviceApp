import random

import threading
from threading import Thread

# for UART
import serial
from time import sleep
from kivy.clock import Clock
# for KIVY
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.image import Image
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
from kivy.uix.screenmanager import Screen
from kivy.network.urlrequest import UrlRequest
from kivy.core.audio import SoundLoader
from lib.childlist import ChildListScreen
from lib.login import LoginScreen
from lib.menu import DifficultyScreen, MenuScreen
# hello

from datetime import datetime, date
from dotenv import load_dotenv
import pyttsx3
import json
import os


# engine = pyttsx3.init()
load_dotenv()
ADDSCOREURL = os.getenv('ADDSCOREURL')

Builder.load_file('lib/kv/op_controller.kv')

class OperationScreen(Screen):
    score = 0
    first_val = 0
    second_val = 0
    ones = ''
    tens = ''
    hundreds = ''
    counter = 1
    quiz_length = 10

    def on_pre_enter(self, *args):
        # reset inputs
        self.reset_inputs()
        #enable RFID reading
        background_thread = Thread(target = self.read_micro)
        self.stop_threads = False
        background_thread.start()

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
    
    def read_micro(self):
        ser = serial.Serial ("/dev/ttyS0", 9600) 
        while True:
            received_data = ser.read()
            sleep(0.03)
            data_left = ser.inWaiting()
            received_data += ser.read(data_left)
            decoded_data = received_data.decode('utf-8')
            Scanned_Raw = str(decoded_data)
            Scanned_Pos = Scanned_Raw[0:2]
            Scanned_Value = Scanned_Raw[2:]
            
            if Scanned_Pos == 'P1':
            # check values if available for P1 (ones)
                if Scanned_Value in ('BB84A828BF', '6B31B128C3', '6B32B828C9', '9BB03D2533', 'ABC8332575', '3B894525D2', '9B9140256F', '2B83B42834', '2B59462511', 'FB503F25B1', 'ABB6BE288B', '6B9CAA2875', '4B974625BF'):
                    if Scanned_Value == 'BB84A828BF':
                        self.ids.ones_input.source = 'assets/images/ones/0.png'
                        self.ones = '0'
                    elif Scanned_Value == '6B31B128C3':
                        self.ids.ones_input.source = 'assets/images/ones/1.png'
                        self.ones = '1'
                    elif Scanned_Value == '6B32B828C9':
                        self.ids.ones_input.source = 'assets/images/ones/2.png'
                        self.ones = '2'
                    elif Scanned_Value == '9BB03D2533':
                        self.ids.ones_input.source = 'assets/images/ones/3.png'
                        self.ones = '3'
                    elif Scanned_Value == 'ABC8332575':
                        self.ids.ones_input.source = 'assets/images/ones/4.png'
                        self.ones = '4'
                    elif Scanned_Value == '3B894525D2':
                        self.ids.ones_input.source = 'assets/images/ones/5.png'
                        self.ones = '5'
                    elif Scanned_Value == '9B9140256F':
                        self.ids.ones_input.source = 'assets/images/ones/6.png'
                        self.ones = '6'
                    elif Scanned_Value == '2B83B42834':
                        self.ids.ones_input.source = 'assets/images/ones/7.png'
                        self.ones = '7'
                    elif Scanned_Value == '2B59462511':
                        self.ids.ones_input.source = 'assets/images/ones/8.png'
                        self.ones = '8'
                    elif Scanned_Value == 'FB503F25B1':
                        self.ids.ones_input.source = 'assets/images/ones/9.png'
                        self.ones = '9'
                    else:
                        self.ids.ones_input.source = 'assets/images/trans_bg.png'
                        self.ones = ''
                else:
                    Clock.schedule_once(lambda dt: self.error_snackbar(), 1.5)
            elif Scanned_Pos == 'P2':
            # check values if available for P2 (tens)
                if Scanned_Value in ('6B74B22885', '8BAEB228BF', '1B8CB28F0', '3BF3D252C', '8BB12C2533', '1B624D2511', '9BD5AD28CB', '1BC6A9285C', 'EBD6C428D1', '6B1F472516', 'ABB6BE288B', '6B9CAA2875', '4B974625BF'):
                    if Scanned_Value == '6B74B22885':
                        self.ids.tens_input.source = 'assets/images/tens/0.png'
                        self.tens = '0'
                    elif Scanned_Value == '8BAEB228BF':
                        self.ids.tens_input.source = 'assets/images/tens/1.png'
                        self.tens = '1'
                    elif Scanned_Value == '1B8CB28F0':
                        self.ids.tens_input.source = 'assets/images/tens/2.png'
                        self.tens = '2'
                    elif Scanned_Value == '3BF3D252C':
                        self.ids.tens_input.source = 'assets/images/tens/3.png'
                        self.tens = '3'
                    elif Scanned_Value == '8BB12C2533':
                        self.ids.tens_input.source = 'assets/images/tens/4.png'
                        self.tens = '4'
                    elif Scanned_Value == '1B624D2511':
                        self.ids.tens_input.source = 'assets/images/tens/5.png'
                        self.tens = '5'
                    elif Scanned_Value == '9BD5AD28CB':
                        self.ids.tens_input.source = 'assets/images/tens/6.png'
                        self.tens = '6'
                    elif Scanned_Value == '1BC6A9285C':
                        self.ids.tens_input.source = 'assets/images/tens/7.png'
                        self.tens = '7'
                    elif Scanned_Value == 'EBD6C428D1':
                        self.ids.tens_input.source = 'assets/images/tens/8.png'
                        self.tens = '8'
                    elif Scanned_Value == '6B1F472516':
                        self.ids.tens_input.source = 'assets/images/tens/9.png'
                        self.tens = '9'
                    else:
                        self.ids.tens_input.source = 'assets/images/trans_bg.png'
                        self.tens = ''
                else:
                    Clock.schedule_once(lambda dt: self.error_snackbar(), 1.5)
            elif Scanned_Pos == 'P3':
            # check values if available for P3 (hundreds)
                if Scanned_Value in ('1BB7BE283A', '7BD3B92839', 'EB7D4625F5', '1B24382522', '4B72C728D6', '6B1F58259', '9B61C72815', '2BBFC6287A', '3B8FBD2821', 'EBBE3A254A', 'ABB6BE288B', '6B9CAA2875', '4B974625BF'):
                    if Scanned_Value == '1BB7BE283A':
                        self.ids.hundreds_input.source = 'assets/images/hundreds/0.png'
                        self.hundreds = '0'
                    elif Scanned_Value == '7BD3B92839':
                        self.ids.hundreds_input.source = 'assets/images/hundreds/1.png'
                        self.hundreds = '1'
                    elif Scanned_Value == 'EB7D4625F5':
                        self.ids.hundreds_input.source = 'assets/images/hundreds/2.png'
                        self.hundreds = '2'
                    elif Scanned_Value == '1B24382522':
                        self.ids.hundreds_input.source = 'assets/images/hundreds/3.png'
                        self.hundreds = '3'
                    elif Scanned_Value == '4B72C728D6':
                        self.ids.hundreds_input.source = 'assets/images/hundreds/4.png'
                        self.hundreds = '4'
                    elif Scanned_Value == '6B1F58259':
                        self.ids.hundreds_input.source = 'assets/images/hundreds/5.png'
                        self.hundreds = '5'
                    elif Scanned_Value == '9B61C72815':
                        self.ids.hundreds_input.source = 'assets/images/hundreds/6.png'
                        self.hundreds = '6'
                    elif Scanned_Value == '2BBFC6287A':
                        self.ids.hundreds_input.source = 'assets/images/hundreds/7.png'
                        self.hundreds = '7'
                    elif Scanned_Value == '3B8FBD2821':
                        self.ids.hundreds_input.source = 'assets/images/hundreds/8.png'
                        self.hundreds = '8'
                    elif Scanned_Value == 'EBBE3A254A':
                        self.ids.hundreds_input.source = 'assets/images/hundreds/9.png'
                        self.hundreds = '9'
                    else:
                        self.ids.hundreds_input.source = 'assets/images/trans_bg.png'
                        self.hundreds = ''
                else:
                    Clock.schedule_once(lambda dt: self.error_snackbar(), 1.5)
            if self.stop_threads:
                return
                
    def error_snackbar(self):
        snackbar = Snackbar(
            text = 'Wrong placement of card!',
            font_size = "16dp",
            snackbar_x = "5dp",
            snackbar_y = "5dp",
            size_hint_x = .7,
            pos_hint = {'center_x': 0.5,'center_y': 0.93},
            bg_color = (1, 0, 0, 1),
            duration = 1
        )
        snackbar.open()
            
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
            self.ids.qcount_label.text = f'Question # {self.counter}'
            self.ids.question_label.text = f'{val1} + {val2} = ?'
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
                self.ids.qcount_label.text = f'Question #{self.counter}'
                self.ids.question_label.text = f'{val1} - {val2} = ?'
        elif MenuScreen.operation == 'multiplication':
            val1 = random.randint(1, 10)
            val2 = random.randint(1, 10)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 * val2
            # generate labels
            self.ids.qcount_label.text = f'Question #{self.counter}'
            self.ids.question_label.text = f'{val1} x {val2} = ???'
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
                self.ids.qcount_label.text = f'Question #{self.counter}'
                self.ids.question_label.text = f'{val1} ÷ {val2} = ???'
        
    
    def load_medium(self):
        # evaluate what operation
        if MenuScreen.operation == 'addition': 
            val1 = random.randint(5, 60)
            val2 = random.randint(5, 60)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 + val2
            # generate labels
            self.ids.qcount_label.text = f'Question #{self.counter}'
            self.ids.question_label.text = f'{val1} + {val2} = ???'
            print(str(self.counter))
        elif MenuScreen.operation == 'subtraction':
            val1 = random.randint(5, 60)
            val2 = random.randint(5, 60)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 - val2
            # check if negative
            if OperationScreen.answer <= 0:
                self.load_medium()
            else:
                # generate labels
                self.ids.qcount_label.text = f'Question #{self.counter}'
                self.ids.question_label.text = f'{val1} - {val2} = ???'
        elif MenuScreen.operation == 'multiplication':
            val1 = random.randint(1, 15)
            val2 = random.randint(10, 30)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 * val2
            # generate labels
            if OperationScreen.answer > 1000:
                self.load_medium()
            else:
                self.ids.qcount_label.text = f'Question #{self.counter}'
                self.ids.question_label.text = f'{val1} x {val2} = ???'
        elif MenuScreen.operation == 'division':
            val1 = random.randint(5, 100)
            val2 = random.randint(5, 100)
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
                self.ids.qcount_label.text = f'Question #{self.counter}'
                self.ids.question_label.text = f'{val1} ÷ {val2} = ???'
            
    def load_hard(self):
        # evaluate what operation
        if MenuScreen.operation == 'addition':
            val1 = random.randint(45, 150)
            val2 = random.randint(45, 150)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 + val2
            # generate labels
            self.ids.qcount_label.text = f'Question #{self.counter}'
            self.ids.question_label.text = f'{val1} + {val2} = ???'
            print(str(self.counter))
        elif MenuScreen.operation == 'subtraction':
            val1 = random.randint(45, 150)
            val2 = random.randint(45, 150)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 - val2
            # check if negative
            if OperationScreen.answer <= 0:
                self.load_hard()
            else:
                # generate labels
                self.ids.qcount_label.text = f'Question #{self.counter}'
                self.ids.question_label.text = f'{val1} - {val2} = ???'
        elif MenuScreen.operation == 'multiplication':
            val1 = random.randint(5, 20)
            val2 = random.randint(10, 50)
            # store values to send
            OperationScreen.first_val = val1
            OperationScreen.second_val = val2
            OperationScreen.answer = val1 * val2
            # check if over 1K
            if OperationScreen.answer > 1000:
                self.load_hard()
            else:
                # generate labels
                self.ids.qcount_label.text = f'Question #{self.counter}'
                self.ids.question_label.text = f'{val1} x {val2} = ???'
        elif MenuScreen.operation == 'division':
            val1 = random.randint(5, 200)
            val2 = random.randint(5, 200)
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
                self.ids.qcount_label.text = f'Question #{self.counter}'
                self.ids.question_label.text = f'{val1} ÷ {val2} = ???'

    def validate_ans(self):
        # loading sounds
        self.stop_threads = True # stop the loop 
        correct_sound_ping=SoundLoader.load("assets/music/correct_answer.wav")
        voice_1 = SoundLoader.load("assets/music/voice_excellent_1.wav")
        voice_2 = SoundLoader.load("assets/music/voice_very_good_1.wav")
        voice_3 = SoundLoader.load("assets/music/voice_good_job_1.wav")
        final_input = self.hundreds + self.tens + self.ones
        if len(final_input) == 0:
            final_input = 0
        self.counter += 1
        if self.answer == int(final_input):
            OperationScreen.score += 1
            correct_sound_ping.play()
            success_voice = random.randint(1,3)
            print ("success_voice_choice is " + str(success_voice))
            if success_voice ==1:
                voice_1.play()
            if success_voice ==2:    
                voice_2.play()
            if success_voice ==3:    
                voice_3.play()
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
            self.reset_inputs()
            self.stop_threads = True
            self.dialog.dismiss()
            self.manager.current = 'menu'
            self.score = 0
            self.counter = 1
    
    def reset_inputs(self):
        self.ids.hundreds_input.source = 'assets/images/trans_bg.png'
        self.ids.tens_input.source = 'assets/images/trans_bg.png'
        self.ids.ones_input.source = 'assets/images/trans_bg.png'

        self.ones = ''
        self.tens = ''
        self.hundreds = ''   
    
class ResultScreen(Screen):
    
    rawscore = 0
    totalscore = 0
    def on_pre_enter(self, *args):
        self.ids.result_label.text = f'Score is\n{OperationScreen.score}/{OperationScreen.quiz_length}'
        Average_score = OperationScreen.score * .6
        if (OperationScreen.score >= Average_score):
            above_average_sound = SoundLoader.load("assets/music/positive_results.wav")
            above_average_sound.play()
        #else: 
            #below_average_sound = Soundloader.load("assets/music/negative_results.wav")
        
        
        return super().on_pre_enter(*args)
    
    def on_leave(self, *args):
        self.ids.upload_status.text = ""
        OperationScreen.score = 0
        return super().on_leave(*args)
    
    def on_again(self):
        self.manager.current = 'operation'
    
    def on_submit(self):

        def isLoading():
            self.ids.upload_status.text = "Loading, Please Wait"
            self.ids.submit_answers_button.disabled = True
            self.ids.try_again_button.disabled = True

        def isnotLoading():
            self.ids.upload_status.text = ""
            self.ids.submit_answers_button.disabled = False
            self.ids.try_again_button.disabled = False

        isLoading()
        # to get the current date and time 
        self.ids.upload_status.text = "Loading, Please Wait"
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
            isnotLoading()
            print ("Submitted Scores") 
            result =  str(Scorerequest.result)
            print(result)
            print(params)

            # back to menu
            goto_menu()

        # On Fail Message of below's request 
        def failedrequest(self,*args):
            isnotLoading()
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
            isnotLoading()
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
    
    def on_enter(self, *args):
        self.ids.next_btn.disabled = False
        # def run_TTS():
        #     engine.say(f"Answer is Wrong, The Correct answer is {self.Ans}")
            
        #     engine.runAndWait()
        #     self.ids.next_btn.disabled = False
            
        # threading.Thread(
        #     target = run_TTS, daemon=True
        # ).start()
        
        return super().on_enter(*args)
    
    def on_pre_enter(self, *args):
        self.ids.next_btn.disabled = True   # disable button on enter (wait on TTS)
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
            # if val1 > 9:
            #     self.ids.first_grid.rows = 4
            # else:
            #     self.ids.first_grid.rows = 3
                
            for i in range(0, val1):
                truck = Image(
                    source = 'assets/images/truck_apples.png'
                )
                self.ids.first_grid.add_widget(truck)
            # second_grid
            # if val2 > 9:
            #     self.ids.second_grid.rows = 4
            # else:
            #     self.ids.second_grid.rows = 3
                
            for i in range(0, val2):
                truck = Image(
                    source = 'assets/images/truck_apples.png'
                )
                self.ids.second_grid.add_widget(truck)
            # answer_grid
            # if val3 > 9:
            #     self.ids.answer_grid.rows = 4
            # else:
            #     self.ids.answer_grid.rows = 3
                
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
            # if val1 > 9:
            #     self.ids.first_grid.rows = 4
            # else:
            #     self.ids.first_grid.rows = 3
                
            for i in range(0, val1):
                basket = Image(
                    source = 'assets/images/basket_apples.png'
                )
                self.ids.first_grid.add_widget(basket)
            # second_grid
            # if val2 > 9:
            #     self.ids.second_grid.rows = 4
            # else:
            #     self.ids.second_grid.rows = 3
                
            for i in range(0, val2):
                basket = Image(
                    source = 'assets/images/basket_apples.png'
                )
                self.ids.second_grid.add_widget(basket)
            # answer_grid
            # if val3 > 9:
            #     self.ids.answer_grid.rows = 4
            # else:
            #     self.ids.answer_grid.rows = 3
                
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
            # if remain1 > 9:
            #     self.ids.first_grid.rows = 4
            # else:
            #     self.ids.first_grid.rows = 3
                
            for i in range(0, remain1):
                apple = Image(
                    source = 'assets/images/apple.png'
                )
                self.ids.first_grid.add_widget(apple)
            # second_grid
            # if remain2 > 9:
            #     self.ids.second_grid.rows = 4
            # else:
            #     self.ids.second_grid.rows = 3
                
            for i in range(0, remain2):
                apple = Image(
                    source = 'assets/images/apple.png'
                )
                self.ids.second_grid.add_widget(apple)
            # answer_grid
            # if remain3 > 9:
            #     self.ids.answer_grid.rows = 4
            # else:
            #     self.ids.answer_grid.rows = 3
                
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