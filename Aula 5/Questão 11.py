import time
# Leia um número e: Se for par e positivo → “Par positivo”; Se for par e negativo → “Par negativo”; Caso contrário → “Ímpar”. 
numero = int(input("Digite seu numero: "))
print("Verificando se é Impar e Par negativo ou positivo...")

#programa vai passar 1.5 segundos verificando.
time.sleep(1.5)

#codigo das cores
red = "\033[31m"
green = "\033[32m"
blue = "\033[34m"
yellow = "\033[33m"
reset = "\033[0m"

#Decisão se é Negativo, Positivo ou igual a ZERO.
if numero > 0 and numero % 2 == 0:
    print(f"O número {yellow}{numero}{reset} é {green}Par e POSITIVO{reset}")
elif numero < 0 and numero % 2 == 0:
    print(f"O número {yellow}{numero}{reset} é {red}Par e NEGATIVO{reset}")
elif numero > 0 and numero % 2 != 0:
    print(f"O número {yellow}{numero}{reset} é {green}Ímpar e POSITIVO{reset}")
elif numero < 0 and numero % 2 != 0:
    print(f"O número {yellow}{numero}{reset} é {red}Ímpar e NEGATIVO{reset}")
