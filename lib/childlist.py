from imp import reload
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivymd.uix.button import MDFlatButton, MDIconButton, MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivy.metrics import dp
from dotenv import load_dotenv
import os

from lib.login import LoginScreen
load_dotenv()
#for the HTTP 
from kivy.network.urlrequest import UrlRequest
import json
LISTURL = os.getenv('LISTURL')

Builder.load_file('lib/kv/childlist.kv')

class ChildListScreen(Screen):
    box_status = False
    dialog = None
    parent_username = ''
    token = ''
    child_length = 0
    child_data = {}
    child_id = ''
    child = ''
    indxSize = 0

    def on_pre_enter(self, *args):
        print('communicating..')
        with open('lib/bin/SavedLogin.json') as json_file:
            data = json.load(json_file)
            json_object = json.loads(data)

        if json_object["checkvalue"] == "True":
            print('Loading saved list')
            ChildListScreen.parent_username = json_object["username"]
            self.token = json_object["token"]
            LoginScreen.token = self.token
        else:
            ChildListScreen.parent_username = LoginScreen.username
            self.token = LoginScreen.token
        
        # On Success Message of below's request 
        def successrequest(self,*args):
            print ("Success request")
            print("Result is " + str(childRequest.result))
            offlinesavedinfo = json.dumps(childRequest.result)

            with open('lib/bin/ChildlistInfo.json','w') as outfile:
                json.dump(offlinesavedinfo,outfile)
            ChildListScreen.child_data = childRequest.result
            ChildListScreen.child_length = len(childRequest.result)
            load_Box()

        def load_offline(self,*args):
            print('Offline Mode')
            with open('lib/bin/ChildlistInfo.json') as json_file:
                offlinechildlist = json.load(json_file)           #loads the file
            loadedfile = json.loads(offlinechildlist)         #parses it so python can use it 
            ChildListScreen.child_data = loadedfile         
            ChildListScreen.child_length = len(loadedfile)

        # On Fail Message of below's request 
        def failedrequest(self,*args):
            print ("Failed Request") # show error message
            print ("Result is "+ str(childRequest.result))

        def load_Box():
            self.on_enter()
            # To double check if the box has been generated or not
            if self.box_status == False:
                self.on_enter()
        
        params = json.dumps({"parent_username" : ChildListScreen.parent_username})
        headers= {'Content-type':'application/json','Accept':'text/plain', 'token': self.token}
        print(params)
        childRequest = UrlRequest(LISTURL, on_success= successrequest, on_failure=failedrequest,timeout = 5, on_error= load_offline,req_body=params, req_headers=headers)
        
        return super().on_enter(*args)

    def on_enter(self, *args):
        if not self.child_data:
            self.box_status = False
            print('No data entered yet')
        else:
            self.box_status = True
            print('loading box')
            for i in range(0, self.child_length):
                card = MDCard(
                    spacing = dp(15),
                    padding = dp(40),
                    orientation = 'vertical',
                    size_hint = (None, 1),
                    width = dp(175),
                    elevation = 10
                )
                self.ids['card'+str(i+1)] = card
                self.ids.scroll_button.add_widget(card)

                icon_btn = MDIconButton(
                    icon = 'account',
                    user_font_size = dp(125),
                    theme_text_color = 'Custom',
                    text_color = '00BFA5',
                    pos_hint = {'center_x': .5}
                )
                self.ids['btn'+str(i+1)] = icon_btn
                self.ids['btn'+str(i+1)].bind(on_release = lambda x: goto_Menu())
                self.ids['card'+str(i+1)].add_widget(icon_btn)

                label = MDLabel(
                    text = str(self.child_data[i]['student_name']),
                    font_size = dp(20),
                    halign = 'center',
                    size_hint = (1, None),
                    height = dp(20)
                )
                self.ids['card'+str(i+1)].add_widget(label)

        def goto_Menu():
            for i in range(0, self.child_length):
                if self.ids['btn'+str(i+1)].state == 'down':
                    print('Entered as: ' + str(self.child_data[i]['student_name']) + '\nID: ' + str(self.child_data[i]['id']))
                    ChildListScreen.child = str(self.child_data[i]['student_name'])
                    ChildListScreen.child_id = str(self.child_data[i]['id'])
                    self.manager.current = 'menu'

        print('done')
        return super().on_enter(*args)

    def on_logout(self):
        self.dialog = MDDialog(
            title = "Do you really want to logout?",
            text = 'This will exit and logout the account',
            size_hint = (.6, None),
            buttons = [
                MDRaisedButton(
                    text = "Logout",
                    on_release = lambda x: logout(),
                    md_bg_color = (.8, 0, 0, 1)
                ),
                MDFlatButton(
                    text="Close",
                    on_release = lambda x: self.dialog.dismiss()
                ),
            ],
            
        )
        self.dialog.open()

        def logout():
            ChildListScreen.parent_username = ''
            emptyinfo = json.dumps({"checkvalue":"False"})
            with open('lib/bin/SavedLogin.json','w') as outfile:
                json.dump(emptyinfo,outfile)

            self.token = ''
            self.dialog.dismiss()
            self.manager.current = 'login'
    
    def on_leave(self, *args):
        self.child_data.clear()
        self.ids.scroll_button.clear_widgets()
        return super().on_pre_leave(*args)
    
    # test data
    # def testdata(self):
    #     print(  '\np_user: ' + self.parent_username +
    #             '\n token: ' + self.token +
    #             '\n child_length: ' + str(self.child_length) +
    #             '\n data: ' + str(self.child_data)
    #         )