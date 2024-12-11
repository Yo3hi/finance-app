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



