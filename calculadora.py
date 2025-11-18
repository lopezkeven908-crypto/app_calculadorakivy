# main.py
import math  # usado para función de raíz cuadrada
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window

#Tamaño de la ventana
Window.size = (700, 1450)
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
                # EXPLICACIÓN PARA PRINCIPIANTES:
                # .replace() es un método que cambia texto por otro texto en una cadena
                # Sintaxis: cadena.replace('buscar', 'reemplazar')
                # Ejemplo: "5+3".replace('+', '-') = "5-3"
                
                # Reemplazar símbolos visuales por operadores que Python entiende:
                # ÷ (símbolo de división) → / (operador de Python)
                # × (símbolo de multiplicación) → * (operador de Python)
                # – (guión largo de resta) → - (operador de Python)
                # ^ (potencia) → ** (operador de potencia en Python)
                expresion_evaluable = expresion.replace('÷', '/').replace('×', '*').replace('–', '-').replace('^', '**')
                
                # eval() evalúa (calcula) una expresión matemática en forma de cadena de texto
                # Ejemplo: eval('5+3*2') = 11 (sigue el orden de operaciones)
                # ADVERTENCIA: eval() es poderoso pero puede ser peligroso si no se controla
                resultado = str(eval(expresion_evaluable))
                self.ids.result.text = resultado
                expresion = resultado
            except:
                self.ids.result.text = 'Error'
                expresion = ''

        # Punto decimal: permitir un solo punto por número
        elif texto == '.':
            # Si la pantalla contiene 'Error' o está vacía, iniciar con '0.'
            if actual == 'Error' or expresion == '':
                expresion = '0.'
                self.ids.result.text = expresion
            else:
                # EXPLICACIÓN PARA PRINCIPIANTES:
                # len(expresion) devuelve la longitud (cantidad de caracteres) de la cadena
                # Ejemplo: si expresion = "5+3", len(expresion) = 3
                # i = len(expresion) - 1 asigna a 'i' el índice del último carácter
                # En "5+3", i = 2 (índice del carácter '3')
                # isdigit() es un método que verifica si un carácter es un dígito (0-9)
                # Ejemplo: '5'.isdigit() = True, '+'.isdigit() = False
                
                # while: bucle que se repite mientras la condición sea verdadera
                # Este bucle recorre la expresión de derecha a izquierda hasta encontrar
                # un operador (+, -, ×, ÷) o llegar al inicio (i < 0)
                i = len(expresion) - 1
                while i >= 0 and (expresion[i].isdigit() or expresion[i] == '.'):
                    i -= 1
                
                # last_token = expresion[i+1:] extrae el último "token" (grupo de dígitos)
                # La notación [i+1:] significa "desde la posición i+1 hasta el final"
                # Ejemplo: si expresion = "5+3.2" e i = 1, last_token = "3.2"
                last_token = expresion[i+1:]
                
                # Agregar punto sólo si el token actual no tiene ya un punto
                if '.' not in last_token:
                    # Si el último carácter es un operador, anteponer '0'
                    if expresion.endswith(('+', '-', '×', '÷', '*', '/', '–')) or expresion == '':
                        expresion += '0.'
                    else:
                        expresion += '.'
                # Actualizar pantalla
                self.ids.result.text = expresion

        # Raíz cuadrada: aplica sqrt al número actualmente mostrado
        elif texto == '√':
            try:
                # EXPLICACIÓN PARA PRINCIPIANTES:
                # float() convierte una cadena de texto a número decimal
                # Ejemplo: float('5.5') convierte el texto '5.5' a número 5.5
                # actual contiene lo que se muestra en la pantalla (una cadena)
                valor = float(actual)
                
                # Validar que el número no sea negativo (raíz cuadrada de negativo = error)
                if valor < 0:
                    raise ValueError('negativo')
                
                # math.sqrt() calcula la raíz cuadrada
                # sqrt viene de "square root" (raíz cuadrada)
                # Ejemplo: math.sqrt(9) = 3.0, math.sqrt(16) = 4.0
                resultado = str(math.sqrt(valor))
                
                # Actualizar pantalla con el resultado
                self.ids.result.text = resultado
                expresion = resultado
            except Exception:
                # Si algo falla (texto inválido, número negativo, etc.) mostrar 'Error'
                self.ids.result.text = 'Error'
                expresion = ''

        # Potencia: permite calcular x^y (x elevado a la potencia y)
        # El usuario presiona '^' para indicar que quiere elevar a una potencia
        elif texto == '^':
            # Si hay un error o la expresión está vacía, no hacer nada
            if actual == 'Error' or expresion == '':
                return
            
            # Agregar el símbolo '^' a la expresión para que se vea en pantalla
            # Ejemplo: si el usuario presiona 2, luego ^, la pantalla muestra '2^'
            expresion += '^'
            self.ids.result.text = expresion

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