while True:
    nota = int(input("Digite sua nota"))
    if nota >= 0 and nota <= 10:
        print(f"Sua nota é {nota}")
        break
    else:
        print("Incorreto")
