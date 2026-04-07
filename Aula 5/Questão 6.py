import time
#Leia dois números e exiba qual é o maior.
numero1 = float(input("Digite seu primeiro número aqui: "))
numero2 = float(input("Digite seu segundo número aqui: "))

#Programa vai verificar por 0.6 segundos qual é o maior
print("Verificando qual número é maior...")

time.sleep(0.6)

if numero1 > numero2:
    print(f"O número {numero1} é Maior que o número {numero2}")
elif numero2 > numero1:
    print(f"O número {numero2} é Maior que o número {numero1}")
else:
    print(f"O número {numero1} e {numero2} são iguais >:)")
