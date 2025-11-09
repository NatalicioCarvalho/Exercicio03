codigo = int(input("Digite o código do produto: "))

if codigo == 1:
    print("Alimento não-perecível")
elif codigo in [2, 3, 4]:
    print("Alimento perecível")
elif codigo in [5, 6]:
    print("Vestuário")
elif codigo == 7:
    print("Higiene pessoal")
elif 8 <= codigo <= 15:
    print("Limpeza e utensílios domésticos")
else:
    print("Código inválido")