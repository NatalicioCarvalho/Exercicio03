altura = float(input("Digite sua altura (em metros): "))
sexo = input("Digite o sexo (M/F): ")
if sexo == "M":
     peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = 0
    print("Sexo inválido!")

if peso_ideal > 0:
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
