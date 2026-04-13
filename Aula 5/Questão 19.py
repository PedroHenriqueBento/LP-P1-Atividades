n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 == n2:
    print(f"Os números {n1} e {n2} são iguais!")
else:
    diferenca = abs(n1 - n2)
    print(f"Os números {n1} e {n2} são diferentes!")
    print(f"A diferença entre eles é {diferenca}")
