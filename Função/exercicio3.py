# Exercício 3: Lista de Quadrados
# Escreva uma função quadrados que aceite um número n e retorne uma lista dos quadrados
# de todos os números de 1 a n.

def quadrados(n):
    numeros = []  # Esta deve ser a lista para armazenar os quadrados
    for loop in range(1, n + 1):
        numeros.append(loop ** 2)  # Adicione cada quadrado à lista
    return numeros  # Retorne a lista completa fora do loop

print(quadrados(10))