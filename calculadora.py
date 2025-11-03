from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.result = Label(text='0', font_size=40, size_hint=(1, 0.2), halign='right', valign='middle')
        self.result.bind(size=self.result.setter('text_size'))
        self.add_widget(self.result)

        buttons = [
            ['AC', 'C', '='],
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['0', '÷', 'x', '-']
        ]

        grid = GridLayout(cols=4, spacing=10, padding=10)

        for row in buttons:
            for label in row:
                btn = Button(text=label, font_size=32)
                btn.background_color = self.get_color(label)
                btn.bind(on_press=self.on_button_press)
                grid.add_widget(btn)

        self.add_widget(grid)

    def get_color(self, label):
        if label in ['AC', 'C', '=']:
            return (1, 0, 0, 1)  # Rojo
        elif label in ['÷', 'x', '-']:
            return (0, 1, 0, 1)  # Verde
        else:
            return (0, 0, 1, 1)  # Azul

    def on_button_press(self, instance):
        text = instance.text
        current = self.result.text

        if text == 'AC':
            self.result.text = '0'
        elif text == 'C':
            self.result.text = current[:-1] if current != '0' else '0'
        elif text == '=':
            try:
                expression = current.replace('÷', '/').replace('x', '*')
                self.result.text = str(eval(expression))
            except:
                self.result.text = 'Error'
        else:
            if current == '0':
                self.result.text = text
            else:
                self.result.text += text

class CalculadoraApp(App):
    def build(self):
        return CalculatorLayout()

if __name__ == '__main__':
    CalculadoraApp().run()