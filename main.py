from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class ZohairSuiteMobile(App):
    def build(self):
        root = BoxLayout(orientation="vertical")

        self.label = Label(text="ZohairSuite Mobile PDF Reader", font_size=22)
        root.add_widget(self.label)

        root.add_widget(Button(text="Open PDF"))
        root.add_widget(Button(text="Prev Page"))
        root.add_widget(Button(text="Next Page"))

        return root

if __name__ == "__main__":
    ZohairSuiteMobile().run()
