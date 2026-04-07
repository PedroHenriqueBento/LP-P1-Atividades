# Leia um valor e: Converta para inteiro; Se for múltiplo de 3 → “Múltiplo de 3”; Senão → “Não é múltiplo”.
import time
numero = float(input("Digite seu número e descubri se é múltiplo de 3"))

print("Verificando se é múltiplo de 3")
#Verificando se é multiplo de 3 por 0.5 segundos
time.sleep(0.5)

numero_inteiro = int(numero)
if numero_inteiro % 3 == 0:
  print(f"O número {numero_inteiro} é múltiplo de 3")
else:
    print(f"O número {numero_inteiro} não é múltiplo de 3")
