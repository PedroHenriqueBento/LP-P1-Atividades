import time 
#Leia um número inteiro e informe se ele é positivo ou negativo.
numero = int(input("Digite seu numero: "))
print("Verificando se é negativo ou positivo...")

#programa vai passar 1.5 segundos verificando.
time.sleep(1.5)

#codigo das cores
red = "\033[31m"
green = "\033[32m"
blue = "\033[34m"
reset = "\033[0m"

#Decisão se é Negativo, Positivo ou igual a ZERO.
if numero > 0:
    print(f"O número {green}{numero}{reset} é {green}POSITIVO{reset}")
elif numero < 0:
    print(f"O número {red}{numero}{reset} é {red}NEGATIVO{reset}")
else:
    print("O número digitado é ZERO")
