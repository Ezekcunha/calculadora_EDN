def calculadora():
    while True:
        try:
            num1_str = input("Digite o primeiro número: ")
            num1 = float(num1_str)
            num2_str = input("Digite o segundo número: ")
            num2 = float(num2_str)
            operacao = input("Digite a operação (+, -, *, /): ")

            if operacao == '+':
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
                break
            elif operacao == '-':
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
                break
            elif operacao == '*':
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
                break
            elif operacao == '/':
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                else:
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}")
                    break
            else:
                print("Erro: Operação inválida. As operações válidas são +, -, *, /.")

        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite números.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if _name_ == "_main_":
    calculadora()
    print("Calculadora encerrada.")
    from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Define as dimensões iniciais da janela (útil para desktop)
Window.size = (300, 400)

class CalculadoraLayout(GridLayout):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        self.cols = 2  # Organiza os widgets em 2 colunas

        # Entrada para o primeiro número
        self.add_widget(Label(text="Número 1:"))
        self.num1_input = TextInput(multiline=False)
        self.add_widget(self.num1_input)

        # Entrada para o segundo número
        self.add_widget(Label(text="Número 2:"))
        self.num2_input = TextInput(multiline=False)
        self.add_widget(self.num2_input)

        # Entrada para a operação
        self.add_widget(Label(text="Operação (+, -, *, /):"))
        self.operacao_input = TextInput(multiline=False)
        self.add_widget(self.operacao_input)

        # Label para exibir o resultado ou mensagens de erro
        self.resultado_label = Label(text="Resultado:")
        self.add_widget(self.resultado_label)

        # Botão para realizar o cálculo
        self.calcular_button = Button(text="Calcular")
        self.calcular_button.bind(on_press=self.calcular)  # Vincula a função calcular ao clique do botão
        self.add_widget(self.calcular_button)

    def calcular(self, instance):
        try:
            num1 = float(self.num1_input.text)
            num2 = float(self.num2_input.text)
            operacao = self.operacao_input.text

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    resultado = "Erro: Divisão por zero!"
                else:
                    resultado = num1 / num2
            else:
                resultado = "Erro: Operação inválida!"

            self.resultado_label.text = f"Resultado: {resultado}"

        except ValueError:
            self.resultado_label.text = "Erro: Entrada inválida!"
        except Exception as e:
            self.resultado_label.text = f"Erro: {e}"

class CalculadoraApp(App):
    def build(self):
        return CalculadoraLayout()

if _name_ == '_main_':
    CalculadoraApp().run()
    import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (300, 400)

class CalculadoraLayout(GridLayout):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Número 1:"))
        self.num1_input = TextInput(multiline=False)
        self.add_widget(self.num1_input)
        self.add_widget(Label(text="Número 2:"))
        self.num2_input = TextInput(multiline=False)
        self.add_widget(self.num2_input)
        self.add_widget(Label(text="Operação (+, -, *, /):"))
        self.operacao_input = TextInput(multiline=False)
        self.add_widget(self.operacao_input)
        self.resultado_label = Label(text="Resultado:")
        self.add_widget(self.resultado_label)
        self.calcular_button = Button(text="Calcular")
        self.calcular_button.bind(on_press=self.calcular)
        self.add_widget(self.calcular_button)

    def calcular(self, instance):
        try:
            num1 = float(self.num1_input.text)
            num2 = float(self.num2_input.text)
            operacao = self.operacao_input.text
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    resultado = "Erro: Divisão por zero!"
                else:
                    resultado = num1 / num2
            else:
                resultado = "Erro: Operação inválida!"
            self.resultado_label.text = f"Resultado: {resultado}"
        except ValueError:
            self.resultado_label.text = "Erro: Entrada inválida!"
        except Exception as e:
            self.resultado_label.text = f"Erro: {e}"

class CalculadoraApp(App):
    def build(self):
        return CalculadoraLayout()

if _name_ == '_main_':
    CalculadoraApp().run()