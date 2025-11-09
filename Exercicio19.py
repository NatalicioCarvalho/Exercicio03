a = int(input("Digite o primeiro número (A): "))
b = int(input("Digite o segundo número (B): "))
c = int(input("Digite o terceiro número (C): "))

if a >= b and a >= c:
    print(f"O maior número digitado é o A: {a}")
elif b >= a and b >= c:
    print(f"O maior número digitado é o B: {b}")
else:
    # Se nem A, nem B são os maiores, C deve ser o maior
    print(f"O maior número digitado é o C: {c}")