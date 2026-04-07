#Leia um número e: Se for positivo, mostre a raiz aproximada (use **0.5); Caso contrário, informe “Número inválido”
numero = float(input("Digite um número: "))

if numero >= 0:
    raiz = numero ** 0.5
    print(f"A raiz aproximada de {numero} é {raiz}")
else:
    print(f"O número {numero} é inválido para calcular raiz")
