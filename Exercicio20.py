l1 = float(input("Digite o comprimento do primeiro lado (L1): "))
l2 = float(input("Digite o comprimento do segundo lado (L2): "))
l3 = float(input("Digite o comprimento do terceiro lado (L3): "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    
    print("É POSSÍVEL formar um triângulo.")
    
    # Classificação
    if l1 == l2 and l2 == l3:
        print("O triângulo é do tipo: EQUILÁTERO.")
        
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("O triângulo é do tipo: ISÓSCELES.")
        
    else:
        print("O triângulo é do tipo: ESCALENO.")

else:
    print("NÃO É POSSÍVEL formar um triângulo com estes lados.")