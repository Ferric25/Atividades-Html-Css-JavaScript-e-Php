contador = 0
def incrementar_contador():
     global contador
     contador += 1
     print(f"Contador atualizado: {contador}")
     mensagem = str("Esta é uma mensagem local.")
     print(mensagem)
incrementar_contador()
print(mensagem)

