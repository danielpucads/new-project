import calculator

def menu():
    print("\n=== Calculadora Simples ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "0":
        print("Encerrando calculadora...")
        break

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if escolha == "1":
        print("Resultado:", calculator.add(a, b))
    elif escolha == "2":
        print("Resultado:", calculator.subtract(a, b))
    elif escolha == "3":
        print("Resultado:", calculator.multiply(a, b))
    elif escolha == "4":
        print("Resultado:", calculator.divide(a, b))
    else:
        print("Opção inválida!")