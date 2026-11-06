from kivy.app import App
from kivy.uix.label import Label

class CapriTestApp(App):
    def build(self):
        return Label(text="Капри на связи!", font_size='30sp')

if __name__ == '__main__':
    CapriTestApp().run()
