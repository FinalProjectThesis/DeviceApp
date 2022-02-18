from imp import reload
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.properties import StringProperty

#for the HTTP 
from kivy.network.urlrequest import UrlRequest
import json


Builder.load_file('lib/kv/childlist.kv')

class ChildListScreen(Screen):
    loadBox = True
    parent_username = ''
    token = ''
    childLength = 0
    childData = {}
    indxSize = 0
    
    def on_pre_enter(self, *args):
        print('communicating..')
        self.parent_username = self.manager.parent_username
        self.token = self.manager.token
        
        # On Success Message of below's request 
        def successrequest(self,*args):
            print ("Success request")
            print("Result is " + str(childRequest.result))
            ChildListScreen.childData = childRequest.result
            ChildListScreen.childLength = len(childRequest.result)
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
        childRequest = UrlRequest('https://uslsthesisapi.herokuapp.com/childlist', on_success= successrequest, on_failure=failedrequest, req_body=params, req_headers=headers)

        return super().on_enter(*args)
    
    def on_enter(self, *args):
        if not self.childData:
            print('No data entered yet')
        else:
            print('loading box')
            print(str(self.childLength))
            for i in range(0, self.childLength):
                size = dp(100)
                b = Button(
                    text = str(self.childData[i]['student_name']),
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
            self.manager.current = 'menu'

        print('exiting')
        return super().on_enter(*args)

    def on_leave(self, *args):
        self.childData.clear()
        self.ids.scroll_child.clear_widgets()
        return super().on_pre_leave(*args)
    
    # test data
    # def testdata(self):
    #     print(  '\np_user: ' + self.parent_username +
    #             '\n token: ' + self.token +
    #             '\n childLength: ' + str(self.childLength) +
    #             '\n data: ' + str(self.childData)
    #         )