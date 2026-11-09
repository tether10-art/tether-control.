from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, RoundedRectangle
import random
import time

class RoundedCard(BoxLayout):
    def __init__(self, **kwargs):
        super(RoundedCard, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 15
        self.spacing = 5
        with self.canvas.before:
            Color(0.12, 0.12, 0.14, 1)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[15])
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class TetherUI(BoxLayout):
    def __init__(self, **kwargs):
        super(TetherUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        
        with self.canvas.before:
            Color(0.07, 0.07, 0.09, 1)
            self.bg = RoundedRectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)

        top_bar = BoxLayout(size_hint_y=None, height=50)
        top_bar.add_widget(Label(text="[b]Archer C6[/b]", markup=True, font_size=20, color=(1,1,1,1)))
        self.add_widget(top_bar)

        status_box = BoxLayout(size_hint_y=None, height=30)
        status_box.add_widget(Label(text="● يعمل بشكل جيد", font_size=14, color=(0.2, 0.8, 0.3, 1)))
        self.add_widget(status_box)

        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=15, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        speed_card = RoundedCard(size_hint_y=None, height=90)
        speed_card.add_widget(Label(text="معدل الرفع والتنزيل", font_size=14, color=(0.7,0.7,0.7,1)))
        self.speed_label = Label(text="↓ --    ↑ --", font_size=18, color=(1,1,1,1), bold=True)
        speed_card.add_widget(self.speed_label)
        grid.add_widget(speed_card)

        cards_layout = GridLayout(cols=2, spacing=15, size_hint_y=None, height=220)
        
        c1 = RoundedCard()
        c1.add_widget(Label(text="العملاء", font_size=14, color=(0.7,0.7,0.7,1)))
        c1.add_widget(Label(text="7 على الإنترنت", font_size=16, color=(1,1,1,1), bold=True))
        cards_layout.add_widget(c1)

        c2 = RoundedCard()
        c2.add_widget(Label(text="حالة الشبكة", font_size=14, color=(0.7,0.7,0.7,1)))
        c2.add_widget(Label(text="متصل بالإنترنت", font_size=16, color=(0.2,0.8,0.3,1), bold=True))
        cards_layout.add_widget(c2)

        c3 = RoundedCard()
        c3.add_widget(Label(text="إعدادات Wi-Fi", font_size=14, color=(0.7,0.7,0.7,1)))
        c3.add_widget(Label(text="نشط", font_size=16, color=(1,1,1,1), bold=True))
        cards_layout.add_widget(c3)

        c4 = RoundedCard()
        c4.add_widget(Label(text="قياس السرعة", font_size=14, color=(0.3, 0.6, 1, 1)))
        self.test_btn = Button(text="ابدأ الفحص", background_color=(0.1, 0.4, 0.8, 1), font_size=14)
        self.test_btn.bind(on_press=self.run_speed_test)
        c4.add_widget(self.test_btn)
        cards_layout.add_widget(c4)

        grid.add_widget(cards_layout)
        scroll.add_widget(grid)
        self.add_widget(scroll)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def run_speed_test(self, instance):
        self.test_btn.text = "جاري القياس..."
        import threading
        def calculate():
            time.sleep(2)
            dl = round(random.uniform(25.0, 95.0), 2)
            ul = round(random.uniform(5.0, 20.0), 2)
            self.speed_label.text = f"↓ {dl} Mbps    ↑ {ul} Mbps"
            self.test_btn.text = "إعادة الفحص"
        threading.Thread(target=calculate).start()

class MyApp(App):
    def build(self):
        return TetherUI()

if __name__ == '__main__':
    MyApp().run()

