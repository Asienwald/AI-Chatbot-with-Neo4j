from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button

from chatbot_logic import ask_chatbot

class MainWindow(Screen):
    gl =ObjectProperty(None)
    userInput = ObjectProperty(None)
    def btn(self):
        print(self.userInput.text)
        # chatbot output
        
        # add box with user input
        lengthUser = len(self.userInput.text)
        if lengthUser<10:
            label = Label(text=self.userInput.text , size_hint=(None,None), size=(self.width/2, 50) )
            layout = BoxLayout(orientation="horizontal")
            layout.add_widget(Label(text="" ) )
            layout.add_widget(label)
            self.gl.add_widget(layout)
        else:
            times = lengthUser/10
            if type(times)==float:
                times= lengthUser%10 +1

            for i in range(times):
                layout = BoxLayout(orientation="horizontal")
                # layout.add_widget(label)
                # self.gl.add_widget(layout)
                if i ==0:
                    label = Label(text=self.userInput.text[0:10] , size_hint=(None,None), size=(self.width/2, 50) )
                    # layout = BoxLayout(orientation="horizontal")
                    layout.add_widget(Label(text="" ) )
                    layout.add_widget(label)
                    # self.gl.add_widget(layout)
                elif i==times-1:
                    label = Label(text=self.userInput.text[(times-1)*10+1:-1] , size_hint=(None,None), size=(self.width/2, 50) )
                    # layout = BoxLayout(orientation="horizontal")
                    layout.add_widget(Label(text="" ) )
                    layout.add_widget(label)
                    # self.gl.add_widget(layout)
                else:
                    label = Label(text=self.userInput.text[i*10: i*10+10] , size_hint=(None,None), size=(self.width/2, 50) )
                    # layout = BoxLayout(orientation="horizontal")
                    layout.add_widget(Label(text="" ) )
                    layout.add_widget(label)
                    # self.gl.add_widget(layout)
                self.gl.add_widget(layout)
        

        reply = ask_chatbot(self.userInput.text)

        # adding space box
        self.gl.add_widget(Label(text="", size_hint=(None,None),size=(self.width,50)))

        # adding reply box
        label2 = Label(text=reply , size_hint=(None,None), size=(self.width/2, 50) ,color=[0.41, 0.42, 0.74, 1])
        layout2 = AnchorLayout()
        layout2.add_widget(label2)
        self.gl.add_widget(layout2)

        # adding space box
        self.gl.add_widget(Label(text="") )

        self.userInput.text=""

    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("debug.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()