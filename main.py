import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import requests

class CapriUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        self.chat_log = Label(
            text="Привет! Я Капри. Напиши мне что-нибудь.",
            font_size='18sp',
            halign='left',
            valign='top',
            size_hint_y=0.7
        )
        self.chat_log.bind(size=self.chat_log.setter('text_size'))
        self.add_widget(self.chat_log)

        self.input_box = TextInput(
            multiline=False,
            size_hint_y=0.15,
            font_size='18sp',
            hint_text="Твой вопрос..."
        )
        self.add_widget(self.input_box)

        self.send_btn = Button(
            text="Отправить",
            size_hint_y=0.15,
            font_size='20sp',
            background_color=(0.1, 0.7, 0.8, 1)
        )
        self.send_btn.bind(on_press=self.send_message)
        self.add_widget(self.send_btn)

    def send_message(self, instance):
        user_text = self.input_box.text.strip()
        if not user_text:
            return
        
        self.chat_log.text += f"\n\nВы: {user_text}"
        self.input_box.text = ""
        self.send_btn.disabled = True
        
        threading.Thread(target=self.get_ai_response, args=(user_text,), daemon=True).start()

    def get_ai_response(self, prompt):
        try:
            server_url = "http://127.0.0.1:5001/chat"
            data = {"prompt": prompt}
            response = requests.post(server_url, json=data, timeout=20)
            
            if response.status_code == 200:
                ai_text = response.json().get('response', 'Нет ответа')
                Clock.schedule_once(lambda dt: self.update_ui(ai_text))
            else:
                Clock.schedule_once(lambda dt: self.update_ui(f"Ошибка сервера: {response.status_code}"))
        except Exception as e:
            Clock.schedule_once(lambda dt: self.update_ui(f"Нет связи с сервером: {str(e)}"))

    def update_ui(self, text):
        self.chat_log.text += f"\n\nКапри: {text}"
        self.send_btn.disabled = False

class CapriApp(App):
    def build(self):
        self.title = "Capri AI"
        return CapriUI()

if __name__ == '__main__':
    CapriApp().run()
