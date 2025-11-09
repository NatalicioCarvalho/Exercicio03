a = int(input("Digite o primeiro valor inteiro (A): "))
b = int(input("Digite o segundo valor inteiro (B): "))
c = int(input("Digite o terceiro valor inteiro (C): "))

if a == b or a == c or b == c:
    print("ERRO: Você deve digitar três valores diferentes.")
else:
    # A é o maior
    if a > b and a > c:
        if b > c:
            print(f"Ordem Decrescente: {a}, {b}, {c}")
        else:
            print(f"Ordem Decrescente: {a}, {c}, {b}")

    # B é o maior
    elif b > a and b > c:
        if a > c:
            print(f"Ordem Decrescente: {b}, {a}, {c}")
        else:
            print(f"Ordem Decrescente: {b}, {c}, {a}")

    # C é o maior
    else:
        if a > b:
            print(f"Ordem Decrescente: {c}, {a}, {b}")
        else:
            print(f"Ordem Decrescente: {c}, {b}, {a}")