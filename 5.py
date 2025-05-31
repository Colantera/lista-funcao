# Implemente uma calculadora simples em Python utilizando funções. A
# calculadora deve ser capaz de realizar as seguintes operações
# matemáticas básicas:
# • Soma
# • Subtração
# • Multiplicação
# • Divisão
# Requisitos:
# • Crie uma função para cada operação matemática (soma,
# subtração, multiplicação e divisão). As funções devem receber
# dois valores e retornar o resultado da operação.
# • Implemente uma função para exibir o menu de opções para o
# usuário.
# • O programa deve repetir o menu após cada operação, até que
# o usuário escolha a opção de sair.

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Não é possível dividir por zero."
    else:
        return a / b

def calculadora():
    while True:
        print("\n--- Menu da Calculadora ---")
        print("Escolha uma operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")
        
        escolha = input("Digite a sua opção (1/2/3/4/5): ")

        if escolha == '5':
            print("Obrigado por usar a calculadora!")
            break 

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, digite apenas números.")
                continue

            if escolha == '1':
                resultado = somar(num1, num2)
                print(f"O resultado da soma é: {resultado}")
            elif escolha == '2':
                resultado = subtrair(num1, num2)
                print(f"O resultado da subtração é: {resultado}")
            elif escolha == '3':
                resultado = multiplicar(num1, num2)
                print(f"O resultado da multiplicação é: {resultado}")
            elif escolha == '4':
                resultado = dividir(num1, num2)
                print(f"O resultado da divisão é: {resultado}")
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

calculadora()