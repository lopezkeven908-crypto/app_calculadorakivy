# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window

#Tamaño de la ventana
Window.size = (700, 1500)
# ICONO DE LA APLICACION
Window.set_icon('ID2227887.png')

# Cargar el archivo de diseño .kv
Builder.load_file('plataforma.kv')

# Variable global para almacenar la expresión matemática
expresion = ''

# Clase principal del layout
class CalculadoraLayout(BoxLayout):
    def on_button_press(self, instance):
        global expresion
        texto = instance.text
        actual = self.ids.result.text

        # Botón de limpiar todo
        if texto == 'AC':
            expresion = ''
            self.ids.result.text = '0'

        # Botón de borrar último carácter
        elif texto == 'C':
            expresion = expresion[:-1]
            self.ids.result.text = expresion if expresion else '0'

        # Botón de igual (=)
        elif texto == '=':
            try:
                # Reemplazar símbolos visuales por operadores reales
                expresion_evaluable = expresion.replace('÷', '/').replace('×', '*').replace('–', '-')
                resultado = str(eval(expresion_evaluable))
                self.ids.result.text = resultado
                expresion = resultado
            except:
                self.ids.result.text = 'Error'
                expresion = ''

        # Cualquier otro botón (número u operador)
        else:
            if actual == '0' or actual == 'Error':
                expresion = texto
            else:
                expresion += texto
            self.ids.result.text = expresion

# Clase principal de la app
class CalculadoraApp(App):
    def build(self):
        self.title = 'Calculadora Cbta131' #tiitulo de la ventana
        set_icon = 'ID2227887.png' #icono de la ventana
        return CalculadoraLayout()

# Ejecutar la app
if __name__ == '__main__':
    CalculadoraApp().run()