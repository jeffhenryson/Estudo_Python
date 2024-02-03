# Exercício 13: Função de Filtragem de Listas
# Crie uma função filtra_pares_impares que receba uma lista de números inteiros
# e retorne duas listas: uma contendo todos os números pares e outra contendo todos 
# os números ímpares da lista original.

def filtra_pares_impares(lista):
    pares = []
    impares = []
    
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
    return pares, impares

# Exemplo de uso
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares, impares = filtra_pares_impares(lista_numeros)
print("Pares:", pares)
print("Ímpares:", impares)

        