# Exercício 7: Função inverte_lista
# Crie uma função inverte_lista que receba uma lista como argumento e retorne uma nova lista com os
# elementos na ordem inversa.

# Dica: Você pode usar o slicing de lista para fazer isso de forma concisa (lista[::-1]), ou usar um 
# método de lista.

def inverte_lista(lista):
    return lista[::-1]


lista_original = [1, 2, 3, 4, 5]
lista_invertida = inverte_lista(lista_original)
print(lista_invertida)  
