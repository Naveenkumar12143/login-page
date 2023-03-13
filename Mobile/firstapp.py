import kivy
# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
#
# class childApp(GridLayout):
#     def __init__(self, **kwargs):
#         super(childApp, self).__init__()
#         self.cols = 3
#         self.add_widget(Label(text='Student Name'))
#         self.s_name = TextInput()
#         self.add_widget(self.s_name)
#
#         self.add_widget(Label(text='Student Marks'))
#         self.s_marks = TextInput()
#         self.add_widget(self.s_marks)
#
#         self.add_widget(Label(text='Student Gender'))
#         self.s_gender = TextInput()
#         self.add_widget(self.s_gender)
#
#         self.press = Button(text='click me')
#         self.press.bind(on_press= self.click_me)
#         self.add_widget(self.press)
#
#     def click_me(self, instance):
#         print("Name of student is "+self.s_name.text)
#         print("Marks of student is " + self.s_marks.text)
#         print("Gender of student is " + self.s_gender.text)
#         print("")
#
# class parentApp(childApp):
#     def build(self):
#         return childApp
#
#
# if __name__== "__main__":
#     parentApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        b1 = BoxLayout()
        button1 = Button(text='Hello')
        button2 = Button(text='world')
        b1.add_widget(button1)
        b1.add_widget(button2)
        return b1


if __name__== "__main__":
    MyApp().run()

