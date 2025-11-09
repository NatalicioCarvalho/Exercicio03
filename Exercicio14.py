codigo_produto = int(input("Digite o código do produto (1 a 10): "))
peso_kg = float(input("Digite o peso do produto em quilos: "))
codigo_pais = int(input("Digite o código do país de origem (1 a 3): "))

peso_gramas = peso_kg * 1000

if 1 <= codigo_produto <= 4:
    preco_grama = 10
elif 5 <= codigo_produto <= 7:
    preco_grama = 25
else:
    preco_grama = 35

if codigo_pais == 1:
    imposto = 0
elif codigo_pais == 2:
    imposto = 0.15
else:
    imposto = 0.25

valor_sem_imposto = peso_gramas * preco_grama / 100
valor_total = valor_sem_imposto * (1 + imposto)

print(f"\nPeso em gramas: {peso_gramas:.0f} g")
print(f"Preço sem imposto: R$ {valor_sem_imposto:.2f}")
print(f"Imposto aplicado: {imposto * 100:.0f}%")
print(f"Valor total a pagar: R$ {valor_total:.2f}")
