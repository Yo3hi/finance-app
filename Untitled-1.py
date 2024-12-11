import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
kivy.require('1.9.0')

#home page creation

        
    
     


class sign_in_page(BoxLayout):

    def __init__(self):
        super(sign_in_page, self).__init__()
    
        self.add_widget(Label(text="Username: "))
    #adding widget
        self.username = TextInput(multiline=False)
    #adding input box 
        self.add_widget(self.username)
    #adding widget

        self.add_widget(Label(text="password: "))
        self.password = TextInput(multiline=False)
        self.add_widget(self.password)

        self.submit = Button(text = "Submit", font_size = 32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        #values gotten from the textinputs
        username = self.username.text
        password = self.password.text
        print("hello " + username + " are you a sigma and is your password " + password + "?")

    def build(self):
        return sign_in_page()


class financeapp(App):
    #starts the building process, makes the homepage then on select will go to sign in or register
    def build(self):
        return homepage()



class homepage(BoxLayout):
    
    def __init__(self):
        super(homepage, self).__init__()
        
        
        self.sign_in = Button(text = "sign in", font_size = 32)
        self.sign_in.bind(on_press=self.sign_in_press)
        self.add_widget(self.sign_in)

        self.register = Button(text = "register", font_size = 32)
        self.register.bind(on_press=self.register_press)
        self.add_widget(self.register)
        

    def sign_in_press(self, instance):
        print("hi")
        variable = sign_in_page()
        variable.build
        
    

    def register_press(self,instance):
        pass


financeapp = financeapp()
financeapp.run()
