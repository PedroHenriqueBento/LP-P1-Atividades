numero = int(input("Digite um número: "))

if numero == 0:
    print(f"O número {numero} é neutro!")
elif numero > 0 and numero % 2 == 0:
    print(f"O número {numero} é par positivo!")
elif numero > 0 and numero % 2 != 0:
    print(f"O número {numero} é ímpar positivo!")
elif numero < 0 and numero % 2 == 0:
    print(f"O número {numero} é par negativo!")
else:
    print(f"O número {numero} é ímpar negativo!")
