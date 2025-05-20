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
   
