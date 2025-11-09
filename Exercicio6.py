n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == '+':
    print("Resultado:", n1 + n2)
elif operacao == '-':
    print("Resultado:", n1 - n2)
elif operacao == '*':
    print("Resultado:", n1 * n2)
elif operacao == '/':
    if n2 != 0:
        print("Resultado:", n1 / n2)
    else:
        print("Erro: divisão por zero não é permitida.")
else:
    print("Operação inválida.")
   



