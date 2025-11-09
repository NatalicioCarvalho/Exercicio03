preco = float(input("Digite o preço do produto: "))
codigo = int(input("Digite o código da condição de pagamento (1 a 4): "))

if codigo == 1:
    total = preco * 0.9
    print(f"À vista em dinheiro/cheque - Total com 10% de desconto: R$ {total:.2f}")
elif codigo == 2:
    total = preco * 0.95
    print(f"À vista no cartão - Total com 5% de desconto: R$ {total:.2f}")
elif codigo == 3:
    print(f"Em duas vezes - Total: R$ {preco:.2f}")
elif codigo == 4:
    total = preco * 1.10
    print(f"Em três vezes - Total com 10% de juros: R$ {total:.2f}")
else:
    print("Código de pagamento inválido.")