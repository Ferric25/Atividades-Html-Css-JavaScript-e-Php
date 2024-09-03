nota1 = nota2 = nota3 = nota4 = media = 0

nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))
nota3 = float(input("Digite sua nota: "))
nota4 = float(input("Digite sua nota: ")) 
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 7:
    print(f"Sua média foi {media}, você foi aprovado!")
else:
    print(f"Sua média foi {media}, você foi reprovado!")