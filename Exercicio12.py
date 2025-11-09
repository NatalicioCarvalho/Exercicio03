salario = float(input("Digite o salário do funcionário: "))

if salario < 500:
    novo_salario = salario * 1.3
    print("O funcionário teve aumento! Novo salário: R$", novo_salario)
else:
    print("O funcionário não tem direito ao aumento.")
