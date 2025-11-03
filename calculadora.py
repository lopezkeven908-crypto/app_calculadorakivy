# Importamos las clases necesarias de Kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Cargamos el archivo de diseño .kv
Builder.load_file('plataforma.kv')

# Clase principal que maneja la lógica de la calculadora
class CalculatorLayout(BoxLayout):
    # Función que se ejecuta al presionar un botón
    def on_button_press(self, instance):
        text = instance.text              # Texto del botón presionado
        current = self.ids.result.text    # Texto actual en pantalla

        if text == 'AC':
            self.ids.result.text = '0'    # Reinicia la pantalla
        elif text == 'C':
            # Borra el último carácter si no es solo '0'
            self.ids.result.text = current[:-1] if current != '0' else '0'
        elif text == '=':
            try:
                # Reemplaza símbolos por operadores reales
                expression = current.replace('÷', '/').replace('x', '*')
                # Calcula el resultado usando eval
                self.ids.result.text = str(eval(expression))
            except:
                self.ids.result.text = 'Error'  # Muestra error si falla
        else:
            # Si el texto es '0', lo reemplaza
            if current == '0':
                self.ids.result.text = text
            else:
                # Si ya hay texto, lo agrega al final
                self.ids.result.text += text

# Clase principal de la app
class CalculadoraApp(App):
    def build(self):
        return CalculatorLayout()  # Devuelve el layout principal

# Ejecuta la app si este archivo es el principal
if __name__ == '__main__':
    CalculadoraApp().run()