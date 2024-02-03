# Exercício 8: Função filtro_par
# Defina uma função filtro_par que receba uma lista de números inteiros e retorne uma nova lista 
# contendo apenas os números pares da lista original.

# Dica: Use uma compreensão de lista com uma condição para filtrar os números pares.

def filtro_par(lista):
    return [x for x in lista if x % 2 == 0]

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = filtro_par(lista_numeros)
print(lista_pares)  #
