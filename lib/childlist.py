from imp import reload
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.metrics import dp
from kivy.properties import StringProperty
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
    loadBox = True
    parent_username = ''
    token = ''
    child_length = 0
    child_data = {}
    child_id = ''
    child = ''
    indxSize = 0

    def on_pre_enter(self, *args):
        print('communicating..')
        with open('SavedLogin.json') as json_file:
            data = json.load(json_file)
            json_object = json.loads(data)
        if json_object["checkvalue"] == "True":
            print('Loading saved list')
        else:
            self.parent_username = LoginScreen.username
            self.token = LoginScreen.token
        
        # On Success Message of below's request 
        def successrequest(self,*args):
            print ("Success request")
            print("Result is " + str(childRequest.result))
            offlinesavedinfo = json.dumps(childRequest.result)

            with open('ChildlistInfo.json','w') as outfile:
                json.dump(offlinesavedinfo,outfile)

            # TEST OPENING OF SAVED FILES *WORKS*
            #if self.manager.connectionstatus == 'connected':

            ChildListScreen.child_data = childRequest.result
            ChildListScreen.child_length = len(childRequest.result)

            #elif self.manager.connectionstatus =='disconnected':

            #with open('ChildlistInfo.json') as json_file:
            #    offlinechildlist = json.load(json_file)           #loads the file
            #    loadedfile = json.loads(offlinechildlist)         #parses it so python can use it 
            #    ChildListScreen.child_data = loadedfile         
            #    ChildListScreen.child_length = len(loadedfile)
            #load the box
            load_Box()

        # On Fail Message of below's request 
        def failedrequest(self,*args):
            print ("Failed Request") # show error message
            print ("Result is "+ str(childRequest.result))

        def load_Box():
            self.on_enter()
        
        params = json.dumps({"parent_username" : self.parent_username})
        headers= {'Content-type':'application/json','Accept':'text/plain', 'token': self.token}
        print(params)
        childRequest = UrlRequest(LISTURL, on_success= successrequest, on_failure=failedrequest, req_body=params, req_headers=headers)
        
        return super().on_enter(*args)

    def on_enter(self, *args):
        if not self.child_data:
            print('No data entered yet')
        else:
            print('loading box')
            print(str(self.child_length))
            for i in range(0, self.child_length):
                size = dp(100)
                b = Button(
                    text = str(self.child_data[i]['student_name']),
                    size_hint = (None, 1), 
                    width = size)
                if self.loadBox == False:
                    print('Passed here')
                    self.remove_widget(self.ids['btn'+str(i+1)])
                    if i+1 == self.indxSize:
                        self.loadBox = True
                        self.indxSize += 1
                        self.on_enter()
                else:
                    print('adding box')
                    self.ids['btn'+str(i+1)] = b
                    self.ids['btn'+str(i+1)].bind(on_press = lambda x: goto_Menu())
                    self.ids.scroll_child.add_widget(b)

        def goto_Menu():
            for i in range(0, self.child_length):
                if self.ids['btn'+str(i+1)].state == 'down':
                    print('Entered as: ' + str(self.child_data[i]['student_name']) + '\nID: ' + str(self.child_data[i]['id']))
                    ChildListScreen.child = str(self.child_data[i]['student_name'])
                    ChildListScreen.child_id = str(self.child_data[i]['id'])
                    self.manager.current = 'menu'

        print('exiting')
        return super().on_enter(*args)

    def on_leave(self, *args):
        self.child_data.clear()
        self.ids.scroll_child.clear_widgets()
        return super().on_pre_leave(*args)
    
    
    
    # test data
    # def testdata(self):
    #     print(  '\np_user: ' + self.parent_username +
    #             '\n token: ' + self.token +
    #             '\n child_length: ' + str(self.child_length) +
    #             '\n data: ' + str(self.child_data)
    #         )

class LogoutPop(Popup):
    def on_logout(self):
        emptyinfo = json.dumps({"checkvalue":"False"})

        with open('SavedLogin.json','w') as outfile:
            json.dump(emptyinfo,outfile)