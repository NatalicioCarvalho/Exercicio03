ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = 2025
idade = ano_atual - ano_nascimento

print(f"Idade: {idade} anos")

if idade >= 18:
    print("Pode votar e tirar habilitação.")
elif idade >= 16:
    print("Pode votar, mas não pode tirar habilitação.")
else:
    print("Ainda não pode votar nem tirar habilitação.")