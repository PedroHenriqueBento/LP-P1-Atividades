# Leia um número e informe: “Dentro do intervalo” se estiver entre 0 e 10; “Fora do intervalo”
caso contrário.
numero = float(input("Digite um número: "))

if 0 <= numero <= 10:
    print(f"O número {numero} está dentro do intervalo de 0 a 10")
else:
    print(f"O número {numero} está fora do intervalo de 0 a 10")
