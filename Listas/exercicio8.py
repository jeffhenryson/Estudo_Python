# Exercício 8: Filtragem Condicional
# Dada a lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], use uma compreensão de lista para criar 
# uma nova lista contendo apenas os números que são divisíveis por 3.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_divisiveis = [x for x in numeros if x % 3 == 0]
print(numeros_divisiveis)
