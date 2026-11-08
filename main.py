import threading
import urllib.request
import json
import ssl
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class ChatScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.scroll = ScrollView(size_hint=(1, 0.7))
        self.chat_layout = GridLayout(cols=1, size_hint_y=None, spacing=10)
        self.chat_layout.bind(minimum_height=self.chat_layout.setter('height'))
        self.scroll.add_widget(self.chat_layout)
        self.add_widget(self.scroll)

        self.add_message("Капри", "Привет! Я Капри. Напиши мне что-нибудь.", (0.2, 0.6, 0.8, 1))

        input_layout = BoxLayout(size_hint=(1, 0.15), spacing=10)
        self.input_box = TextInput(multiline=False, font_size='18sp', hint_text="Твой вопрос...")
        input_layout.add_widget(self.input_box)

        self.send_btn = Button(text="Отправить", size_hint_x=0.3, background_color=(0.1, 0.7, 0.8, 1))
        self.send_btn.bind(on_press=self.send_message)
        input_layout.add_widget(self.send_btn)
        self.add_widget(input_layout)

    def add_message(self, sender, text, color):
        msg_label = Label(
            text=f"[b]{sender}:[/b] {text}",
            markup=True, halign='left', valign='top', size_hint_y=None, color=color
        )
        msg_label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        msg_label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.chat_layout.add_widget(msg_label)
        Clock.schedule_once(lambda dt: setattr(self.scroll, 'scroll_y', 0), 0.1)

    def send_message(self, instance):
        user_text = self.input_box.text.strip()
        if not user_text: return
        
        self.add_message("Вы", user_text, (1, 1, 1, 1))
        self.input_box.text = ""
        self.send_btn.disabled = True
        self.add_message("Капри", "Думает...", (0.5, 0.5, 0.5, 1))
        
        threading.Thread(target=self.get_ai_response, args=(user_text,), daemon=True).start()

    def get_ai_response(self, prompt):
        try:
            # ТВОЙ АДРЕС CLOUDFLARE
            server_url = "https://lucky-field-55a6.efimkojnov.workers.dev"
            
            data = {"messages": [{"role": "user", "content": prompt}]}
            
            context = ssl._create_unverified_context()
            req = urllib.request.Request(
                server_url,
                data=json.dumps(data).encode('utf-8'),
                headers={'Content-Type': 'application/json'}
            )
            
            with urllib.request.urlopen(req, timeout=20, context=context) as response:
                result = json.loads(response.read().decode('utf-8'))
                if "error" in result:
                    ai_text = f"Ошибка сервера: {result['error']}"
                else:
                    ai_text = result['choices'][0]['message']['content']
                Clock.schedule_once(lambda dt: self.update_ui(ai_text))
                
        except Exception as e:
            Clock.schedule_once(lambda dt: self.update_ui(f"Ошибка сети: {str(e)}"))

    def update_ui(self, text):
        self.chat_layout.remove_widget(self.chat_layout.children[0])
        self.add_message("Капри", text, (0.2, 0.8, 0.4, 1))
        self.send_btn.disabled = False

class CapriApp(App):
    def build(self):
        self.title = "Capri AI"
        return ChatScreen()

if __name__ == '__main__':
    CapriApp().run()
