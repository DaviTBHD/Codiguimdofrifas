import random
import string

def gerar_codigo_free_fire(qtd=1):
    codigos = []
    for _ in range(qtd):
        codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        codigos.append(codigo)
    return codigos

# Exemplo de uso:
quantidade = int(input("Quantos códigos você deseja gerar? "))
codigos_gerados = gerar_codigo_free_fire(quantidade)

print("\nCódigos gerados:")
for codigo in codigos_gerados:
    print(codigo)