
import time 
#Leia um número (entrada padrão do input) e: Converta para inteiro; Exiba o dobro do valor.
numero = float(input("Digite seu numero: "))
print("Convertendo seu número para inteiro...")

#programa vai passar 0.5 segundos convertendo.
time.sleep(0.5)

print("Calculando o Dobro...")

#programa vai passar 0.5 segundos calculando.
time.sleep(0.5)

#codigo das cores
red = "\033[31m"
green = "\033[32m"
blue = "\033[34m"
yellow = "\033[33m"
reset = "\033[0m"

#convertendo.
convertido = int(numero)
result = convertido * 2

print(f"O número convertido para inteiro é {yellow}{convertido}{reset} e o Dobro do valor é {green}{result}{reset}")
