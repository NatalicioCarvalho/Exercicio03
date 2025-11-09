# Entrada de dados
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
opcao = input("Escolha uma opção: (a) Média, (b) Diferença, (c) Produto: ")

# Estrutura condicional
if opcao == "a":
    media = (num1 + num2) / 2
    print("A média é:", media)
elif opcao == "b":
    diferenca = num1 - num2
    print("A diferença é:", diferenca)
elif opcao == "c":
    produto = num1 * num2
    print("O produto é:", produto)
else:
    print("Opção inválida!")
