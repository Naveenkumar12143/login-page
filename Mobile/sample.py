from kivy.app import App
from kivy.lang import Builder

kv = """
Screen:
    GridLayout:
        cols: 2
        rows:2
        Label:
            text:"Student name: "
        TextInput:
            id:s_name
        Label:
            text:"Student gender: "
        TextInput:
            id:s_gender
"""

class ParentApp(App):
    screen = None
    def build(self):
        self.screen = Builder.load_string(kv)
        return self.screen


if __name__ == "__main__":
    ParentApp().run()